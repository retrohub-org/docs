.. include:: /global/godot_api.rst

.. _api_RetroHubGameData:

RetroHubGameData
================

Represents a game entry from the user's library. Holds all informations available about a game. It is generated by :ref:`api_RetroHub` when the app in launched, and passed to themes through the :ref:`game_received <api_RetroHub_game_received>` signal.

The received object is unique and shared among the app. An instance can also be used to uniquely identify this game, which is done for other parts of the API.

Enumerations
------------

.. _api_RetroHubGameData_BoxTextureRegions:

enum **BoxTextureRegions**:

- **BACK** - Back cover.
- **SPINE** - Spine portion.
- **FRONT** - Front cover.

Properties
----------

.. list-table::
	:widths: 20 70 10
	:header-rows: 1

	* - Type
	  - Name
	  - Default
	* - |godot_bool|
	  - :ref:`has_metadata <api_RetroHubGameData_has_metadata>`
	  - ``false``
	* - |godot_bool|
	  - :ref:`has_media <api_RetroHubGameData_has_media>`
	  - ``false``
	* - :ref:`api_RetroHubSystemData`
	  - :ref:`system <api_RetroHubGameData_system>`
	  - *other*
	* - |godot_string|
	  - :ref:`system_path <api_RetroHubGameData_system_path>`
	  - ``""``
	* - |godot_string|
	  - :ref:`name <api_RetroHubGameData_name>`
	  - *other*
	* - |godot_string|
	  - :ref:`path <api_RetroHubGameData_path>`
	  - *other*
	* - |godot_string|
	  - :ref:`description <api_RetroHubGameData_description>`
	  - ``""``
	* - |godot_float|
	  - :ref:`rating <api_RetroHubGameData_rating>`
	  - ``0.0``
	* - |godot_string|
	  - :ref:`release_date <api_RetroHubGameData_release_date>`
	  - ``""``
	* - |godot_string|
	  - :ref:`developer <api_RetroHubGameData_developer>`
	  - ``""``
	* - |godot_string|
	  - :ref:`publisher <api_RetroHubGameData_publisher>`
	  - ``""``
	* - |godot_array|
	  - :ref:`genres <api_RetroHubGameData_genres>`
	  - ``[]``
	* - |godot_string|
	  - :ref:`num_players <api_RetroHubGameData_num_players>`
	  - ``""``
	* - |godot_string|
	  - :ref:`age_rating <api_RetroHubGameData_age_rating>`
	  - ``""``
	* - |godot_bool|
	  - :ref:`favorite <api_RetroHubGameData_favorite>`
	  - ``false``
	* - |godot_int|
	  - :ref:`play_count <api_RetroHubGameData_play_count>`
	  - ``0``
	* - |godot_string|
	  - :ref:`last_played <api_RetroHubGameData_last_played>`
	  - ``""``
	* - |godot_string|
	  - :ref:`emulator <api_RetroHubGameData_emulator>`
	  - ``""``
	* - |godot_dictionary|
	  - :ref:`box_texture_regions <api_RetroHubGameData_box_texture_regions>`
	  - ``{}``

----

.. _api_RetroHubGameData_has_metadata:

	|godot_bool| **has_metadata** = ``false``

Whether there's metadata available. If ``false``, only the :ref:`name <api_RetroHubGameData_name>` and :ref:`path <api_RetroHubGameData_path>` properties are guaranteed to be valid. In that case, :ref:`name <api_RetroHubGameData_name>` will be set to the game's file name.

----

.. _api_RetroHubGameData_has_media:

	|godot_bool| **has_media** = ``false``

Whether there's media available for this game. If ``false``, any calls to retrieve media will fail.

.. note::
	This only denotes the existence of any media, and doesn't guarantee that all media types are available.

----

.. _api_RetroHubGameData_system:

	:ref:`api_RetroHubSystemData` **system** = ``<valid system instance>``

The :ref:`api_RetroHubSystemData` this game belongs to.

----

.. _api_RetroHubGameData_system_path:

	|godot_string| **system_path** = ``""``

The physical system folder this game comes from. Because of system remaps for different regions, the :ref:`system <api_RetroHubGameData_system>` may be pointing to a different system from the game file's location. This is used internally by RetroHub to determine the correct system for the game when launching the game.

