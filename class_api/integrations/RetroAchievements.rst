.. include:: /global/godot_api.rst

.. _api_RetroAchievements:

RetroAchievements
=================

This is the main class to interact with RetroAchievements.

.. note::

	For a proper guide on how to use this integration, please refer to the :ref:`dedicated integration guide <theme_integrations_retroachievements>`.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_bool|
	  - :ref:`is_available <api_RetroAchievements_is_available>`
	* - |godot_string|
	  - :ref:`get_cheevos_dir <api_RetroAchievements_get_cheevos_dir>`
	* - |godot_string|
	  - :ref:`get_cheevos_hash_cache_path <api_RetroAchievements_get_cheevos_hash_cache_path>`
	* - |godot_dictionary|
	  - :ref:`build_auth <api_RetroAchievements_build_auth>`
	* - :ref:`api_RetroAchievements_GameInfo`
	  - :ref:`get_game_info <api_RetroAchievements_get_game_info>`
	* - |godot_string|
	  - :ref:`get_game_hash <api_RetroAchievements_get_game_hash>`

----

.. _api_RetroAchievements_is_available:

	static |godot_bool| **is_available** ()

Indicates whether the RetroAchievements integration is enabled by the user. If this returns ``false``, any usage of this API results in undefined behavior.

.. warning::

	It is only safe to instantiate this class if this function returns ``true``. Otherwise, the instance will remove itself and become ``null``, which may cause crashes.

.. note::

	This only refers to RetroHub's configuration. The API itself may be unavailable for other reasons, such as the user not being logged in, or network issues.

----

.. _api_RetroAchievements_get_cheevos_dir:

	static |godot_string| **get_cheevos_dir** ()

Returns the path to the directory where RetroAchievements stores its data. Used internally by RetroHub.

----

.. _api_RetroAchievements_get_cheevos_hash_cache_path:

	static |godot_string| **get_cheevos_hash_cache_path** ()

Returns the path to the file where RetroAchievements stores the known ROM hashes. Used internally by RetroHub.

----

.. _api_RetroAchievements_build_auth:

	|godot_dictionary| **build_auth** (|godot_bool| reload_credentials = ``false``)

Builds an authentication |godot_dictionary|, needed for any raw API calls. If ``reload_credentials`` is ``true``, the credentials will be re-fetched from the user's configuration.

.. warning::

	You will only need to ``reload_credentials``  if using the :ref:`api_RetroAchievements_Raw` endpoints; if you're only using the high-level API calls on this page, this is not needed.

	Additionally, only ``reload_credentials`` when you known the credentials are invalid (e.g. receiving ``401`` HTTP response codes), as every force reload will cause file I/O to load user credentials.

----

.. _api_RetroAchievements_get_game_info:

	:ref:`api_RetroAchievements_GameInfo` **get_game_info** (:ref:`api_RetroHubGameData` data)

Returns a :ref:`api_RetroAchievements_GameInfo` object for the given game. This object contains all achievement information for themes to use.

.. note::

	This function is asynchronous; use ``await`` to wait for it's completion.

----

.. _api_RetroAchievements_get_game_hash:

	|godot_string| **get_game_hash** (:ref:`api_RetroHubGameData` data)

Returns the hash of the given game. This is used for identifying game files in RetroAchievements.

.. note::

	RetroAchievements has it's own hashing algorithms dependant on different game files. Check their `documentation <https://docs.retroachievements.org/Game-Identification/>`_ for more information.
