.. include:: /global/godot_api.rst

.. _api_RetroHubMedia:

RetroHubMedia
=============

This class handles media loading for :ref:`api_RetroHubGameData` instances.

Enumerations
------------

.. _api_RetroHubMedia_Type:

enum **Type**:

- **LOGO = 1** - Game logo.
- **SCREENSHOT = 2** - Game screenshot.
- **TITLE_SCREEN = 4** - Game title screen.
- **VIDEO = 8** - Game video.
- **BOX_RENDER = 16** - Game box render.
- **BOX_TEXTURE = 32** - Game box texture.
- **SUPPORT_RENDER = 64** - Game physical support render.
- **SUPPORT_TEXTURE = 128** - Game physical support texture.
- **MANUAL = 256** - Game manual.
- **ALL = 511** - All media types.


Signals
-------

.. _api_RetroHubMedia_media_loaded:

	**media_loaded** (media_data: :ref:`api_RetroHubGameMediaData`, game_data: :ref:`api_RetroHubGameData`, types: :ref:`Type <api_RetroHubMedia_Type>`)

Emitted when an asynchronous request for media has finished loading. Returns the original game data and requested types when doing the request, which allows to uniquely identify this request among others.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - void
	  - :ref:`clear_media_cache <api_RetroHubMedia_clear_media_cache>`
	* - void
	  - :ref:`clear_all_media_cache <api_RetroHubMedia_clear_all_media_cache>`
	* - |godot_array|
	  - :ref:`convert_type_bitmask_to_list <api_RetroHubMedia_convert_type_bitmask_to_list>`
	* - |godot_string|
	  - :ref:`convert_type_to_media_path <api_RetroHubMedia_convert_type_to_media_path>`
	* - :ref:`api_RetroHubGameMediaData`
	  - :ref:`retrieve_media_data <api_RetroHubMedia_retrieve_media_data>`
	* - :ref:`api_RetroHubGameMediaData`
	  - :ref:`retrieve_media_blurhash <api_RetroHubMedia_retrieve_media_blurhash>`
	* - void
	  - :ref:`retrieve_media_data_async <api_RetroHubMedia_retrieve_media_data_async>`
	* - :ref:`api_RetroHubGameMediaData`
	  - :ref:`retrieve_media_data_and_blurhash_async <api_RetroHubMedia_retrieve_media_data_and_blurhash_async>`
	* - void
	  - :ref:`cancel_media_data_async <api_RetroHubMedia_cancel_media_data_async>`
	* - |godot_texture2d|
	  - :ref:`get_box_texture_region <api_RetroHubMedia_get_box_texture_region>`

----

.. _api_RetroHubMedia_clear_media_cache:

	void **clear_media_cache** (data: :ref:`api_RetroHubGameMediaData`)

Clears the internal media cache for the given data. The media will thus be freed if the theme doesn't reference it anymore.

----

.. _api_RetroHubMedia_clear_all_media_cache:

	void **clear_all_media_cache** ()

Clears the entire internal media cache. Unreference data will be freed.

----

.. _api_RetroHubMedia_convert_type_bitmask_to_list:

	|godot_array| **convert_type_bitmask_to_list** (bitmask: :ref:`Type <api_RetroHubMedia_Type>`)

Converts a bitmask of media types to a list with each type separated, to make it easily iterable.

.. code-block:: gdscript

	# Returns [Type.LOGO, Type.VIDEO]
	convert_type_bitmask_to_list(Type.LOGO | Type.VIDEO)

----

.. _api_RetroHubMedia_convert_type_to_media_path:

	|godot_string| **convert_type_to_media_path** (type: :ref:`Type <api_RetroHubMedia_Type>`)

Converts a media type to its corresponding path in the RetroHub media directory. Used internally when saving downloaded media. If an invalid/unknown ``type`` is passed, returns the string ``"unknown"``.

.. code-block:: gdscript

	# Returns "support_render"
	convert_type_to_media_path(Type.SUPPORT_TEXTURE)

----

.. _api_RetroHubMedia_retrieve_media_data:

	:ref:`api_RetroHubGameMediaData` **retrieve_media_data** (game_data: :ref:`api_RetroHubGameData`, types: :ref:`Type <api_RetroHubMedia_Type>` = ``Type.ALL``)

Retrieves media for the requested game data. If ``types`` is not specified, all media types will be retrieved.

Returns a :ref:`api_RetroHubGameMediaData` instance with the requested media data. If game data doesn't have :ref:`has_media <api_RetroHubGameData_has_media>` set to ``true``, returns ``null`` instead.

This function blocks while media is loaded, so if you want to load plenty of media files without freezing your theme, use :ref:`retrieve_media_data_async <api_RetroHubMedia_retrieve_media_data_async>` instead.

.. code-block:: gdscript

	# Returns a RetroHubMediaData instance with all media types
	var media_data = retrieve_media_data(game_data)

	# Returns a RetroHubMediaData instance with only the logo and video
	var media_data = retrieve_media_data(game_data, Type.LOGO | Type.VIDEO)

