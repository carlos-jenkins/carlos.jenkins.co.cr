=======================================
Autodeploy a Github-hosted Pelican blog
=======================================

:date: 2014-09-22T16:44-0600
:author: carlos-jenkins
:category: sysadmin
:tags: pelican, apache
:slug: autodeploy-a-github-hosted-pelican-blog

.. contents::
    :backlinks: none


If you have a `Pelican <http://blog.getpelican.com/>`_ blog or static site and
you version control it using `Github <https://github.com/>`_, this tutorial
shows you how to auto deploy it to your web server each time you ``push`` your
repository using `webhooks <https://developer.github.com/webhooks/>`_.

I will assume the following:

- You have installed Apache in Ubuntu 14.04.
- You Apache user is Ubuntu's default ``www-data`` and it's home is
  ``/var/www/``.
- You have a Virtual Host for your site ``my.site.com``.
- The configuration file for that virtual host is
  ``/etc/apache2/sites-available/my.site.com.conf``
- It's ``DocumentRoot`` is ``/var/www/site.com/my/htdocs/``.
- Apache has write permissions to ``/var/www/site.com/my/`` and children.
- You have installed ``git``, ``pelican`` and all other dependencies your
  site requires.
- Your project repository is called ``my.site.com``.


Steps
=====

Create SSH directory
--------------------

.. code:: bash

   sudo mkdir /var/www/.ssh
   sudo chown -R www-data:www-data /var/www/.ssh/


Create SSH key
--------------

.. code:: bash

   sudo -H -u www-data ssh-keygen -t rsa

Note: Leave default name and empty password.


Add SSH key to your Github account
----------------------------------

.. code:: bash

   cat /var/www/.ssh/id_rsa.pub

Copy, then go to, and paste:

    https://github.com/settings/ssh


Clone website repository
------------------------

.. code:: bash

   cd /var/www/site.com/my/
   sudo -H -u www-data git clone --recursive git@github.com:you/my.site.com.git


Clone ``python-github-webhooks``
--------------------------------

`python-github-webhooks <https://github.com/carlos-jenkins/python-github-webhooks>`_
will allow you to script the built of your site when you push it.

.. code:: bash

   cd /var/www/site.com/my/
   sudo -H -u www-data git clone git@github.com:carlos-jenkins/python-github-webhooks.git

Install ``python-github-webhooks`` dependencies:

.. code:: bash

   sudo apt-get install python-pip
   cd /var/www/site.com/my/python-github-webhooks
   sudo pip install -r requirements.txt


Configure Apache for Github webhooks
------------------------------------

Install and enable WSGI support in Apache:

.. code:: bash

   sudo apt-get install libapache2-mod-wsgi

Edit your virtual host file to look something like this:

.. code:: apache

   <VirtualHost *:80>
       ServerAdmin you@my.site.com
       ServerName  my.site.com
       DocumentRoot /var/www/site.com/my/htdocs/

       # Handle Github webhook
       <Directory "/var/www/site.com/my/python-github-webhooks">
           Order deny,allow
           Allow from all
       </Directory>
       WSGIScriptAlias /webhooks /var/www/site.com/my/python-github-webhooks/webhooks.py

   </VirtualHost>

Do not forget to restart Apache:

.. code:: bash

   sudo service apache2 restart


Add webhook to your Github repository
-------------------------------------

Go to your Github repository settings:

    https://github.com/youruser/my.site.com/settings/hooks

And add a Webhook to the WSGI script URL:

::

   http://my.site.com/webhooks


Create custom build script
--------------------------

.. code:: bash

   cd /var/www/site.com/my/python-github-webhooks/hooks
   sudo -u www-data touch push-my.site.com-master
   sudo chmod +x push-my.site.com-master
   sudo nano push-my.site.com-master

And add the following:

.. code:: bash

   #!/usr/bin/env bash

   set -e
   set -u

   PATH=/usr/local/bin:/usr/bin:/bin

   cd /var/www/site.com/my/my.site.com
   git pull origin master
   git submodule foreach git pull origin master
   cp -rf output/* ../htdocs/


Test you hook
-------------

You can test a hook for your repo as explained in
`Test a push hook <https://developer.github.com/v3/repos/hooks/#test-a-push-hook>`_
like so:

.. code:: bash

   curl --user "youruser" https://api.github.com/repos/youruser/my.site.com/hooks

Toke note of the ``"test_url"``.

.. code:: bash

   curl --user "youruser" -i -X POST [TEST_URL]


Credits
=======

Thanks to:

- https://gist.github.com/oodavid/1809044
- https://github.com/datafolklabs/github-webhook-wrapper
- https://gist.github.com/caspyin/2288960