----

.. _api_RetroHubGameData_name:

	|godot_string| **name** = ``"..."``

The game's name. This field is always set even when :ref:`has_metadata <api_RetroHubGameData_has_metadata>` is ``false``, in which case it will be set to the game's file name.

----

.. _api_RetroHubGameData_path:

	|godot_string| **path** = ``"..."``

The game's file absolute path. This field is always set even when :ref:`has_metadata <api_RetroHubGameData_has_metadata>` is ``false``.

----

.. _api_RetroHubGameData_description:

	|godot_string| **description** = ``""``

The game's description.

----

.. _api_RetroHubGameData_rating:

	|godot_float| **rating** = ``0.0``

The game's rating, which ranges between ``0.0`` and ``1.0``.

----

.. _api_RetroHubGameData_release_date:

	|godot_string| **release_date** = ``""``

The game's release date, in ISO8601 format. Use :ref:`RegionUtils.localize_date() <api_RegionUtils_localize_date>` to convert it to the user's local date format.

----

.. _api_RetroHubGameData_developer:

	|godot_string| **developer** = ``""``

The game's developer.

----

.. _api_RetroHubGameData_publisher:

	|godot_string| **publisher** = ``""``

The game's publisher.

----

.. _api_RetroHubGameData_genres:

	|godot_array| **genres** = ``[]``

The game's genres. This is an array of strings.

----

.. _api_RetroHubGameData_num_players:

	|godot_string| **num_players** = ``""``

The game's number of players, in the format ``"{min_players}-{max_players}"``. This is used to represent both singleplayer (``"1-1"``) and multiplayer (``"2-4"``) games.

----

.. _api_RetroHubGameData_age_rating:

	|godot_string| **age_rating** = ``""``

The game's age rating, in the format ``"{esrb}/{pegi}/{cero}"``. Values range from 0 to 5, where 0 means unknown, and 1 through 5 increasing levels of age rating. Use :ref:`RegionUtils.localize_age_rating <api_RegionUtils_localize_age_rating>` to get the appropriate rating as a |godot_texture|.

----

.. _api_RetroHubGameData_favorite:

	|godot_bool| **favorite** = ``false``

Whether the game is marked as a favorite.

----

.. _api_RetroHubGameData_play_count:

	|godot_int| **play_count** = ``0``

The number of times the game has been played.

----

.. _api_RetroHubGameData_last_played:

	|godot_string| **last_played** = ``""``

The date the game was last played, in ISO8601 format. Use :ref:`RegionUtils.localize_date() <api_RegionUtils_localize_date>` to convert it to the user's local date format.

.. warning::
	If never played before, the string will be set to ``"null"``.

----

.. _api_RetroHubGameData_emulator:

	|godot_string| **emulator** = ``""``

Used internally by RetroHub to specify a specific emulator to be used when launching the game.

----

.. _api_RetroHubGameData_box_texture_regions:

	|godot_dictionary| **box_texture_regions** = ``{}``

Defines regions of the game's box art texture. This allows you to extract specific regions of the box art, such as the front portion. See :ref:`RetroHubMedia.get_box_texture_region() <api_RetroHubMedia_get_box_texture_region>` for more information.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_bool|
	  - :ref:`sort <api_RetroHubGameData_sort>`
	* - void
	  - :ref:`copy_from <api_RetroHubGameData_copy_from>`

----

.. _api_RetroHubGameData_sort:

	|godot_bool| **sort** (a: :ref:`api_RetroHubGameData`, b: :ref:`api_RetroHubGameData`)

Custom sorting implementation for :ref:`api_RetroHubGameData` instances. This is used internally by RetroHub to sort games by name, in ascending order. You can also use this if you need to sort game datas, by using `Array.sort_custom() <https://docs.godotengine.org/en/4.1/classes/class_array.html#class-array-method-sort-custom>`_.

.. code-block:: gdscript

	var game_datas = [...]

	game_datas.sort_custom(RetroHubGameData, "sort")

	# game_datas will now be sorted by names

----

.. _api_RetroHubGameData_copy_from:

	void **copy_from** (other: :ref:`api_RetroHubGameData`)

Copies all information from existing game data, creating a duplicate.
