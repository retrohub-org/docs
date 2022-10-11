.. include:: /global/godot_api.rst

.. _api_RetroHub:

RetroHub
========

This is the main class to interact with RetroHub. It is also the source of all information regarding the user's library.

Constants
---------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_int|
	  - :ref:`version_major <api_RetroHub_version_major>`
	* - |godot_int|
	  - :ref:`version_minor <api_RetroHub_version_minor>`
	* - |godot_int|
	  - :ref:`version_patch <api_RetroHub_version_patch>`
	* - |godot_string|
	  - :ref:`version_extra <api_RetroHub_version_extra>`
	* - |godot_string|
	  - :ref:`version_str <api_RetroHub_version_str>`

----

.. _api_RetroHub_version_major:

	|godot_int| **version_major**

Major version of RetroHub. A change in the major version number indicates a breaking change to RetroHub or Godot. Themes designed for a different major version are highly unlikely to work without significant modifications regarding RetroHub's API or even Godot changes.

----

.. _api_RetroHub_version_minor:

	|godot_int| **version_minor**

Minor version of RetroHub. A change in the minor version number indicates minor changes to RetroHub's API. Themes designed for a different minor version are highly unlikely to work without some modifications regarding RetroHub's API.

----

.. _api_RetroHub_version_patch:

	|godot_int| **version_patch**

Patch version of RetroHub. A change in the patch version number indicates mostly bug fixes or new features implemented in a backwards-compatible way. Themes designed for a different patch version are expected to work without issues.

----

.. _api_RetroHub_version_extra:

	|godot_string| **version_extra**

Extra information about the version, such as ``alpha`` or ``beta``. On release versions, this is empty.

----

.. _api_RetroHub_version_str:

	|godot_string| **version_str**

Fully assembled version string, for convenience, in the format ``{major}.{minor}.{patch}{extra}``.

Signals
-------

.. _api_RetroHub_app_initializing:

	**app_initializing** ()

Called only one time, when the app is initializing. Themes aren't able to catch this signal.

----

.. _api_RetroHub_app_closing:

	**app_closing** ()

Called only one time, when the app is closing.

----

.. _api_RetroHub_app_received_focus:

	**app_received_focus** ()

Called when the app receives focus.

----

.. _api_RetroHub_app_lost_focus:

	**app_lost_focus** ()

Called when the app loses focus.

----

.. _api_RetroHub_app_returning:

	**app_returning** (system_data: :ref:`api_RetroHubSystemData`, game_data: :ref:`api_RetroHubGameData`)

Called when the app is returning from a launched game. This signal is emitted after a full theme load cycle, notably after all the :ref:`system_received <api_RetroHub_system_received>` and :ref:`game_received <api_RetroHub_game_received>` signals have been emitted.

----

.. _api_RetroHub_system_receive_start:

	**system_receive_start** ()

Called when system data is about to be sent to the theme. This signal is emitted only if there's system data available.

----

.. _api_RetroHub_system_received:

	**system_received** (system_data: :ref:`api_RetroHubSystemData`)

Information about a :ref:`api_RetroHubSystemData`.

----

.. _api_RetroHub_system_receive_end:

	**system_receive_end** ()

Called when all system data has been sent. Game data will follow after this signal.

----

.. _api_RetroHub_game_receive_start:

	**game_receive_start** ()

Called when game data is about to be sent to the theme. This signal is emitted after all system data has been sent.

----

.. _api_RetroHub_game_received:

	**game_received** (game_data: :ref:`api_RetroHubGameData`)

Information about a :ref:`api_RetroHubGameData`.

----

.. _api_RetroHub_game_receive_end:

	**game_receive_end** ()

Called when all game data has been sent. By this point, all information about the user's gaming library has been sent.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - void
	  - :ref:`set_curr_game_data <api_RetroHub_set_curr_game_data>`
	* - |godot_bool|
	  - :ref:`is_main_app <api_RetroHub_is_main_app>`
	* - |godot_bool|
	  - :ref:`is_dev_env <api_RetroHub_is_dev_env>`
	* - |godot_bool|
	  - :ref:`is_input_echo <api_RetroHub_is_input_echo>`
	* - void
	  - :ref:`quit <api_RetroHub_quit>`
	* - void
	  - :ref:`launch_game <api_RetroHub_launch_game>`
	* - void
	  - :ref:`request_theme_reload <api_RetroHub_request_theme_reload>`

----

.. _api_RetroHub_set_curr_game_data:

	void **set_curr_game_data** (game_data: :ref:`api_RetroHubGameData`)

Sets the currently selected game data. This is needed to launch games, but also so users can edit and/or scrape game information from RetroHub.

----

.. _api_RetroHub_is_main_app:

	|godot_bool| **is_main_app** ()

Returns whether the theme is running on the main app, or under the theme helper addon.

----

.. _api_RetroHub_is_dev_env:

	|godot_bool| **is_dev_env** ()

Returns whether RetroHub is running in a developer environment or as a regular user. Used internally to create separate config folders.

----

.. _api_RetroHub_is_input_echo:

	|godot_bool| **is_input_echo** ()

Returns whether the current input event was generated by RetroHub. This is used to simulate echo events for controller inputs. This can be undesirable for some scenarios, so in that case, use this to ignore the event.

.. code-block:: gdscript

	func _input(event):
		if RetroHub.is_input_echo():
			return
		
		...

----

.. _api_RetroHub_quit:

	void **quit** ()

Request the app to quit. Theme configuration will be saved.

----

.. _api_RetroHub_launch_game:

	void **launch_game** ()

Launches the currently selected game. Must be set prior with :ref:`set_curr_game_data <api_RetroHub_set_curr_game_data>`. After this call, the theme will be unloaded, so this should be treated as an exit point where no more code from your will be executed.

----

.. _api_RetroHub_request_theme_reload:

	void **request_theme_reload** ()

Request RetroHub to fully reload your theme. This is useful if some major configuration was changed from the app, and it's easier to reload the theme than to try to update it in place.