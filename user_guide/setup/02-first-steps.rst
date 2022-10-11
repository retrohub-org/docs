First Steps
===========

The first time you launch RetroHub, you'll be presented with a first-time wizard setup. This setup will bootstrap your retro gaming library and set some default settings. Each section is described in more detail below.

Region
^^^^^^

Region is used to set up some cosmetic settings used throughout the app. You can choose a region to use a preset of settings, or customize each type of setting:

- **Rating System:** Age rating system to use:
	- **ESRB**
	- **PEGI**
	- **CERO**
- **Date Format:** Format to present date & time
- **System Names:** Names to use for consoles with region-specific names

Import Settings
^^^^^^^^^^^^^^^

If you have a current setup on another frontend, RetroHub may be able to automatically import it. It will scan your files and show any valid apps found for you to import, as well as what kind of information it can import and any drawbacks:

- **Game metadata:** - Game "text" information, such as names, descriptions, publishers, release dates, etc...
- **Game media:** - Game "visual" media, such as screenshots, videos, box arts, etc...
- **Themes:** Application themes. RetroHub may be able to load these themes under a wrapper.

If you don't wish to import, you can also skip this step by picking ``Don't Import Settings``.

If you pick an app to import, you'll be asked whether you want to move or copy the media files *(game metadata files are always copied)*:

- **Moving** doesn't duplicate files, saving you disk space. However it make the original app lose information, requiring you to regenerate or recreate game information if you still wish to use it.
- **Copying** doesn't change any original files, leaving the original app untouched. However it will consume more disk space, which can be a problem with very large libraries. RetroHub shows an estimate of you much that would take, but always ensure you have plenty of space before proceeding.

After one of these options, RetroHub will begin importing the files. This step may take some time.

Games
^^^^^

.. note::
	If you imported settings in the previous place, the game path may already be filled to your existing library. If you choose a different path from what was picked, remember to move your games to the new location.

Here you should pick a folder for storing your games. This can either be empty or already where you store your games.

This folder will have a defined structure to organize your games. RetroHub uses the same structure and names from EmulationStation (DE): your library consists of folders with short system names, and all games are inside each folder:

.. code-block::

	games
	├── c64
	│   ├── game1.bin
	│   └── game2.d64
	├── gc
	│   ├── game1.iso
	│   └── game2.iso
	├── snes
	│   ├── game1.sfc
	│   └── game2.sfc
	└── ...

The system short names available can be checked at :doc:`/user_guide/systems/index`. The next section also allows you to bootstrap some or all system folders.

Each system as a set of file extensions associated, so RetroHub doesn't pick irrelevant files. These can be configured per system later on.

Systems
^^^^^^^

Here you'll find a list of all the systems RetroHub supports by default. These are separated by category, so you can add only a specific kind of system to your library.

Pick any systems you want to support, and RetroHub will create folders for it in the games library.

If the game library already has some valid files, that system can not be deselected. RetroHub treats your game library as read-only, so it can't delete any files. If you wish to remove a system, you'll need to manually remove the files in there.

You can add/remove systems later from configuration as well.

Emulators
^^^^^^^^^

This section searchs for emulators in your system, and gives you an overall idea of what systems are expected to already work out-of-the-box.

While RetroHub ships with many defaults to use most popular emulators per system, it does not ship with emulators. You will have to download and configure these yourself.

All done
^^^^^^^^

After this setup, your retro gaming library is configured! RetroHub loads a default theme for you to start straightaway, but if you want to customize the look and feel of the app, move on to the next section for learning how to download, install and use custom themes.