'''
@since: 4 Sep 2015
@author: Prashant Bhosale <pbhosale@lenovo.com>
@license: Lenovo License
@copyright: Copyright 2016, Lenovo
@organization: Lenovo 
@summary: This module is for creating a connection session object for given xHMC.

'''

import requests
import logging, json
import os, platform
from _socket import timeout
from requests.sessions import session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

logger = logging.getLogger(__name__)

class lxcaAdapter(HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):

        self.poolmanager = PoolManager(num_pools=connections,

                                       maxsize=maxsize,

                                       block=block,

                                       assert_hostname='localhost')


class Error(Exception):
    """This exception is raised for any other low level errors """
    pass

class ConnectionError(Error):
    """This exception is raised when a connection related problem occurs, where a retry might make sense."""
    pass

class lxca_connection():
    '''
    C
    '''
    def __init__(self, url, user = None,  passwd = None, verify_callback = True, retries = 3):
        self.url = url
        self.user = user
        self.passwd = passwd
        self.retires = retries 
        self.debug = False
        self.session = None
        #self.verify_callback = verify_callback
        #os.environ['REQUESTS_CA_BUNDLE'] = os.path.join('/etc/ssl/certs/','ca-certificates.crt')
        if verify_callback:
            self.verify_callback = os.environ['REQUESTS_CA_BUNDLE']
        else:
            self.verify_callback = verify_callback
        
    def __repr__(self):
        return "%s(%s, %s, debug=%s)" %(self.__class__.__name__, `self.url`, self.user, `self.debug`)

    def connect(self):
        '''
        connection function
        '''
        try:
            logger.debug("Establishing Connection")
            self.session = requests.session()
            self.session.verify = self.verify_callback
            self.session.headers.update({'content-type': 'application/json; charset=utf-8'})
            payload = dict(UserId= self.user, password=self.passwd)
            pURL = self.url + '/sessions'
            self.session.mount(self.url, lxcaAdapter(max_retries=self.retires))
            r = self.session.post(pURL,data = json.dumps(payload),headers=dict(Referer=pURL),verify=self.verify_callback)
            r.raise_for_status()
        except ConnectionError as e:
            logger.debug("Connection Exception: Exception = %s", e)
            return False
        except Exception as e:
            logger.debug("Connection Exception: Exception = %s", e)
            return False
        except requests.exceptions.HTTPError as e:
            logger.debug("Connection Exception: Exception = %s", e.response.text)
            return False
        return  True

    def test_connection(self):
        '''
        Test Connection from requests module
        '''
        try:
            test_url = self.url + '/aicc'
            resp = self.session.get(test_url,verify=self.session.verify, timeout=3)
            #If valid JSON object is parsed then the connection is successfull
            py_obj = json.loads(resp.text)
        except Exception as e:
            raise ConnectionError("Invalid connection")
        return 

    def get_url(self):
        return self.url
    
    def get_session(self):
        return self.session
    
    def disconnect(self):
        '''
        session Disconnection
        '''
        self.url = None
        self.user = None
        self.passwd = None
        self.debug = False
        self.session.close()
        self.session = None

    def ping(self, host):
        """
        Returns True if host responds to a ping request
        """

        # Ping parameters as function of OS
        ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

        # Ping
        return os.system("ping " + ping_str + " " + host) == 0
