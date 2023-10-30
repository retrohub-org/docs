.. _app_contributing_data:

Adding systems and emulators
============================

RetroHub is a community project, and we welcome contributions to systems and emulators! If your favorite system or emulator is not yet supported by default, you can help us by adding it to the project.

The `Emulation General Wiki <https://emulation.gametechwiki.com/index.php/Main_Page>`_ is a fantastic resource for finding information about systems and emulators, and we recommend it as a reference in order to help your research when contributing information.

.. warning::

	Be wary of the license of any assets you use: only assets under free/open licenses will be accepted.

Contributing a new system
-------------------------

A system is a particular piece of hardware that can run a specific range of games released for it. Currently, RetroHub distinguishes systems as computers, game engines, and consoles. Here are a few design choices that can help you understand what we're looking for in RetroHub:

- RetroHub is a "retrogaming library frontend", and therefore there's no point in adding artificial system or categories that fall outside of this goal, like audio and video software.
- A system should be something that's usually not straigthforward for the user to just run, meaning they need to open an emulator or some other software in order to play. Games that can be directly launched break RetroHub's philosophy. This implicitly means PC games and storefront like Steam, Epic, GOG and etc. are not accepted.
- A system **needs** to have some emulator associated with it. Systems without or with very poor emulation are not accepted.

Systems are defined in ``base_config/systems.json``. It consists of an array of dictionaries, each one defining a new system:

.. code-block:: json

	{
		"name": "amstradcpc",
		"fullname": "Amstrad CPC",
		"category": "computer",
		"extension": [
			".cdt",
			".cpr",
			".cpc",
			".dsk",
			".kcr",
			".m3u",
			".sna",
			".tap",
			".voc",
			".zip"
		],
		"platform": "amstradcpc",
		"emulator": [
			{
				"retroarch": [
					"caprice32",
					"crocods",
					"mame"
				]
			},
			"caprice32",
			"mame"
		]
	}

The specification for systems is the same as the end-user configuration, so check the :ref:`systems_spec` in order to understand each required field.

A new system will require two assets: a picture of the system (prefereably a drawing of it, and not a photo), and it's commercial logo. Both assets should be placed in ``assets/systems/``, and be named ``<system_name>_photo.png`` and ``<system_name>_logo.png`` respectively.

Contributing a new emulator
---------------------------

An emulator is some software that RetroHub will launch in order to run games of a given system. The emulator must provide some CLI interface in order for RetroHub to launch it directly. Additionally, here's some guidelines for adding emulators:

- It's prefereable to choose emulators that are cross-platform and/or open-source.
- The emulator must have a reasonable degree of compatibility with the given system.
- The emulator must be able to run games directly, without requiring further user input.
- The emulator must be relatively popular and active, and prefereably marked as recommended on the `Emulation General Wiki <https://emulation.gametechwiki.com/index.php/Main_Page>`_.

Emulators are defined in ``base_config/emulators.json``. It consists of an array of dictionaries, each one defining a new emulator:

.. code-block:: json

	{
		"name": "cemu",
		"fullname": "Cemu",
		"binpath": [
			{
				"windows": [
					"Emulators/cemu/Cemu.exe"
				]
			},
			{
				"macos": [
					"/Applications/Cemu.app/Contents/MacOS/Cemu"
				]
			},
			{
				"linux": [
					"/bin/cemu",
					"/usr/bin/cemu"
				]
			}
		],
		"command": "{binpath} -g \"{rompath}\" -f"
	},

The specification for emulators is the same as the end-user configuration, so check the :ref:`emulators_spec` in order to understand each required field.

A new emulator will require an icon to represent it. Place this under ``assets/emulators/``, and name it ``<emulator_name>.png``.