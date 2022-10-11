.. include:: /global/godot_api.rst

.. _api_JSONUtils:

JSONUtils
=========

This is a helper class to facilitate usage of JSON files.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_dictionary|
	  - :ref:`load_json_file <api_JSONUtils_load_json_file>`
	* - void
	  - :ref:`save_json_file <api_JSONUtils_save_json_file>`
	* - void
	  - :ref:`make_system_specific <api_JSONUtils_make_system_specific>`
	* - |godot_dictionary|
	  - :ref:`map_array_by_key <api_JSONUtils_map_array_by_key>`
	* - |godot_string|
	  - :ref:`format_string_with_substitutes <api_JSONUtils_format_string_with_substitutes>`

----

.. _api_JSONUtils_load_json_file:

	|godot_dictionary| **load_json_file** (filepath: |godot_string|)

Loads a JSON file and returns it as a dictionary. If the file does not exist or is invalid, an empty dictionary is returned.

----

.. _api_JSONUtils_save_json_file:

	void **save_json_file** (json: |godot_dictionary|, file_path: |godot_string|)

Saves a dictionary as a JSON file to ``file_path``.

----

.. _api_JSONUtils_make_system_specific:

	void **make_system_specific** (json: |godot_dictionary|, curr_system: |godot_string|)

Edits a dictionary in-place to remove variable :ref:`Paths <emulators_spec_paths>`, taking into account the current system. Used internally to load configurations dependent on the current system.

.. code-block:: gdscript

	var data = {
		"foo": "bar",
		"path": {
			"windows": [
				"C:\\foo\\bar",
				"C:\\foo\\bar2"
			],
			"macos": "/Applications/foo/bar",
			"linux": "/bin/foo/bar"
		}
	}

	JSONUtils.make_system_specific(data, "windows")
	# Returns {"foo": "bar", "path": ["C:\\foo\\bar", "C:\\foo\\bar2"]}

----

.. _api_JSONUtils_map_array_by_key:

	|godot_dictionary| **map_array_by_key** (input: |godot_array|, key: |godot_string|)

Given an array of dictionaries with a given key, returns a dictionary mapped by the key's value.

.. code-block:: gdscript

	var data = [
		{"id": "foo", "name": "Foo"},
		{"id": "bar", "name": "Bar"}
	]

	JSONUtils.map_array_by_key(data, "id")
	# Returns {"foo": {"id": "foo", "name": "Foo"}, "bar": {"id": "bar", "name": "Bar"}}

----

.. _api_JSONUtils_format_string_with_substitutes:

	|godot_string| **format_string_with_substitutes** (raw_str: |godot_string|, substitutes: |godot_dictionary|, tk_start: |godot_string| = ``"{"``, tk_end: |godot_string| = ``"}"``, remove_empty: bool = ``false``)

Takes a string with embedded tokens and replaces them with values from a dictionary. Tokens are defined by ``tk_start`` and ``tk_end``, and are ``{}`` by default. If ``remove_empty`` is ``true``, tokens that are not found in the dictionary are removed from the string.

.. code-block:: gdscript

	var raw_str = "Hello {name}! You are {age} years old."

	JSONUtils.format_string_with_substitutes(raw_str, {"name": "John", "age": 30})
	# Returns "Hello John! You are 30 years old."

	JSONUtils.format_string_with_substitutes(raw_str, {"name": "John"})
	# Returns "Hello John! You are {age} years old."

	JSONUtils.format_string_with_substitutes(raw_str, {"name": "John"}, "{", "}", remove_empty = true)
	# Returns "Hello John! You are years old."
