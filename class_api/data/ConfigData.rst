.. include:: /global/godot_api.rst
.. include:: /global/rh_actions.rst

.. _api_ConfigData:

ConfigData
==========

This class holds app configuration information from RetroHub. This is not directly accessible from themes, and instead passed on through the :ref:`config_ready <api_RetroHubConfig_config_ready>` and :ref:`config_updated <api_RetroHubConfig_config_updated>` signals.

Constants
---------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_string|
	  - :ref:`KEY_CONFIG_VERSION <api_ConfigData_KEY_CONFIG_VERSION>`
	* - |godot_string|
	  - :ref:`KEY_IS_FIRST_TIME <api_ConfigData_KEY_IS_FIRST_TIME>`
	* - |godot_string|
	  - :ref:`KEY_GAMES_DIR <api_ConfigData_KEY_GAMES_DIR>`
	* - |godot_string|
	  - :ref:`KEY_CURRENT_THEME <api_ConfigData_KEY_CURRENT_THEME>`
	* - |godot_string|
	  - :ref:`KEY_LANG <api_ConfigData_KEY_LANG>`
	* - |godot_string|
	  - :ref:`KEY_FULLSCREEN <api_ConfigData_KEY_FULLSCREEN>`
	* - |godot_string|
	  - :ref:`KEY_VSYNC <api_ConfigData_KEY_VSYNC>`
	* - |godot_string|
	  - :ref:`KEY_RENDER_RESOLUTION <api_ConfigData_KEY_RENDER_RESOLUTION>`
	* - |godot_string|
	  - :ref:`KEY_REGION <api_ConfigData_KEY_REGION>`
	* - |godot_string|
	  - :ref:`KEY_RATING_SYSTEM <api_ConfigData_KEY_RATING_SYSTEM>`
	* - |godot_string|
	  - :ref:`KEY_DATE_FORMAT <api_ConfigData_KEY_DATE_FORMAT>`
	* - |godot_string|
	  - :ref:`KEY_SYSTEM_NAMES <api_ConfigData_KEY_SYSTEM_NAMES>`
	* - |godot_string|
	  - :ref:`KEY_SCRAPER_HASH_FILE_SIZE <api_ConfigData_KEY_SCRAPER_HASH_FILE_SIZE>`
	* - |godot_string|
	  - :ref:`KEY_SCRAPER_SS_USE_CUSTOM_ACCOUNT <api_ConfigData_KEY_SCRAPER_SS_USE_CUSTOM_ACCOUNT>`
	* - |godot_string|
	  - :ref:`KEY_SCRAPER_SS_MAX_THREADS <api_ConfigData_KEY_SCRAPER_SS_MAX_THREADS>`
	* - |godot_string|
	  - :ref:`KEY_CUSTOM_INPUT_REMAP <api_ConfigData_KEY_CUSTOM_INPUT_REMAP>`
	* - |godot_string|
	  - :ref:`KEY_INPUT_KEY_MAP <api_ConfigData_KEY_INPUT_KEY_MAP>`
	* - |godot_string|
	  - :ref:`KEY_INPUT_CONTROLLER_MAP <api_ConfigData_KEY_INPUT_CONTROLLER_MAP>`
	* - |godot_string|
	  - :ref:`KEY_INPUT_CONTROLLER_MAIN_AXIS <api_ConfigData_KEY_INPUT_CONTROLLER_MAIN_AXIS>`
	* - |godot_string|
	  - :ref:`KEY_INPUT_CONTROLLER_SECONDARY_AXIS <api_ConfigData_KEY_INPUT_CONTROLLER_SECONDARY_AXIS>`
	* - |godot_string|
	  - :ref:`KEY_INPUT_CONTROLLER_ICON_TYPE <api_ConfigData_KEY_INPUT_CONTROLLER_ICON_TYPE>`
	* - |godot_string|
	  - :ref:`KEY_INPUT_CONTROLLER_ECHO_PRE_DELAY <api_ConfigData_KEY_INPUT_CONTROLLER_ECHO_PRE_DELAY>`
	* - |godot_string|
	  - :ref:`KEY_INPUT_CONTROLLER_ECHO_DELAY <api_ConfigData_KEY_INPUT_CONTROLLER_ECHO_DELAY>`
	* - |godot_string|
	  - :ref:`KEY_VIRTUAL_KEYBOARD_LAYOUT <api_ConfigData_KEY_VIRTUAL_KEYBOARD_LAYOUT>`
	* - |godot_string|
	  - :ref:`KEY_VIRTUAL_KEYBOARD_TYPE <api_ConfigData_KEY_VIRTUAL_KEYBOARD_TYPE>`
	* - |godot_string|
	  - :ref:`KEY_VIRTUAL_KEYBOARD_SHOW_ON_CONTROLLER <api_ConfigData_KEY_VIRTUAL_KEYBOARD_SHOW_ON_CONTROLLER>`
	* - |godot_string|
	  - :ref:`KEY_VIRTUAL_KEYBOARD_SHOW_ON_MOUSE <api_ConfigData_KEY_VIRTUAL_KEYBOARD_SHOW_ON_MOUSE>`
	* - |godot_bool|
	  - :ref:`KEY_ACCESSIBILITY_SCREEN_READER_ENABLED <api_ConfigData_KEY_ACCESSIBILITY_SCREEN_READER_ENABLED>`
	* - |godot_string|
	  - :ref:`KEY_CUSTOM_GAMEMEDIA_DIR <api_ConfigData_KEY_CUSTOM_GAMEMEDIA_DIR>`
	* - |godot_string|
	  - :ref:`KEY_UI_VOLUME <api_ConfigData_KEY_UI_VOLUME>`
	* - |godot_string|
	  - :ref:`KEY_INTEGRATION_RCHEEVOS_ENABLED <api_ConfigData_KEY_INTEGRATION_RCHEEVOS_ENABLED>`

