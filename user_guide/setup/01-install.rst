Download
========

RetroHub can be downloaded from `GitHub releases <https://github.com/retrohub-org/retrohub/releases>`_. The current latest release is `v0.1.2-beta <https://github.com/retrohub-org/retrohub/releases/tag/v0.1.2-beta>`_.

RetroHub is available for **Windows**, **macOS** and **Linux**.

Installing
~~~~~~~~~~

Windows
-------

Windows releases work like portable applications. Extract to a folder of your choice and run the main ``RetroHub.exe`` executable.

macOS
-----

macOS releases work as an app bundle. Run the downloaded ``Retrohub.App``.

.. warning::
	RetroHub is signed, but not notarized, so you need to enable apps from untrusted sources in your `Secrity & Privacy settings <https://support.apple.com/en-us/HT202491>`_. For more information on what to do on specific scenarios, check `this page <https://docs.godotengine.org/en/3.5/tutorials/export/running_on_macos.html>`_.

Linux
-----

Linux releases work like portable applications. Extract to a folder of your choice and run the main ``RetroHub`` executable.


.. warning::
	When downloading automatic builds from GitHub's CI, you need to mark the app as executable. This is specially relevant for macOS, as not doing so will throw a generic ``This app can't be opened`` error. To do so, open a terminal and run:

	* macOS: ``chmod +x RetroHub.App/Contents/MacOS/RetroHub``
	* Linux: ``chmod +x RetroHub``