.. include:: /global/godot_api.rst

.. _api_RetroHubUI:

RetroHubUI
==========

This class exposes some UI actions and data for themes.

Constants
---------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_color|
	  - :ref:`color_theme_accent <api_RetroHubUI_color_theme_accent>`
	* - |godot_color|
	  - :ref:`color_success <api_RetroHubUI_color_success>`
	* - |godot_color|
	  - :ref:`color_warning <api_RetroHubUI_color_warning>`
	* - |godot_color|
	  - :ref:`color_error <api_RetroHubUI_color_error>`
	* - |godot_color|
	  - :ref:`color_pending <api_RetroHubUI_color_pending>`
	* - |godot_color|
	  - :ref:`color_unavailable <api_RetroHubUI_color_unavailable>`
	* - |godot_int|
	  - :ref:`max_popupmenu_height <api_RetroHubUI_max_popupmenu_height>`

----

.. _api_RetroHubUI_color_theme_accent:

	|godot_color| **color_theme_accent**

Color used for "accent" elements on RetroHub's interface.

----

.. _api_RetroHubUI_color_success:

	|godot_color| **color_success**

Color used for success messages.

----

.. _api_RetroHubUI_color_warning:

	|godot_color| **color_warning**

Color used for warning messages.

----

.. _api_RetroHubUI_color_error:

	|godot_color| **color_error**

Color used for error messages.

----

.. _api_RetroHubUI_color_pending:

	|godot_color| **color_pending**

Color used for pending operations.

----

.. _api_RetroHubUI_color_unavailable:

	|godot_color| **color_unavailable**

Color used for unavailable objects.

----

.. _api_RetroHubUI_max_popupmenu_height:

	|godot_int| **max_popupmenu_height**

Maximum size, in pixels, for |godot_popupmenu| elements. Use this value in your themes to have consistent sizes with RetroHub's defaults.

Enumerations
------------

.. _api_RetroHubUI_Icons:

enum **Icons**:

- **DOWNLOADING** - Downloading icon.
- **ERROR** - Error icon.
- **FAILURE** - Failure icon.
- **IMAGE_DOWNLOADING** - Image downloading icon.
- **LOAD** - Load file/directory icon.
- **LOADING** - Loading icon.
- **SUCCESS** - Success icon.
- **VISIBILITY_HIDDEN** - Hidden visibility icon.
- **VISIBILITY_VISIBLE** - Visible visibility icon.
- **WARNING** - Warning icon.

----

.. _api_RetroHubUI_ConfigTabs:

enum **ConfigTabs**:

- **QUIT** - Quit tab.
- **GAME** - Game metadata editor tab.
- **SCRAPER** - Scraper tab.
- **THEME** - Theme settings tab.
- **SETTINGS_GENERAL** - General settings tab.
- **SETTINGS_INPUT** - Input settings tab.
- **SETTINGS_REGION** - Region settings tab.
- **SETTINGS_SYSTEMS** - Systems settings tab.
- **SETTINGS_EMULATORS** - Emulators settings tab.
- **SETTINGS_ABOUT** - About tab.

Signals
-------

.. _api_RetroHubUI_path_selected:

	**path_selected** (file: |godot_string|)

Emitted when a path is selected in the file/directory dialog. Used for :ref:`request_file_load <api_RetroHubUI_request_file_load>`/:ref:`request_folder_load <api_RetroHubUI_request_folder_load>`. ``file`` is the path selected, or ``""`` if nothing was selected.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - void
	  - :ref:`filesystem_filters <api_RetroHubUI_filesystem_filters>`
	* - void
	  - :ref:`request_file_load <api_RetroHubUI_request_file_load>`
	* - void
	  - :ref:`request_folder_load <api_RetroHubUI_request_folder_load>`
	* - |godot_texture|
	  - :ref:`load_app_icon <api_RetroHubUI_load_app_icon>`
	* - void
	  - :ref:`show_virtual_keyboard <api_RetroHubUI_show_virtual_keyboard>`
	* - |godot_bool|
	  - :ref:`is_virtual_keyboard_visible <api_RetroHubUI_is_virtual_keyboard_visible>`
	* - |godot_bool|
	  - :ref:`is_event_from_virtual_keyboard <api_RetroHubUI_is_event_from_virtual_keyboard>`
	* - void
	  - :ref:`hide_virtual_keyboard <api_RetroHubUI_hide_virtual_keyboard>`
	* - void
	  - :ref:`open_app_config <api_RetroHubUI_open_app_config>`
	* - void
	  - :ref:`show_warning <api_RetroHubUI_show_warning>`

