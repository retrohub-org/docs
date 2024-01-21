.. include:: /global/godot_api.rst

.. _api_RetroAchievements_Achievement:

RetroAchievements.Achievement
=============================

This class contains information of a specific achievement from a :ref:`api_RetroAchievements_GameInfo` object.

.. note::

	For a proper guide on how to use this integration, please refer to the :ref:`dedicated integration guide <theme_integrations_retroachievements>`.

Enumerations
------------

.. _api_RetroAchievements_Achievement_Type_Enum:

enum **Type**:

- **NORMAL** - A normal achievement.
- **PROGRESSION** - An achievement that denotes some in-game progression.
- **WIN** - An achievement obtainable by reaching (one of) the game's ending.
- **MISSABLE** - An achievement that can be missed during a playthrough, requiring the player to start a new game to obtain it.

Properties
----------

.. list-table::
	:widths: 20 70 10
	:header-rows: 1

	* - Type
	  - Name
	  - Default
	* - |godot_int|
	  - :ref:`id <api_RetroAchievements_Achievement_id>`
	  - ``0``
	* - |godot_string|
	  - :ref:`title <api_RetroAchievements_Achievement_title>`
	  - ``""``
	* - |godot_string|
	  - :ref:`description <api_RetroAchievements_Achievement_description>`
	  - ``""``
	* - :ref:`Achievement.Type <api_RetroAchievements_Achievement_Type_Enum>`
	  - :ref:`type <api_RetroAchievements_Achievement_type>`
	  - ``NORMAL``
	* - |godot_bool|
	  - :ref:`unlocked <api_RetroAchievements_Achievement_unlocked>`
	  - ``false``
	* - |godot_bool|
	  - :ref:`unlocked_hard_mode <api_RetroAchievements_Achievement_unlocked_hard_mode>`
	  - ``false``
	* - |godot_int|
	  - :ref:`unlocked_count <api_RetroAchievements_Achievement_unlocked_count>`
	  - ``0``
	* - |godot_int|
	  - :ref:`unlocked_hard_mode_count <api_RetroAchievements_Achievement_unlocked_hard_mode_count>`
	  - ``0``

----

.. _api_RetroAchievements_Achievement_id:

	|godot_int| **id** = ``0``

The achievement's ID on RetroAchievements.

----

.. _api_RetroAchievements_Achievement_title:

	|godot_string| **title** = ``""``

The achievement's title.

----

.. _api_RetroAchievements_Achievement_description:

	|godot_string| **description** = ``""``

The achievement's description.

----

.. _api_RetroAchievements_Achievement_type:

	:ref:`Achievement.Type <api_RetroAchievements_Achievement_Type_Enum>` **type** = ``NORMAL``

The achievement's type.

----

.. _api_RetroAchievements_Achievement_unlocked:

	|godot_bool| **unlocked** = ``false``

Whether the achievement has been unlocked.

----

.. _api_RetroAchievements_Achievement_unlocked_hard_mode:

	|godot_bool| **unlocked_hard_mode** = ``false``

Whether the achievement has been unlocked, in hard mode.

----

.. _api_RetroAchievements_Achievement_unlocked_count:

	|godot_int| **unlocked_count** = ``0``

How many players unlocked this achievement.

----

.. _api_RetroAchievements_Achievement_unlocked_hard_mode_count:

	|godot_int| **unlocked_hard_mode_count** = ``0``

How many players unlocked this achievement, in hard mode.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_texture|
	  - :ref:`load_icon <api_RetroAchievements_Achievement_load_icon>`
	* - void
	  - :ref:`parse_raw <api_RetroAchievements_Achievement_parse_raw>`

----

.. _api_RetroAchievements_Achievement_load_icon:

	|godot_texture| **load_icon** ()

Loads the achievement's icon. If the icon doesn't exist yet, it will download it from RetroAchievements' servers and store it automatically.

.. warning::

	This function will queue downloads, which cannot be canceled. A large queue will create delays on other API calls that require any network access. Therefore, you should only call this function only when immediately needed, and take care to not call it for a lot of achievements at once.

.. note::

	This function is asynchronous; use an ``await`` to wait for it's completion.

----

.. _api_RetroAchievements_Achievement_parse_raw:

	void **parse_raw** (|godot_dictionary| data)

Parses a raw JSON response from RetroAchievements's API into this object. Used internally by RetroHub.
