.. include:: /global/godot_api.rst

.. _api_RetroAchievements_GameInfo:

RetroAchievements.GameInfo
==========================

This class contains all information about a game's achievements.

.. note::

	For a proper guide on how to use this integration, please refer to the :ref:`dedicated integration guide <theme_integrations_retroachievements>`.

Enumerations
------------

.. _api_RetroAchievements_GameInfo_Error:

enum **Error**:

- **OK** - Success / no error.
- **ERR_INVALID_CRED** - The user's credentials are invalid.
- **ERR_CONSOLE_NOT_SUPPORTED** - The requested game's system is not supported by RetroAchievements.
- **ERR_GAME_NOT_FOUND** - The requested game hash was not found on RetroAchievements.
- **ERR_NETWORK** - A network error occurred.
- **ERR_INTERNAL** - An internal error occurred.

Properties
----------

.. list-table::
	:widths: 20 70 10
	:header-rows: 1

	* - Type
	  - Name
	  - Default
	* - :ref:`GameInfo.Error <api_RetroAchievements_GameInfo_Error>`
	  - :ref:`err <api_RetroAchievements_GameInfo_err>`
	  - ``OK``
	* - |godot_int|
	  - :ref:`id <api_RetroAchievements_GameInfo_id>`
	  - ``0``
	* - |godot_array| [ :ref:`api_RetroAchievements_Achievement` ]
	  - :ref:`achievements <api_RetroAchievements_GameInfo_achievements>`
	  - ``[]``
	* - |godot_int|
	  - :ref:`player_count <api_RetroAchievements_GameInfo_player_count>`
	  - ``0``

----

.. _api_RetroAchievements_GameInfo_err:

	:ref:`GameInfo.Error <api_RetroAchievements_GameInfo_Error>` **err** = ``OK``

The error code of the function call that generated/returned this game info. If not ``OK``, the remaining properties will have no meaning, and this object should be discarded.

----

.. _api_RetroAchievements_GameInfo_id:

	|godot_int| **id** = ``0``

The game's ID on RetroAchievements.

----

.. _api_RetroAchievements_GameInfo_achievements:

	|godot_array| [ :ref:`api_RetroAchievements_Achievement` ] **achievements** = ``[]``

An |godot_array| of :ref:`api_RetroAchievements_Achievement` objects, containing all the achievements available for this game.

----

.. _api_RetroAchievements_GameInfo_player_count:

	|godot_int| **player_count** = ``0``

The total number of players that have played this game on RetroAchievements.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - void
	  - :ref:`parse_raw <api_RetroAchievements_GameInfo_parse_raw>`

----

.. _api_RetroAchievements_GameInfo_parse_raw:

	void **parse_raw** (|godot_dictionary| data)

Parses a raw JSON response from RetroAchievements's API into this object. Used internally by RetroHub.
