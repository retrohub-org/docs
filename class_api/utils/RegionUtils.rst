.. include:: /global/godot_api.rst

.. _api_RegionUtils:

RegionUtils
===========

This is a helper class to handle challenges with presenting information in the user's region.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_string|
	  - :ref:`localize_date <api_RegionUtils_localize_date>`
	* - |godot_string|
	  - :ref:`globalize_date_str <api_RegionUtils_globalize_date_str>`
	* - |godot_string|
	  - :ref:`globalize_date_dict <api_RegionUtils_globalize_date_dict>`
	* - |godot_control|
	  - :ref:`localize_age_rating <api_RegionUtils_localize_age_rating>`
	* - |godot_string|
	  - :ref:`localize_system_name <api_RegionUtils_localize_system_name>`

----

.. _api_RegionUtils_localize_date:

	|godot_string| **localize_date** (date_raw: |godot_string|)

Localizes a raw date string which is in ISO8601 format.

.. code-block:: gdscript

	# User prefers DD/MM/YYYY
	RegionUtils.localize_date("19870102T152741") # Returns "02/01/1987 15:27:41"

----

.. _api_RegionUtils_globalize_date_str:

	|godot_string| **globalize_date_str** (date_raw: |godot_string|, source_format: |godot_string| = ``""``)

Globalizes a previously localized date with :ref:`localize_date <api_RegionUtils_localize_date>` back to a global ISO8601 format. ``source_format`` can be specified to tell in which format the string is (one of :ref:`date_format <api_ConfigData_date_format>`), otherwise leave it empty to use the current user's region.

.. code-block:: gdscript

	# User prefers DD/MM/YYYY
	RegionUtils.globalize_date_str("02/01/1987 15:27:41") # Returns "19870102T152741"

----

.. _api_RegionUtils_globalize_date_dict:

	|godot_string| **globalize_date_dict** (date_dict: |godot_dictionary|, source_format: |godot_string| = ``""``)

Globalizes a date dictionary coming from `Godot <https://docs.godotengine.org/en/3.5/classes/class_time.html#class-time-method-get-datetime-dict-from-system>`_ back to a global ISO8601 format. ``source_format`` can be specified to tell in which format the string is (one of :ref:`date_format <api_ConfigData_date_format>`), otherwise leave it empty to use the current user's region.

.. code-block:: gdscript

	# User prefers DD/MM/YYYY
	RegionUtils.globalize_date_dict({
		"year": 1987, "month": 1,
		"day": 2, "hour": 15,
		"minute": 27, "second": 41
	}) # Returns "19870102T152741"

----

.. _api_RegionUtils_localize_age_rating:

	|godot_control| **localize_age_rating** (age_rating_raw: |godot_string|)

Localizes an age rating string to the user's preferred age rating system. This returns a |godot_control| depicting that information which you should add in your theme's scene tree.

.. code-block:: gdscript

	# User prefers PEGI
	RegionUtils.localize_age_rating("2/3/4") # Returns a Control with the PEGI 12 rating icon

----

.. _api_RegionUtils_localize_system_name:

	|godot_string| **localize_system_name** (system_name: |godot_string|)

Localizes a short system name to the user's preferred system name.

.. code-block:: gdscript

	# User prefers "Sega Megadrive"
	RegionUtils.localize_system_name("genesis") # Returns "megadrive"
