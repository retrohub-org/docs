.. include:: /global/godot_api.rst

.. _api_FileUtils:

FileUtils
=========

This is a helper class to handle file operations in a platform agnostic way.

Enumerations
------------

.. _api_FileUtils_OS_ID:

enum **OS_ID**:

- **WINDOWS** - Windows or UWP
- **MACOS** - macOS
- **LINUX** - Unix systems (Linux, BSD, etc.)
- **UNSUPPORTED** - Any other system currently not supported

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_string|
	  - :ref:`test_for_valid_path <api_FileUtils_test_for_valid_path>`
	* - void
	  - :ref:`ensure_path <api_FileUtils_ensure_path>`
	* - |godot_string|
	  - :ref:`expand_path <api_FileUtils_expand_path>`
	* - |godot_int|
	  - :ref:`get_space_left <api_FileUtils_get_space_left>`
	* - |godot_string|
	  - :ref:`get_folder_size <api_FileUtils_get_folder_size>`
	* - |godot_int|
	  - :ref:`get_file_count <api_FileUtils_get_file_count>`
	* - |godot_int|
	  - :ref:`get_home_dir <api_FileUtils_get_home_dir>`
	* - :ref:`OS_ID <api_FileUtils_OS_ID>`
	  - :ref:`get_os_id <api_FileUtils_get_os_id>`
	* - |godot_string|
	  - :ref:`get_os_string <api_FileUtils_get_os_string>`
	* - |godot_bool|
	  - :ref:`is_steam_deck <api_FileUtils_is_steam_deck>`

----

.. _api_FileUtils_test_for_valid_path:

	|godot_string| **test_for_valid_path** (paths: |godot_string| \| |godot_array|)

Tests whether the supplied path(s) exist in the user's system. If ``paths`` is a |godot_string|, tests if it exists. Otherwise, if it is a |godot_array|, tests for all strings inside and returns the first valid one. Returns ``""`` if no valid path is found.

----

.. _api_FileUtils_ensure_path:

	void **ensure_path** (path: |godot_string|)

Recursively creates the directory structure of the specified path, ensuring all subfolders exist

.. code-block:: gdscript

	# Creates the directory structure "very/long/folder" if necessary
	FileUtils.ensure_path("very/long/folder/my_file.txt")
	var file = File.open("very/long/folder/my_file.txt", File.WRITE)
	...

----

.. _api_FileUtils_expand_path:

	|godot_string| **expand_path** (path: |godot_string|)

Expand paths with embedded variables. Supported variables are:

- ``~`` - User's home directory

.. code-block:: gdscript

	# Returns C:/Users/<username>/Documents on Windows
	FileUtils.expand_path("~/Documents")

----

.. _api_FileUtils_get_space_left:

	|godot_int| **get_space_left** ()

Returns the amount of free space, in bytes, of the disk that contains RetroHub's config directory.

----

.. _api_FileUtils_get_folder_size:

	|godot_string| **get_folder_size** (path: |godot_string|, filter_folders: |godot_array| = ``[]``)

Returns the total size of the specified folder, in bytes. If ``filter_folders`` is specified, it will not count the size of any folder that matches any of the strings in the array.

----

.. _api_FileUtils_get_file_count:

	|godot_int| **get_file_count** (path: |godot_string|, filter_folders: |godot_array| = ``[]``)

Returns the total number of files in the specified folder. If ``filter_folders`` is specified, it will not count any files inside a folder that matches any of the strings in the array.

----

.. _api_FileUtils_get_home_dir:

	|godot_string| **get_home_dir** ()

Returns the user's home directory.

----

.. _api_FileUtils_get_os_id:

	:ref:`OS_ID <api_FileUtils_OS_ID>` **get_os_id** ()

Returns the current operating system as an :ref:`OS_ID <api_FileUtils_OS_ID>`.

----

.. _api_FileUtils_get_os_string:

	|godot_string| **get_os_string** ()

Returns the current operating system as a string. Possible values are ``"windows"``, ``"macos"``, ``"linux"``, and ``"null"``.

----

.. _api_FileUtils_is_steam_deck:

	|godot_bool| **is_steam_deck** ()

Returns ``true`` if the current system is a Steam Deck.