----

.. _api_ConfigData_KEY_CONFIG_VERSION:

	|godot_string| **KEY_CONFIG_VERSION** = ``"config_version"``

Key for the :ref:`config_version <api_ConfigData_config_version>` property.

----

.. _api_ConfigData_KEY_IS_FIRST_TIME:

	|godot_string| **KEY_IS_FIRST_TIME** = ``"is_first_time"``

Key for the :ref:`is_first_time <api_ConfigData_is_first_time>` property.

----

.. _api_ConfigData_KEY_GAMES_DIR:

	|godot_string| **KEY_GAMES_DIR** = ``"games_dir"``

Key for the :ref:`games_dir <api_ConfigData_games_dir>` property.

----

.. _api_ConfigData_KEY_CURRENT_THEME:

	|godot_string| **KEY_CURRENT_THEME** = ``"current_theme"``

Key for the :ref:`current_theme <api_ConfigData_current_theme>` property.

----

.. _api_ConfigData_KEY_LANG:

	|godot_string| **KEY_LANG** = ``"lang"``

Key for the :ref:`lang <api_ConfigData_lang>` property.

----

.. _api_ConfigData_KEY_FULLSCREEN:

	|godot_string| **KEY_FULLSCREEN** = ``"fullscreen"``

Key for the :ref:`fullscreen <api_ConfigData_fullscreen>` property.

----

.. _api_ConfigData_KEY_VSYNC:

	|godot_string| **KEY_VSYNC** = ``"vsync"``

Key for the :ref:`vsync <api_ConfigData_vsync>` property.

----

.. _api_ConfigData_KEY_RENDER_RESOLUTION:

	|godot_string| **KEY_RENDER_RESOLUTION** = ``"render_resolution"``

Key for the :ref:`render_resolution <api_ConfigData_render_resolution>` property.

----

.. _api_ConfigData_KEY_REGION:

	|godot_string| **KEY_REGION** = ``"region"``

Key for the :ref:`region <api_ConfigData_region>` property.

----

.. _api_ConfigData_KEY_RATING_SYSTEM:

	|godot_string| **KEY_RATING_SYSTEM** = ``"rating_system"``