.. note::
	The :ref:`Type <api_RetroHubMedia_Type>` enum is a bitmask, so you can combine any types you need using the bitwise OR operator (``|``).

.. warning::
	Never assume a given media type is available. Always check that the requested media file is non ``null`` before using it.

----

.. _api_RetroHubMedia_retrieve_media_blurhash:

	:ref:`api_RetroHubGameMediaData` **retrieve_media_blurhash** (game_data: :ref:`api_RetroHubGameData`, types: :ref:`Type <api_RetroHubMedia_Type>` = ``Type.ALL``)

Fetches BlurHash data for existing game media, returning media data with blurred previews of the requested media types. Although the function is blocking, fetching a BlurHash is very quick, so this can be repeatedly called without freezing your theme.

.. note::
	The :ref:`Type <api_RetroHubMedia_Type>` enum is a bitmask, so you can combine any types you need using the bitwise OR operator (``|``).

.. warning::
	Never assume a given media type is available. Always check that the requested media file is non ``null`` before using it.

----

.. _api_RetroHubMedia_retrieve_media_data_async:

	void **retrieve_media_data_async** (game_data: :ref:`api_RetroHubGameData`, types: :ref:`Type <api_RetroHubMedia_Type>` = ``Type.ALL``, priority: |godot_bool| = ``false``)

Retrieves media for the requested game data asynchronously. If ``types`` is not specified, all media types will be retrieved. If ``priority`` is ``true``, the request will be given priority over pending async requests.

This function returns immediately, and the :ref:`media_loaded <api_RetroHubMedia_media_loaded>` signal will be emitted when the media has finished loading. You should keep a reference to the supplied game data and types, to later be able to identify this request among others.

If game data doesn't have :ref:`has_media <api_RetroHubGameData_has_media>` set to ``true``, the request is never made, and so the signal will never be emitted.

.. code-block:: gdscript

	connect("media_loaded", self, "on_media_loaded")

	# Loads all media types asynchronously
	retrieve_media_data_async(game_data, Type.ALL)
	
	func on_media_loaded(media_data, game_data, types):
		if self.game_data == game_data and types == Type.ALL:
			# This was the request we asked. Use media
			...

.. note::
	The :ref:`Type <api_RetroHubMedia_Type>` enum is a bitmask, so you can combine any types you need using the bitwise OR operator (``|``).

.. warning::
	Never assume a given media type is available. Always check that the requested media file is not ``null`` before using it.

----

.. _api_RetroHubMedia_retrieve_media_data_and_blurhash_async:

	:ref:`api_RetroHubGameMediaData` **retrieve_media_data_and_blurhash_async** (game_data: :ref:`api_RetroHubGameData`, types: :ref:`Type <api_RetroHubMedia_Type>` = ``Type.ALL``, priority: |godot_bool| = ``false``)

Calls :ref:`retrieve_media_data_async <api_RetroHubMedia_retrieve_media_data_async>` and :ref:`retrieve_media_blurhash <api_RetroHubMedia_retrieve_media_blurhash>` at the same time. This provides you with a quick media preview while the media request is handled asynchronously.

.. note::
	The :ref:`Type <api_RetroHubMedia_Type>` enum is a bitmask, so you can combine any types you need using the bitwise OR operator (``|``).

.. warning::
	Never assume a given media type is available. Always check that the requested media file is not ``null`` before using it.

----

.. _api_RetroHubMedia_cancel_media_data_async:

	void **cancel_media_data_async** (game_data: :ref:`api_RetroHubGameData`)

Cancels all pending asynchronous request done with :ref:`retrieve_media_data_async <api_RetroHubMedia_retrieve_media_data_async>` under that game data. This is useful if you want to cancel a request that you don't need anymore, to avoid wasting resources.

.. note::
	This will cancel all requests for a given game_data, even if multiple requests were made with different types.

.. note::
	A request may still finish and be sent over the :ref:`media_loaded <api_RetroHubMedia_media_loaded>` signal even after calling this function.

----

.. _api_RetroHubMedia_get_box_texture_region:

	|godot_texture2d| **get_box_texture_region** (game_data: :ref:`api_RetroHubGameData`, media_data: :ref:`api_RetroHubGameMediaData`, region: :ref:`RetroHubGameData.BoxTextureRegions <api_RetroHubGameData_BoxTextureRegions>`, rotate: |godot_bool| = ``true``)

Extracts the specified box region from a game box art. This allows you to only use relevant portions of the box art, like the front cover. If ``rotate`` is ``true``, it will also rotate the region to ensure text is displayed left-to-right.

If the media data doesn't have any box art, or the game data :ref:`box_texture_regions <api_RetroHubGameData_box_texture_regions>` doesn't contain the specified ``region``, this function returns ``null``.

.. code-block:: gdscript


	# Get the front cover of the box texture.
	get_box_texture_region(game_data, media_data, RetroHubGameData.BoxTextureRegions.FRONT)

	# Get the spine portion of the box texture, without rotating it (since they're usually vertical).
	get_box_texture_region(game_data, media_data, RetroHubGameData.BoxTextureRegions.SPINE, false)

