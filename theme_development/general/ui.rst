.. _theme_section_ui:

User Interface
==============

This section shows some existing user interfaces from RetroHub that themes can use. All of these are accessible through the ``RetroHubUI`` singleton.

Default Colors
--------------

There are some default colors you can use for some scenarios:

- Success - ``RetroHubUI.color_success``
- Warning - ``RetroHubUI.color_warning``
- Error - ``RetroHubUI.color_error``
- Pending - ``RetroHubUI.color_pending``
- Unavailable - ``RetroHubUI.color_unavailable``

File/Directory Picker
---------------------

If you need to pick a file or directory to load, you can request that through the existing interface for that. This also ensures proper controller support in this scenario.

.. code-block:: gdscript

	# Example to load a single PNG file
	RetroHubUI.filesystem_filters(["*.png ; PNG Images"])
	RetroHubUI.request_file_load(FileUtils.get_home_dir())
	var path : String = yield(RetroHubUI, "path_selected")
		if not path.empty():
			print("File selected: " + path)
		else:
			print("No file selected")

For more information check the :ref:`api_RetroHubUI` class reference.

App Icons
---------

You can access the default icons that are shipped with RetroHub. All the icons available are in the ``RetroHubUI.Icons`` enum.

.. code-block:: gdscript

	# Example to load the default icon for loading files
	var icon : Texture = RetroHubUI.load_app_icon(RetroHubUI.Icons.LOAD)

Virtual Keyboard
----------------

RetroHub will show a virtual keyboard automatically if a ``LineEdit`` or ``TextEdit`` node is focused from a controller and/or mouse input. If you need to, you can also manually trigger the virtual keyboard to show up with ``RetroHubUI.show_virtual_keyboard()``.

You need to have the required node be currently focused and accept raw key events for this to properly work. For more information check the :ref:`api_RetroHubUI` class reference.