Key for the :ref:`rating_system <api_ConfigData_rating_system>` property.

----

.. _api_ConfigData_KEY_DATE_FORMAT:

	|godot_string| **KEY_DATE_FORMAT** = ``"date_format"``

Key for the :ref:`date_format <api_ConfigData_date_format>` property.

----

.. _api_ConfigData_KEY_SYSTEM_NAMES:

	|godot_string| **KEY_SYSTEM_NAMES** = ``"system_names"``

Key for the :ref:`system_names <api_ConfigData_system_names>` property.

----

.. _api_ConfigData_KEY_SCRAPER_HASH_FILE_SIZE:

	|godot_string| **KEY_SCRAPER_HASH_FILE_SIZE** = ``"scraper_hash_file_size"``

Key for the :ref:`scraper_hash_file_size <api_ConfigData_scraper_hash_file_size>` property.

----

.. _api_ConfigData_KEY_SCRAPER_SS_USE_CUSTOM_ACCOUNT:

	|godot_string| **KEY_SCRAPER_SS_USE_CUSTOM_ACCOUNT** = ``"scraper_ss_use_custom_account"``

Key for the :ref:`scraper_ss_use_custom_account <api_ConfigData_scraper_ss_use_custom_account>` property.

----

.. _api_ConfigData_KEY_SCRAPER_SS_MAX_THREADS:

	|godot_string| **KEY_SCRAPER_SS_MAX_THREADS** = ``"scraper_ss_max_threads"``

Key for the :ref:`scraper_ss_max_threads <api_ConfigData_scraper_ss_max_threads>` property.

----

.. _api_ConfigData_KEY_CUSTOM_INPUT_REMAP:

	|godot_string| **KEY_CUSTOM_INPUT_REMAP** = ``"custom_input_remap"``

Key for the :ref:`custom_input_remap <api_ConfigData_custom_input_remap>` property.

----

.. _api_ConfigData_KEY_INPUT_KEY_MAP:

	|godot_string| **KEY_INPUT_KEY_MAP** = ``"input_key_map"``

Key for the :ref:`input_key_map <api_ConfigData_input_key_map>` property.

----

.. _api_ConfigData_KEY_INPUT_CONTROLLER_MAP:

	|godot_string| **KEY_INPUT_CONTROLLER_MAP** = ``"input_controller_map"``

Key for the :ref:`input_controller_map <api_ConfigData_input_controller_map>` property.

----

.. _api_ConfigData_KEY_INPUT_CONTROLLER_MAIN_AXIS:

	|godot_string| **KEY_INPUT_CONTROLLER_MAIN_AXIS** = ``"input_controller_main_axis"``

Key for the :ref:`input_controller_main_axis <api_ConfigData_input_controller_main_axis>` property.

----

.. _api_ConfigData_KEY_INPUT_CONTROLLER_SECONDARY_AXIS:

	|godot_string| **KEY_INPUT_CONTROLLER_SECONDARY_AXIS** = ``"input_controller_secondary_axis"``

Key for the :ref:`input_controller_secondary_axis <api_ConfigData_input_controller_secondary_axis>` property.

----

.. _api_ConfigData_KEY_INPUT_CONTROLLER_ICON_TYPE:

	|godot_string| **KEY_INPUT_CONTROLLER_ICON_TYPE** = ``"input_controller_icon_type"``

Key for the :ref:`input_controller_icon_type <api_ConfigData_input_controller_icon_type>` property.

----

.. _api_ConfigData_KEY_INPUT_CONTROLLER_ECHO_PRE_DELAY:

	|godot_string| **KEY_INPUT_CONTROLLER_ECHO_PRE_DELAY** = ``"input_controller_echo_pre_delay"``

Key for the :ref:`input_controller_echo_pre_delay <api_ConfigData_input_controller_echo_pre_delay>` property.

----

.. _api_ConfigData_KEY_INPUT_CONTROLLER_ECHO_DELAY:

	|godot_string| **KEY_INPUT_CONTROLLER_ECHO_DELAY** = ``"input_controller_echo_delay"``