----

.. _api_RetroHubUI_filesystem_filters:

	void **filesystem_filters** (filters: |godot_array|)

Set file filters for the file/directory dialog. Works exactly the same as Godot's `FileDialog.filters <https://docs.godotengine.org/en/3.5/classes/class_filedialog.html#class-filedialog-property-filters>`_.

.. code-block:: gdscript

	# Only show supported image files
	filesystem_filters([["*.png, *.jpg, *.jpeg ; Supported Images"]])

----

.. _api_RetroHubUI_request_file_load:

	void **request_file_load** (base_path: |godot_string|)

Request a file load. The file dialog will be opened and the user will be able to select a file. ``base_path`` indicates what folder path to start on initially. Call :ref:`filesystem_filters <api_RetroHubUI_filesystem_filters>` before to set desired file filters.

When a file is selected, the :ref:`path_selected <api_RetroHubUI_path_selected>` signal will be emitted with the path to the file. If the user cancels the dialog, the signal will be emitted with an empty string.

.. code-block:: gdscript

	# Example to load a single PNG file
	RetroHubUI.filesystem_filters(["*.png ; PNG Images"])
	RetroHubUI.request_file_load(FileUtils.get_home_dir())
	var path : String = yield(RetroHubUI, "path_selected")
		if not path.empty():
			print("File selected: " + path)
		else:
			print("No file selected")

----

.. _api_RetroHubUI_request_folder_load:

	void **request_folder_load** (base_path: |godot_string|)

Request a folder load. The file dialog will be opened and the user will be able to select a folder. ``base_path`` indicates what folder path to start on initially.

When a folder is selected the :ref:`path_selected <api_RetroHubUI_path_selected>` signal will be emitted with the path to the folder. If the user cancels the dialog, the signal will be emitted with an empty string.

.. code-block:: gdscript

	# Example to load a folder
	RetroHubUI.request_folder_load(FileUtils.get_home_dir())
	var path : String = yield(RetroHubUI, "path_selected")
		if not path.empty():
			print("Folder selected: " + path)
		else:
			print("No folder selected")

----

.. _api_RetroHubUI_load_app_icon:

	|godot_texture| **load_app_icon** (icon: :ref:`Icons <api_RetroHubUI_Icons>`)

Load an app-default icon.

----

.. _api_RetroHubUI_show_virtual_keyboard:

	void **show_virtual_keyboard** ()

Asks RetroHub to show the virtual keyboard. The node you want to receive key events must be focused (`Control.grab_focus() <https://docs.godotengine.org/en/3.5/classes/class_control.html#class-control-method-grab-focus>`_) before calling this method. The virtual keyboard will then send raw `InputEventKey <https://docs.godotengine.org/en/3.5/classes/class_inputeventkey.html>`_ events to the focused node.

.. note::
	RetroHub automatically opens the virtual keyboard for |godot_lineedit| and |godot_textedit| nodes. This method is only needed if you want to show the virtual keyboard for other nodes.

----

.. _api_RetroHubUI_is_virtual_keyboard_visible:

	|godot_bool| **is_virtual_keyboard_visible** ()

Returns ``true`` if the virtual keyboard is currently visible.

----

.. _api_RetroHubUI_is_event_from_virtual_keyboard:

	|godot_bool| **is_event_from_virtual_keyboard** ()

Returns ``true`` if the current input event is coming from the virtual keyboard.

.. code-block:: gdscript

	func _input(event):
		if RetroHubUI.is_event_from_virtual_keyboard():
			# From virtual keyboard
			...
		else:
			# From actual user input
			...

----

.. _api_RetroHubUI_hide_virtual_keyboard:

	void **hide_virtual_keyboard** ()

Hides the virtual keyboard.

----

.. _api_RetroHubUI_open_app_config:

	void **open_app_config** (tab : :ref:`ConfigTabs <api_RetroHubUI_ConfigTabs>` = ``-1``)

Opens RetroHub's app configuration UI. If ``-1`` is specified, the app will stay on the currently selected tab.

.. warning::
	Opening the app configuration UI will steal focus from the theme until the user closes it.

----

.. _api_RetroHubUI_show_warning:

	void **show_warning** (text: |godot_string|)

Shows a warning to the user. Use this for warnings that are at the application level, and not specific to your theme.