.. include:: /global/rh_actions.rst

Removing default systems
========================

To remove a default system, you can remove or rename that system's folder in your gaming library. However, if you do not want to do that, you can also "hide" it from the app instead.

There are two ways to achieve this:

Application
-----------

.. note::
	This is still not implemented in the app. For now you must follow instructions on the **Manually** section.

Manually
--------

Edit the ``rh_systems.json`` file in the configuration directory. Add a dictionary entry to the existing array, with the ``name`` field set to the name of the system you want to remove, and then add the special ``#delete`` key to it:

.. code-block:: json

	[
		{
			"name": "n64",
			"#delete": true
		}
	]

For more information, see the :ref:`systems_spec` section.