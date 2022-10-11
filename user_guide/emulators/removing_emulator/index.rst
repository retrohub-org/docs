.. include:: /global/rh_actions.rst

Removing default emulators
==========================

There are two ways to achieve this:

Application
-----------

.. note::
	This is still not implemented in the app. For now you must follow instructions on the **Manually** section.

Manually
--------

Edit the ``rh_emulators.json`` file in the configuration directory. Add a dictionary entry to the existing array, with the ``name`` field set to the name of the emulator you want to remove, and then add the special ``#delete`` key to it:

.. code-block:: json

	[
		{
			"name": "mupen64plus",
			"#delete": true
		}
	]

For more information, see the :ref:`emulators_spec` section.