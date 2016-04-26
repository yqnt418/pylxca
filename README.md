## Welcome to PyLXCA

PyLXCA command-line interface (CLI) provides a Python-based library of commands to automate provisioning and resource management from an OpenStack environment, such as Ansible or Puppet.

The Lenovo XClarity Administrator PYLXCA CLI provide an interface to Lenovo XClarity Administrator REST APIs to automate functions such as:
*	Logging in to Lenovo XClarity Administrator
*	Managing and unmanaging chassis, servers, storage systems, and top-of-rack switches (endpoints)
*	Viewing inventory data for endpoints and components
*	Deploying an operating-system image to one or more servers
*	Configuring servers through the use of Configuration Patterns
*	Applying firmware updates to endpoints

## Code Example

python lxca_shell
connect -l https://10.241.106.216 -u USERID --noverify
connect -l https://10.241.106.216 -u USERID

Example to call lxca_cmd pytohn module from python script or Ansible module

from pylxca.pylxca_cmd.lxca_pyshell import *
pyshell()
con1 = connect("https://10.241.106.216","USERID","CME44ibm","True")

Several sample scripts are also available to help you to quickly begin using the PYLXCA command-line interface (CLI) to manage endpoints. 
The sample scripts are location in the following directory:
lib/python2.7/site-packages/pylxca-1.0-py2.7.egg/pylxca\test

## Installation
To use the PYLXCA command-line interface (CLI), you must install the CLI and start a command session.

**Before you begin**
Python (including the request and logging modules) is required to use to the PYLXCA CLI. Ensure at the following requirements are met. For more information about Python, see the [Link]www.python.org website. 
*	Python v2.7.x (Later versions have not been tested.)
*	Python requests v2.7.0 or later
*	Python logging v0.4.9.6 or later

Procedure
Complete the following steps to install the PYLXCA CLI.
1.	Download the toolkit by clicking Help ( )> Resources from the Lenovo XClarity Administrator title bar, and then clicking Download PYLXCA CLI from the dialog.
2.	Unzip the package into a local directory.
3.	Run the following command to install the module:
easy_install unzip_directory\pylxca-1.0-py2.7.egg
4.	Start a Python shell session.

$lxca_shell

--------------------------------------------------
Welcome to PyLXCA Shell v1.0
Type "help" at any time for a list of commands.
Type "pyshell" at any time to get interactive python shell
--------------------------------------------------
PyLXCA >>

5.	Validate that the module was installed correctly by running the following command:
In Python Shell Try to import pylxca module as follows

>>> import pylxca

If python able to import pylxca without any error then it is installed correctly.

## API Reference

PyLXCA command reference is available at 
[Link]http://ralfss30.labs.lenovo.com:8120/help/topic/com.lenovo.lxca.doc/pycli_overview.html

## License

(C) Copyright Lenovo 2015.
LIMITED AND RESTRICTED RIGHTS NOTICE:
If data or software is delivered pursuant a General Services
Administration (GSA) contract, use, reproduction, or disclosure
is subject to restrictions set forth in Contract No. GS-35F-05925.