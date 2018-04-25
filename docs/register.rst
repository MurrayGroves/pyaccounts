========
Register
========

.. data:: registerui(#)

.. note:: The # in the brackets is not meant to be used, readthedocs won't let me do two brackets by themselves.

Use this when you don't have the details the user wants to sign up with.

.. code-block:: python
	
	from pyaccounts import register
	registerui()
  
.. data:: register(username, password)
Use this when you have the details the user wants to sign up with.
Variables username and password are strings.

.. code-block:: python
    
	from pyaccounts import register
	username = input("What do you want your username to be?")
	password = input("What do you want your password to be?")
	register(username, password)

.. toctree::
   :maxdepth: 2
   login.rst
