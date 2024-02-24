.. include:: /global/rh_actions.rst

Changing system settings
========================

There are two ways to achieve this:

Application
-----------

Open the **Settings** (|action: rh_menu|) panel, and navigate to the **Systems** section.

.. image:: ../adding_system/assets/system_section.png

Then modify these fields to your liking. Remember to save changes when you're done.

You can also revert to the default settings by clicking the **Restore default system** button.

Manually
--------

Edit the ``rh_systems.json`` file in the configuration directory. Add a dictionary entry to the existing array, with the ``name`` field set to the name of the system you want to modify, and then changing the other key values:

.. code-block:: json

	[
		{
			"name": "n64",
			"fullname": "Nintendo 64 (Custom Name)",
			"extension": [
				".abc",
				".rom"
			]
			"category": "computer"
		}
	]

For more information on the existing keys and their values, see the :ref:`systems_spec` section.