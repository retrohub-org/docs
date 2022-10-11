.. include:: /global/godot_api.rst

.. _api_RetroHubGameMediaData:

RetroHubGameMediaData
=====================

Holds media information for a given :ref:`api_RetroHubGameData`. Retrieved through calls to :ref:`api_RetroHubMedia`.

.. warning::
	Of all the data classes, this one is the heaviest to have in memory, as all game assets are loaded into VRAM. Therefore, you must be careful to ensure this is deleted when you don't need it anymore.

Properties
----------

.. list-table::
	:widths: 20 70 10
	:header-rows: 1

	* - Type
	  - Name
	  - Default
	* - |godot_image_texture|
	  - :ref:`logo <api_RetroHubGameMediaData_logo>`
	  - ``null``
	* - |godot_image_texture|
	  - :ref:`screenshot <api_RetroHubGameMediaData_screenshot>`
	  - ``null``
	* - |godot_image_texture|
	  - :ref:`title_screen <api_RetroHubGameMediaData_title_screen>`
	  - ``null``
	* - |godot_video_stream|
	  - :ref:`video <api_RetroHubGameMediaData_video>`
	  - ``null``
	* - |godot_image_texture|
	  - :ref:`box_render <api_RetroHubGameMediaData_box_render>`
	  - ``null``
	* - |godot_image_texture|
	  - :ref:`box_texture <api_RetroHubGameMediaData_box_texture>`
	  - ``null``
	* - |godot_image_texture|
	  - :ref:`support_render <api_RetroHubGameMediaData_support_render>`
	  - ``null``
	* - |godot_image_texture|
	  - :ref:`support_texture <api_RetroHubGameMediaData_support_texture>`
	  - ``null``
	* - <undefined>
	  - :ref:`manual <api_RetroHubGameMediaData_manual>`
	  - ``null``

----

.. _api_RetroHubGameMediaData_logo:

	|godot_image_texture| **logo** = ``null``

The game's logo, usually the title art.

----

.. _api_RetroHubGameMediaData_screenshot:

	|godot_image_texture| **screenshot** = ``null``

A screenshot of the game in action.

----

.. _api_RetroHubGameMediaData_title_screen:

	|godot_image_texture| **title_screen** = ``null``

A screenshot of the game's title screen.

----

.. _api_RetroHubGameMediaData_video:

	|godot_video_stream| **video** = ``null``

A video of the game in action.

----

.. _api_RetroHubGameMediaData_box_render:

	|godot_image_texture| **box_render** = ``null``

A pre-rendered image of the game's box art.

----

.. _api_RetroHubGameMediaData_box_texture:

	|godot_image_texture| **box_texture** = ``null``

A raw texture of the game's box art. This can be used to create a 3D model.

.. note::
	Automatic generation of box art models is planned for a future release.

----

.. _api_RetroHubGameMediaData_support_render:

	|godot_image_texture| **support_render** = ``null``

A pre-rendered image of the game's physical support *(cartridge, CD, etc.)*

----

.. _api_RetroHubGameMediaData_support_texture:

	|godot_image_texture| **support_texture** = ``null``

A raw texture of the game's physical support *(cartridge, CD, etc.)*. This can be used to create a 3D model.

.. note::
	Automatic generation of physical support models is planned for a future release.

----

.. _api_RetroHubGameMediaData_manual:

	**manual** = ``null``

The game's manual. Currently unimplemented, will always be ``null``.