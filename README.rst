Backbone Banter
===============

Setup
-----

.. code-block:: bash

    $ mkvirtualenv banter
    $ git clone git@github.com:lockwooddev/backbone-banter.git
    $ source env/bin/activate
    $ make devinstall


Development settings
--------------------

Create a new file named ``settings.py`` in the ``src/banter`` folder with the
following content.

.. code-block:: python

    from banter.conf.dev_settings import *



Staring the server
------------------

Make sure you have memcached running before running:

   $ python src/manage.py runserver
