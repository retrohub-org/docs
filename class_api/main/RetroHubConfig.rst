
.. include:: /global/godot_api.rst

.. _api_RetroHubConfig:

RetroHubConfig
==============

This class handles all configuration aspects of RetroHub.


Signals
-------

.. _api_RetroHubConfig_config_ready:

	**config_ready** (config_data: :ref:`api_ConfigData`)

Emitted when RetroHub has finished loading app configs. This signal is emitted after theme initialization.

----

.. _api_RetroHubConfig_config_updated:

	**config_updated** (key: |godot_string|, old_value: |godot_variant|, new_value: |godot_variant|)

Emitted when a config value of the app has been updated. ``key`` refers to one of the key constants defined in :ref:`api_ConfigData`, with ``old_value`` and ``new_value`` representing the old and new values of that config.

----

.. _api_RetroHubConfig_theme_config_ready:

	**theme_config_ready** ()

Emitted when RetroHub has finished loading theme configs. This signal is emitted after theme initialization, and configurations can be retrieved with :ref:`get_theme_config <api_RetroHubConfig_get_theme_config>`.

----

.. _api_RetroHubConfig_theme_config_updated:

	**theme_config_updated** (key: |godot_string|, old_value: |godot_variant|, new_value: |godot_variant|)

Emitted when a config value of the theme has been updated. ``key`` is the same value used on :ref:`get_theme_config <api_RetroHubConfig_get_theme_config>`/:ref:`set_theme_config <api_RetroHubConfig_set_theme_config>`, and therefore defined by your theme. ``old_value`` and ``new_value`` represent the old and new values of that config.

----

.. _api_RetroHubConfig_game_data_updated:

	**game_data_updated** (game_data: :ref:`api_RetroHubGameData`)

Emitted when a game data has been updated by the user. The reference doesn't change from the earlier data received from :ref:`game_received <api_RetroHub_game_received>`, so you can use it to test whether you need to update displayed information in your theme.

.. code-block:: gdscript

	connect("game_data_updated", self, "_on_game_data_updated")

	func _on_game_data_updated(game_data):
		if self.game_data == game_data:
			# Update displayed information with new info
			...

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_variant|
	  - :ref:`get_theme_config <api_RetroHubConfig_get_theme_config>`
	* - void
	  - :ref:`set_theme_config <api_RetroHubConfig_set_theme_config>`
	* - void
	  - :ref:`save_theme_config <api_RetroHubConfig_save_theme_config>`

----

.. _api_RetroHubConfig_get_theme_config:

	|godot_variant| **get_theme_config** (key: |godot_string|, default_value: |godot_variant|)

Get a theme config under the given ``key``. If the key doesn't exist, ``default_value`` is returned.

.. warning::
	If the key doesn't exist, ``default_value`` is not implicitely set in the configuration.

----

.. _api_RetroHubConfig_set_theme_config:

	void **set_theme_config** (key: |godot_string|, value: |godot_variant|)

Sets a theme config under the given ``key`` to ``value``. If the key doesn't exist, it is created.

.. warning::
	RetroHub only emits the :ref:`theme_config_updated <api_RetroHubConfig_theme_config_updated>` signal when the settings are saved with :ref:`save_theme_config <api_RetroHubConfig_save_theme_config>`.

----

.. _api_RetroHubConfig_save_theme_config:

	void **save_theme_config** ()

Saves the theme config to disk. For every ``key`` that has been changed, the :ref:`theme_config_updated <api_RetroHubConfig_theme_config_updated>` signal is emitted.

.. note::
	If you're using a dedicated theme config scene, RetroHub will automatically call this function by you when the theme is unloaded, and therefore you only need to use :ref:`set_theme_config <api_RetroHubConfig_set_theme_config>`.