Key for the :ref:`input_controller_echo_delay <api_ConfigData_input_controller_echo_delay>` property.

----

.. _api_ConfigData_KEY_VIRTUAL_KEYBOARD_LAYOUT:

	|godot_string| **KEY_VIRTUAL_KEYBOARD_LAYOUT** = ``"virtual_keyboard_layout"``

Key for the :ref:`virtual_keyboard_layout <api_ConfigData_virtual_keyboard_layout>` property.

----

.. _api_ConfigData_KEY_VIRTUAL_KEYBOARD_TYPE:

	|godot_string| **KEY_VIRTUAL_KEYBOARD_TYPE** = ``"virtual_keyboard_type"``

Key for the :ref:`virtual_keyboard_type <api_ConfigData_virtual_keyboard_type>` property.

----

.. _api_ConfigData_KEY_VIRTUAL_KEYBOARD_SHOW_ON_CONTROLLER:

	|godot_string| **KEY_VIRTUAL_KEYBOARD_SHOW_ON_CONTROLLER** = ``"virtual_keyboard_show_on_controller"``

Key for the :ref:`virtual_keyboard_show_on_controller <api_ConfigData_virtual_keyboard_show_on_controller>` property.

----

.. _api_ConfigData_KEY_VIRTUAL_KEYBOARD_SHOW_ON_MOUSE:

	|godot_string| **KEY_VIRTUAL_KEYBOARD_SHOW_ON_MOUSE** = ``"virtual_keyboard_show_on_mouse"``

Key for the :ref:`virtual_keyboard_show_on_mouse <api_ConfigData_virtual_keyboard_show_on_mouse>` property.

----

.. _api_ConfigData_KEY_ACCESSIBILITY_SCREEN_READER_ENABLED:

	|godot_string| **KEY_ACCESSIBILITY_SCREEN_READER_ENABLED** = ``"accessibility_screen_reader_enabled"``

Key for the :ref:`accessibility_screen_reader_enabled <api_ConfigData_accessibility_screen_reader_enabled>` property.

----

.. _api_ConfigData_KEY_CUSTOM_GAMEMEDIA_DIR:

	|godot_string| **KEY_CUSTOM_GAMEMEDIA_DIR** = ``"custom_gamemedia_dir"``

Key for the :ref:`custom_gamemedia_dir <api_ConfigData_custom_gamemedia_dir>` property.

----

.. _api_ConfigData_KEY_UI_VOLUME:

	|godot_string| **KEY_UI_VOLUME** = ``"ui_volume"``

Key for the :ref:`ui_volume <api_ConfigData_ui_volume>` property.

----

.. _api_ConfigData_KEY_INTEGRATION_RCHEEVOS_ENABLED:

	|godot_string| **KEY_INTEGRATION_RCHEEVOS_ENABLED** = ``"integration_rcheevos_enabled"``

Key for the :ref:`integration_rcheevos_enabled <api_ConfigData_integration_rcheevos_enabled>` property.

Properties
----------

