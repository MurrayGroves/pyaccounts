========
Register
========

.. data:: registerui(#)

.. note:: The # in the brackets is not meant to be used, readthedocs won't let me do two brackets by themselves.

Use this when you don't have the user's details, it will prompt them to enter their details.

Example:

.. code-block:: python
	registerui()

.. data:: register(user, password)

Use this when you have the user's details.
Variables user and password are strings.

Example:

.. code-block:: python
	user = input("What do you want your username to be?")
	password = input("What do you want your password to be?")
	register(user, password)
	print("Registered")

.. toctree::
   :maxdepth: 2
   login.rst
