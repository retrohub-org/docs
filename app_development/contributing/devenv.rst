.. _app_compiling_godot:

Setting up the development environment
======================================

If you intend to develop for RetroHub, you must first setup the environment and all required dependencies.

.. warning::
	The development version of RetroHub stores configuration on a separate directory from the normal version. This is to prevent modification and corruption to any existing setup. This directory is located at:
	
	- **Windows**: ``C:\Users\<username>\RetroHub-Dev``
	- **macOS**: ``/Users/<username>/.retrohub-dev``
	- **Linux**: ``/home/<username>/.retrohub-dev``

Compiling Godot
---------------

RetroHub requires some functionality not present on the Godot engine yet. While changes are kept to a minimum and are mostly pending code contributions and custom bugfixes, if you try to develop this project with a regular Godot version, you'll encounter errors due to missing functionality.

RetroHub `maintains a custom Godot fork <https://github.com/retrohub-org/godot/tree/retrohub_patches_4x>`_ with custom changes being implemented on the ``retrohub_patches_4x``. To compile it, simply follow the official Godot `compilation instructions <https://docs.godotengine.org/en/stable/development/compiling/index.html>`_.

Obtaining third-party libraries
-------------------------------

Due to some existing third-party dependencies with different licenses, the RetroHub source code only includes dependencies with the same license as ours. For any missing dependencies, you'll need to manually obtain them in order to setup the development environment.

Video playback uses `FFmpeg <https://ffmpeg.org/>`_ for decoding, which is under GPLv3. You will need to compile these dependencies yourself. Check out `retrohub-org/godot-videodecoder <https://github.com/retrohub-org/godot-videodecoder>`_ for instructions on compiling for your system. Once you're done, move the compiled binaries to the appropriate system folder under ``addons/godot-videodecoder``.

.. note::
	You only need to compile binaries for your current system, unless you intend to export for other platforms.

Obtaining default themes
------------------------

The default themes are not included in the source code, and are rather downloaded and packaged on our CI. Therefore, you'll need to obtain at least one theme in order to display any games. You can download official themes directly from their project page:

- `Default Theme <https://github.com/retrohub-org/default-theme/releases>`_
- `EmulationStation Theme Wrapper <https://github.com/retrohub-org/es-theme-wrapper/releases>`_

Then place them at your RetroHub-Dev configuration directory.