.. list-table::
	:widths: 20 60 20
	:header-rows: 1

	* - Type
	  - Name
	  - Default
	* - |godot_int|
	  - :ref:`config_version <api_ConfigData_config_version>`
	  - ``1``
	* - |godot_bool|
	  - :ref:`is_first_time <api_ConfigData_is_first_time>`
	  - ``true``
	* - |godot_string|
	  - :ref:`games_dir <api_ConfigData_games_dir>`
	  - :ref:`FileUtils.get_home_dir() <api_FileUtils_get_home_dir>` + ``"/ROMS"``
	* - |godot_string|
	  - :ref:`current_theme <api_ConfigData_current_theme>`
	  - ``"default"``
	* - |godot_string|
	  - :ref:`lang <api_ConfigData_lang>`
	  - ``"en"``
	* - |godot_bool|
	  - :ref:`fullscreen <api_ConfigData_fullscreen>`
	  - ``true``
	* - |godot_bool|
	  - :ref:`vsync <api_ConfigData_vsync>`
	  - ``true``
	* - |godot_int|
	  - :ref:`render_resolution <api_ConfigData_render_resolution>`
	  - ``100``
	* - |godot_string|
	  - :ref:`region <api_ConfigData_region>`
	  - ``"usa"``
	* - |godot_string|
	  - :ref:`rating_system <api_ConfigData_rating_system>`
	  - ``"esrb"``
	* - |godot_string|
	  - :ref:`date_format <api_ConfigData_date_format>`
	  - ``"mm/dd/yyyy"``
	* - |godot_dictionary|
	  - :ref:`system_names <api_ConfigData_system_names>`
	  - |godot_dictionary|
	* - |godot_int|
	  - :ref:`scraper_hash_file_size <api_ConfigData_scraper_hash_file_size>`
	  - ``64``
	* - |godot_bool|
	  - :ref:`scraper_ss_use_custom_account <api_ConfigData_scraper_ss_use_custom_account>`
	  - ``false``
	* - |godot_int|
	  - :ref:`scraper_ss_max_threads <api_ConfigData_scraper_ss_max_threads>`
	  - ``6``
	* - |godot_string|
	  - :ref:`custom_input_remap <api_ConfigData_custom_input_remap>`
	  - ``""``
	* - |godot_dictionary|
	  - :ref:`input_key_map <api_ConfigData_input_key_map>`
	  - |godot_dictionary|
	* - |godot_dictionary|
	  - :ref:`input_controller_map <api_ConfigData_input_controller_map>`
	  - |godot_dictionary|
	* - |godot_int|
	  - :ref:`input_controller_main_axis <api_ConfigData_input_controller_main_axis>`
	  - ``JOY_ANALOG_LX``
	* - |godot_int|
	  - :ref:`input_controller_secondary_axis <api_ConfigData_input_controller_secondary_axis>`
	  - ``JOY_ANALOG_RX``
	* - |godot_int|
	  - :ref:`input_controller_icon_type <api_ConfigData_input_controller_icon_type>`
	  - ``0``
	* - |godot_float|
	  - :ref:`input_controller_echo_pre_delay <api_ConfigData_input_controller_echo_pre_delay>`
	  - ``0.75``
	* - |godot_float|
	  - :ref:`input_controller_echo_delay <api_ConfigData_input_controller_echo_delay>`
	  - ``0.15``
	* - |godot_string|
	  - :ref:`virtual_keyboard_layout <api_ConfigData_virtual_keyboard_layout>`
	  - ``"qwerty"``
	* - |godot_string|
	  - :ref:`virtual_keyboard_type <api_ConfigData_virtual_keyboard_type>`
	  - ``"builtin"``
	* - |godot_bool|
	  - :ref:`virtual_keyboard_show_on_controller <api_ConfigData_virtual_keyboard_show_on_controller>`
	  - ``true``
	* - |godot_bool|
	  - :ref:`virtual_keyboard_show_on_mouse <api_ConfigData_virtual_keyboard_show_on_mouse>`
	  - ``false``
	* - |godot_bool|
	  - :ref:`accessibility_screen_reader_enabled <api_ConfigData_accessibility_screen_reader_enabled>`
	  - ``false``
	* - |godot_string|
	  - :ref:`custom_gamemedia_dir <api_ConfigData_custom_gamemedia_dir>`
	  - ``""``
	* - |godot_int|
	  - :ref:`ui_volume <api_ConfigData_ui_volume>`
	  - ``100``
	* - |godot_bool|
	  - :ref:`integration_rcheevos_enabled <api_ConfigData_integration_rcheevos_enabled>`
	  - ``false``

----

.. _api_ConfigData_config_version:

	|godot_int| **config_version** = ``1``

Specifies the latest internal configuration version. This is used internally to determine if the configuration needs to be updated.

----

.. _api_ConfigData_is_first_time:

	|godot_bool| **is_first_time** = ``true``

If ``true``, this is the first time the user is running RetroHub, therefore the first-time wizard will be shown. Themes are not loaded until the first-time wizard is completed, so in practice this property is always ``false`` when queried by the theme.

