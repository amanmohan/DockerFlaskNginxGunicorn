==============
Cisco Project
==============

Create a Python project runBook automation task to have a master control a bunch of servers as minions.

We can run this project on local machine or can create docker image(Docker setup using Flask, Gunicorn, and Nginx.).

We have used following tools to approach the solution.


Introduction of tools
=====================

1. Flask-RESTPlus is an extension for `Flask` that adds support for quickly building REST APIs. Flask-RESTPlus encourages best practices with minimal setup. If you are familiar with Flask, Flask-RESTPlus should be easy to pick up. It provides a coherent collection of decorators and tools to describe your API and expose its documentation properly using `Swagger`.

2. Vagrant is a tool for building and distributing development environments.Development environments managed by Vagrant can run on local virtualized platforms such as VirtualBox or VMware, in the cloud via AWS or OpenStack, or in containers such as with Docker or raw LXC. Vagrant provides the framework and configuration format to create and manage complete portable development environments. These development environments can live on your computer or in the cloud, and are portable between Windows, Mac OS X, and Linux.

3. SaltStack makes software for complex systems management at scale. SaltStack is the company that created and maintains the Salt Open project and develops and sells SaltStack Enterprise software, services and support. Easy enough to get running in minutes, scalable enough to manage tens of thousands of servers, and fast enough to communicate with them in seconds.

4. Paramiko is a module for Python 2.6+/3.3+ that implements the SSH2 protocol for secure (encrypted and authenticated) connections to remote machines.

5. Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.


Compatibility
=============

Flask-RestPlus requires Python 2.7+ ,Virtual Box or Docker.


Docker Image Setup
==================

Build:

.. code-block:: console

    $ docker-compose build

Run:

With the flask server:

.. code-block:: console

    $ docker-compose -f docker-compose.local.yml up -d --force-recreate

With nginx and gunicorn:

.. code-block:: console

    $ docker-compose up -d --force-recreate


Installation to Run on Local Machine
====================================

Install necessary packages with pip:

.. code-block:: console

    $ pip install -r requirements.txt

Install Vagrant by following instructions:

.. _Vagrant: https://www.vagrantup.com/

Install SaltStack on master:

.. code-block:: console

    $ curl -L https://bootstrap.saltstack.com -o install_salt.sh
    $ sudo sh install_salt.sh -M
    $ salt-key --accept-all

Install SaltStack on minions:

.. code-block:: console

    $ curl -L https://bootstrap.saltstack.com -o install_salt.sh
    $ sudo sh install_salt.sh


Quick start
===========

Clone this repo:

.. code-block:: console

    $ git clone git@github.com:manmohana/Loan-Submission-Form.git

Use the vagrant file from cloned file to create Master and Minions VM:

.. code-block:: console

    $ git clone git@github.com:manmohana/Loan-Submission-Form.git

Install SaltStack as instructed in installation.

Run the app:

.. code-block:: console

    $ export FLASK_APP=app.py	
	$ flask run

	If you are on Windows you need to use set instead of export.

Open browser and got tolocalhost http://localhost:5000/

Post json by following insturctions on Page.
Example json data:

.. code-block:: console
	
	{
	  "command": "sudo salt '*' cmd.run 'sudo apt-get update'",
	  "hostname": "192.168.56.101",
	  "password": "vagrant",
	  "username": "vagrant"
	}


.. image:: https://github.com/amanmohan/automation_master_minions/blob/master/screen_shots/page.png?raw=true
.. image:: https://github.com/amanmohan/automation_master_minions/blob/master/screen_shots/post.png?raw=true
.. image:: https://github.com/amanmohan/automation_master_minions/blob/master/screen_shots/get.png?raw=true


Documentation
=============

For version 1.1 we can add upload feature to add .sls file to get executed on master and to perform changes on minions.

Test cases can be writen for Flask Frame work.
example:
1. post data.
2. getdata.
3. JsonResponse.
4. empty_render.
5. assert400/500.
6. get_server_url.
7. can_ping_server.

Test cases for executing file using paramiko:
1. Error_handling.
2. insuficient_information.
3. incorrect_key.
4. incorrect_command.


