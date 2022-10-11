.. _systems_spec:

``rh_systems.json`` specification
=================================

This page details the JSON specification of the systems file, ``rh_systems.json``. This file is applied on top of the default systems specification file, which can be checked `here <https://github.com/retrohub-org/retrohub/blob/main/base_config/systems.json>`_.

.. warning::
	Always close RetroHub before editing this file, otherwise your changes may be overriden!

.. warning::
	Ensure the file is valid before using it. You can use a JSON validator such as `JSONLint <https://jsonlint.com/>`_.

This JSON consists of an array of dictionary entries. Each entry details a custom system or modifications to an existing system:

.. code-block:: json

	[
		{
			"name": "psx",
			"extension": [
				".bin",
				".cue"
			]
		},
		{
			"name": "amiga",
			"#delete": true
		},
		{
			"name": "my_custom_system",
			"platform": "my_custom_system",
			"fullname": "My Custom System",
			"extends": "ps4",
			"extension": [
				".abc",
				".rom"
			],
			"emulator": [
				"my_custom_emulator",
				{
					"retroarch": [
						"my_custom_core"
					]
				}
			],
			"category": "console"
		}
	]

Each entry has specific keys for system information, detailed below:

- ``name`` - String **(required)**

Short name for the system

.. code-block:: json

	"name": "n64"

- ``platform`` - String **(required)**

To what platform this system belongs, if applicable. This is for systems that are functionally the same (such as using the same emulators), but are different enough to be displayed separately for users *(for example, Nintendo 64 DD on Nintendo 64, or Sega Genesis CD on Sega Genesis)*.

If this isn't the case, set it to the same value as ``name``.

.. code-block:: json
	:emphasize-lines: 2

	"name": "n64dd",
	"platform": "n64"

- ``fullname`` - String **(required)**

System name displayed to the user

.. code-block:: json

	"fullname": "Nintendo 64"

- ``extension`` - Array **(required)**

Accepted file extensions. These are case insensitive, so ``.bin`` and ``.BIN`` are the same, for example.

.. code-block:: json

	"extension": [
		".n64",
		".v64",
		".z64",
		".zip"
	]

- ``emulator`` - Array **(required)**

Valid emulators to use for this system. It is composed of either:

	- A String for simple emulators

	.. code-block:: json

		"emulator": [
			"mupen64plus"
		]

	- A Dictionary for complex emulators:
		- RetroArch (key ``retroarch``): array of strings of accepted libretro cores

		.. code-block:: json

			"emulator": [
				{
					"retroarch": [
						"mupen64plus",
						"parallel_n64"
					]
				}
			]

- ``category`` - String **(required)**

System category. Must be ``console``, ``computer``, ``arcade`` or ``modern_console``

.. code-block:: json

	"category": "console"

- ``extends`` - String *(optional)*

Copies the configuration of an existing system. With this, you can omit all the other keys (except ``name``) as they will be copied from the system you are extending. You can still specify keys, which will override the copied values.

.. code-block:: json
	:emphasize-lines: 3

	"name": "n64dd",
	"fullname": "Nintendo 64 DD",
	"extends": "n64"

- ``#delete`` - Boolean *(optional)*

If this key exists, RetroHub will delete this system, making it unavailable to the user. Must be combined with a ``name`` key to know which system to delete.

.. code-block:: json
	:emphasize-lines: 2

	"name": "n64dd",
	"#delete": true