----

.. _api_ConfigData_games_dir:

	|godot_string| **games_dir** = :ref:`FileUtils.get_home_dir() <api_FileUtils_get_home_dir>` + ``"/ROMS"``

The user's game library. This is the directory where RetroHub will look for games.

----

.. _api_ConfigData_current_theme:

	|godot_string| **current_theme** = ``"default"``

The currently loaded theme. If lacking any extension, it will load a default theme at ``res://default_themes/{current_theme}.pck``. Otherwise, the theme is loaded from ``<retrohub_config_dir>/themes/{current_theme}.``

----

.. _api_ConfigData_lang:

	|godot_string| **lang** = ``"en"``

Language. Used throughout the UI and for themes that support localization as well.

Valid values:
	* ``"en"``: English

----

.. _api_ConfigData_fullscreen:

	|godot_bool| **fullscreen** = ``true``

If ``true``, RetroHub will run in fullscreen mode, otherwise it will run in windowed mode.

----

.. _api_ConfigData_vsync:

	|godot_bool| **vsync** = ``true``

If ``true``, RetroHub will enable V-Sync.

----

.. _api_ConfigData_render_resolution:

	|godot_int| **render_resolution** = ``100``

Theme render resolution, in percentage. Doesn't affect RetroHub's UI. Can range from ``50`` to ``100``.

----

.. _api_ConfigData_region:

	|godot_string| **region** = ``"usa"``

User's preferred region.

Valid values:
	* ``"usa"``: USA
	* ``"eur"``: Europe
	* ``"jpn"``: Japan

----

.. _api_ConfigData_rating_system:

	|godot_string| **rating_system** = ``"esrb"``

User's preferred age rating system.

Valid values:
	* ``"esrb"``: ESRB
	* ``"pegi"``: PEGI
	* ``"cero"``: CERO

----

.. _api_ConfigData_date_format:

	|godot_string| **date_format** = ``"mm/dd/yyyy"``

User's preferred date formatting.

Valid values:
	* ``"mm/dd/yyyy"``: month / day / year
	* ``"dd/mm/yyyy"``: day / month / year
	* ``"yyyy/mm/dd"``: year / month / day

----

.. _api_ConfigData_system_names:

	|godot_dictionary| **system_names** = |godot_dictionary|

Chosen system remaps per region. Each key determines the displayed name for the system.

----

.. _api_ConfigData_scraper_hash_file_size:

	|godot_int| **scraper_hash_file_size** = ``64``

Maximum allowed size, in MB, of game files to be hashed for scraping. This is used to avoid scraping large files. Set to ``0`` to disable this limit.

----

.. _api_ConfigData_scraper_ss_use_custom_account:

	|godot_bool| **scraper_ss_use_custom_account** = ``false``

If ``true``, uses a user's account details when using ScreenScraper. Used to bypass global API quota limits.

----

.. _api_ConfigData_scraper_ss_max_threads:

	|godot_int| **scraper_ss_max_threads** = ``6``

Maximum amount of threads to use when scraping with ScreenScraper with a custom account. Set this to limit thread usage to a specific number.

.. note::
	RetroHub will always check how many threads your account has available. If this value is bigger than your allowed thread count, RetroHub will respect your account's thread limit.

----

.. _api_ConfigData_custom_input_remap:

	|godot_string| **custom_input_remap** = ``""``

Custom controller layout string. This follows the SDL format. See :ref:`userguide_input_controller_layouts` for more information.

----

.. _api_ConfigData_input_key_map:

	|godot_dictionary| **input_key_map** = |godot_dictionary|

Input map for keyboard actions. Keys are RetroHub's input actions, available on :ref:`theme_input_input_actions`. Values are KEY_* constants available in `@GlobalScope <https://docs.godotengine.org/en/4.1/classes/class_%40globalscope.html#enum-globalscope-key>`__.

----

.. _api_ConfigData_input_controller_map:

	|godot_dictionary| **input_controller_map** = |godot_dictionary|

