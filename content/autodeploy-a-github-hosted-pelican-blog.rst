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


Clone ``github-webhook-wrapper``
--------------------------------

`github-webhook-wrapper <https://github.com/datafolklabs/github-webhook-wrapper>`_
will allow you to script the built of your site when you push it.

.. code:: bash

   cd /var/www/site.com/my/
   sudo -H -u www-data git clone git@github.com:datafolklabs/github-webhook-wrapper.git


Configure Apache for Github webhooks
------------------------------------

Enable CGI scripts in Apache:

.. code:: bash

   sudo a2enmod cgi

Edit your virtual host file to look something like this:

.. code:: apache

   <VirtualHost *:80>
       ServerAdmin you@my.site.com
       ServerName  my.site.com
       DocumentRoot /var/www/site.com/my/htdocs/

       # Handle Github webhook
       <Directory "/var/www/site.com/my/github-webhook-wrapper">
           Options +ExecCGI
           AddHandler cgi-script .cgi
       </Directory>
       Alias /da7496d7111749982285d1e2aa8bba0b0b2edd9a /var/www/site.com/my/github-webhook-wrapper

   </VirtualHost>

**Note:** The hash is just and arbitrary hash to avoid abuse of the service.
It can be anything, or generated with ``date +%s | sha1sum``.

Do not forget to restart Apache:

.. code:: bash

   sudo service apache restart


Add webhook to your Github repository
-------------------------------------

Go to your Github repository settings:

    https://github.com/carlos-jenkins/my.site.com/settings/hooks

And add a Webhook to your CGI script URL you just configure:

::

   http://my.site.com/da7496d7111749982285d1e2aa8bba0b0b2edd9a/hook.cgi


Create custom build script
--------------------------

.. code:: bash

   cd /var/www/site.com/my/github-webhook-wrapper/scripts
   sudo -u www-data touch my.site.com
   sudo chmod +x my.site.com
   sudo nano my.site.com

And add the following:

.. code:: bash

   #!/usr/bin/env bash

   set -e
   set -u

   PATH=/usr/local/bin:/usr/bin:/bin

   cd /var/www/site.com/my/my.site.com
   git pull origin master
   git submodule foreach git pull origin master
   cp -rf plugins/* ../htdocs/



Credits
=======

Thanks to:

- https://gist.github.com/oodavid/1809044
- https://github.com/datafolklabs/github-webhook-wrapper
