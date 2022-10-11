.. _emulators_spec:

``rh_emulators.json`` specification
===================================

This page details the JSON specification of the emulators file, ``rh_emulators.json``. This file is applied on top of the default emulators specification file, which can be checked `here <https://github.com/retrohub-org/retrohub/blob/main/base_config/emulators.json>`_.

.. warning::
	Always close RetroHub before editing this file, otherwise your changes may be overriden!

.. warning::
	Ensure the file is valid before using it. You can use a JSON validator such as `JSONLint <https://jsonlint.com/>`_.

This JSON consists of an array of dictionary entries. Each entry details a custom emulator or modifications to an existing emulator:

.. code-block:: json

	[
		{
			"name": "retroarch",
			"binpath": "/usr/local/bin/custom-retroarch",
			"corepath": "~/.config/retroarch/cores"
		},
		{
			"name": "dolphin",
			"#delete": true
		},
		{
			"name": "my_custom_Emulator",
			"fullname": "My Custom Emulator",
			"binpath": [
				{
					"windows": [
						"C:/Program Files/My Custom Emulator/MyCustomEmulator.exe"
					]
				},
				{
					"macos": [
						"/Applications/MyCustomEmulator.app/Contents/MacOS/MyCustomEmulator"
					]
				},
				{
					"linux": [
						"/bin/my_custom_emulator"
					]
				}
			],
			"command": "{binpath} \"{rompath}\""
		}
	]

Each entry has specific keys for emulator information, detailed below:

- ``name`` - String **(required)**

Short name for the emulator

.. code-block:: json

	"name": "mupen64plus"

- ``fullname`` - String **(required)**

Emulator name displayed to the user

.. code-block:: json

	"fullname": "Mupen64Plus"

- ``binpath`` - :ref:`Path <emulators_spec_paths>` **(required)**

Path to the emulator executable.

.. code-block:: json

	"binpath": "/usr/bin/mupen64plus"

- ``command``: String **(required)**

Command to run the emulator. It can use some pre-defined variables to fill in information:

	- ``{binpath}`` - Path to the emulator executable
	- ``{rompath}`` - Path to the game file

.. code-block:: json

	"command": "{binpath} --file \"{rompath}\""

.. note::
	Game files may have spaces in the file name. Ensure you surround the ``{rompath}`` variable with quotes ``"`` to avoid such issues.

- ``#delete`` - Boolean *(optional)*

If this key exists, RetroHub will delete this emulator, making it unavailable to the user. Must be combined with a ``name`` key to know which emulator to delete.

.. code-block:: json
	:emphasize-lines: 2

	"name": "mupen64plus",
	"#delete": true

RetroArch configs
-----------------

RetroArch is a more complex emulator that needs more information to properly work:

- ``corepath`` - :ref:`Path <emulators_spec_paths>` **(required)**

Path to the RetroArch cores folder.

.. code-block:: json

	"corepath": "/usr/lib/libretro"

- ``cores`` - Array of Dictionaries **(required)**

Contains the definition of cores as Dictionary entries:

	- ``name`` - String **(required)**

	Short name for the core

	- ``fullname`` - String **(required)**

	Core name displayed to the user

	- ``file`` - :ref:`Path <emulators_spec_paths>` **(required)**

	Core file name

.. code-block:: json

	"cores": [
		{
			"name": "mupen64plus-next",
			"fullname": "Mupen64Plus-Next",
			"file": [
				{
					"windows": "mupen64plus_next_libretro.dll",
					"macos": "mupen64plus_next_libretro.dylib",
					"linux": "mupen64plus_next_libretro.so"
				}
			]
		}
	]

.. _emulators_spec_paths:

Paths
^^^^^

Paths point to files in the user's computer. There are peculiarities to each OS, which RetroHub handles for you. Here are some notes valid for all operating systems:

- Path separators are always ``/``, instead of ``\\``. (e.g ``C:/Program Files/My Emulator/MyEmulator.exe``)
- You can go to the previous folder by typing ``..`` (e.g ``C:/Program Files/../Program Files (x86).``)
- You can use ``~`` to refer to the user's home folder `` (e.g. ``~/Desktop/Emulators/MyEmulator.exe``)
- Absolute paths start with ``/`` on macOS and Linux, and the drive letter (e.g. ``C:/``) on Windows. Otherwise, it's a relative path, which is relative to the RetroHub executable.

Since paths are highly OS dependent, RetroHub uses a special syntax to define them. For example, the ``binpath`` is supposed to be a string, but is defined as a dictionary with keys ``windows``, ``macos`` and ``linux``:

.. code-block:: json

	"name": "mupen64plus",
	"binpath": [
		{
			"windows": [
				"mupen64plus/mupen64plus-ui-console.exe",
				"Emulators/mupen64plus/mupen64plus-ui-console.exe",
				"../mupen64plus/mupen64plus-ui-console.exe"
			]
		},
		{
			"macos": [
				"/Applications/mupen64plus.app/Contents/MacOS/mupen64plus",
				"/usr/local/bin/mupen64plus"
			]
		},
		{
			"linux": [
				"/bin/m64p",
				"/bin/mupen64plus",
				"/usr/bin/m64p",
				"/usr/bin/mupen64plus",
				"/var/lib/flatpak/exports/bin/io.github.m64p.m64p",
				"~/.local/share/flatpak/exports/bin/io.github.m64p.m64p"
			]
		}
	]

RetroHub will search these paths, according to the current OS, and return the first valid one. If no valid one is found, RetroHub will use the first defined path.

For example, on Windows, with the following definition, and with RetroHub finding the emulator on the highlighted line:

.. code-block:: json
	:emphasize-lines: 5

	"binpath": [
		{
			"windows": [
				"C:/Program Files/My Custom Emulator/MyCustomEmulator.exe",
				"C:/Program Files (x86)/My Custom Emulator/MyCustomEmulator.exe",
				"D:/Program Files/My Custom Emulator/MyCustomEmulator.exe",
				"D:/Program Files (x86)/My Custom Emulator/MyCustomEmulator.exe"
			]
		}
	]

It will be converted to:

.. code-block:: json

	"binpath": "C:/Program Files (x86)/My Custom Emulator/MyCustomEmulator.exe"

.. note::
	Currently, it's not possible to set these alternative paths from the application. If you wish to use this feature, you must edit the file manually.