Input map for controller actions. Keys are RetroHub's input actions, available on :ref:`theme_input_input_actions`. Values are JOY_* constants available in `@GlobalScope <https://docs.godotengine.org/en/4.1/classes/class_%40globalscope.html#enum-globalscope-joybutton>`__.

----

.. _api_ConfigData_input_controller_main_axis:

	|godot_int| **input_controller_main_axis** = ``JOY_ANALOG_LX``

Main joystick axis for controller input. This is used for navigation.

Valid values:
	* ``JOY_ANALOG_LX``: Left stick
	* ``JOY_ANALOG_RX``: Right stick

----

.. _api_ConfigData_input_controller_secondary_axis:

	|godot_int| **input_controller_secondary_axis** = ``JOY_ANALOG_RX``

Secondary joystick axis for controller input. This is used for scrolling.

Valid values:
	* ``JOY_ANALOG_LX``: Left stick
	* ``JOY_ANALOG_RX``: Right stick

----

.. _api_ConfigData_input_controller_icon_type:

	|godot_int| **input_controller_icon_type** = ``0``

Type of controller icons.

Valid values:
	* ``0``: Detect controller automatically
	* ``1``: Xbox 360
	* ``2``: Xbox One
	* ``3``: Xbox Series
	* ``4``: PS3
	* ``5``: PS4
	* ``6``: PS5
	* ``7``: Switch (Controller)
	* ``8``: Switch (Joy-Con)
	* ``9``: Steam Controller
	* ``10``: Steam Deck
	* ``11``: Amazon Luna
	* ``12``: Google Stadia

----

.. _api_ConfigData_input_controller_echo_pre_delay:

	|godot_float| **input_controller_echo_pre_delay** = ``0.75``

Pre-delay in seconds for controller echo events. This is the amount of time a user has to keep a button pressed/axis moved before it starts repeating.

----

.. _api_ConfigData_input_controller_echo_delay:

	|godot_float| **input_controller_echo_delay** = ``0.15``

Delay in seconds between controller echo events. This dictactes the frequency of controller echo events.

----

.. _api_ConfigData_virtual_keyboard_layout:

	|godot_string| **virtual_keyboard_layout** = ``"qwerty"``

Preferred virtual keyboard layout.

Valid values:
	* ``"qwerty"``: QWERTY
	* ``"qwertz"``: QWERTZ
	* ``"azerty"``: AZERTY

----

.. _api_ConfigData_virtual_keyboard_type:

	|godot_string| **virtual_keyboard_type** = ``"builtin"``

What virtual keyboard to use.

Valid values:
	* ``"builtin"``: App built-in virtual keyboard
	* ``"steam"``: Steam/Steam Deck virtual keyboard

----

.. _api_ConfigData_virtual_keyboard_show_on_controller:

	|godot_bool| **virtual_keyboard_show_on_controller** = ``true``

If ``true``, shows the virtual keyboard when a controller is connected and a given valid node is selected with |action-joy: rh_accept|.

----

.. _api_ConfigData_virtual_keyboard_show_on_mouse:

	|godot_bool| **virtual_keyboard_show_on_mouse** = ``false``

If ``true``, shows the virtual keyboard when a mouse click or touch event is done on a valid node.

----

.. _api_ConfigData_accessibility_screen_reader_enabled:

	|godot_bool| **accessibility_screen_reader_enabled** = ``false``

If ``true``, enables screen reader support.

----

.. _api_ConfigData_custom_gamemedia_dir:

	|godot_string| **custom_gamemedia_dir** = ``""``

If specificed, stores downloaded media files separately from the main configuration directory, on a user specified path.

----

.. _api_ConfigData_ui_volume:

	|godot_int| **ui_volume** = ``100``

UI volume, in percentage. Can range from ``0`` to ``100``.

----

.. _api_ConfigData_integration_rcheevos_enabled:

	|godot_bool| **integration_rcheevos_enabled** = ``false``

If ``true``, enables RetroHub's integration with the `RetroAchievements <https://retroachievements.org/>`__ service.