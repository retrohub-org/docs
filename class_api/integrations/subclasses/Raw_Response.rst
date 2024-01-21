.. include:: /global/godot_api.rst

.. _api_RetroAchievements_Raw_Response:

RetroAchievements.Raw.Response
==============================

Class holding API responses from the :ref:`api_RetroAchievements_Raw` class.

Properties
----------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_int|
	  - :ref:`godot_error <api_RetroAchievements_Raw_Response_godot_error>`
	* - |godot_int|
	  - :ref:`response_code <api_RetroAchievements_Raw_Response_response_code>`
	* - |godot_dictionary| / |godot_array|
	  - :ref:`body <api_RetroAchievements_Raw_Response_body>`

----

.. _api_RetroAchievements_Raw_Response_godot_error:

	|godot_int| **godot_error**

Godot error code. If not ``OK``, there was some internal error when making the HTTP request.

----

.. _api_RetroAchievements_Raw_Response_response_code:

	|godot_int| **response_code**

HTML response code. If not ``200``, the request failed on the server side.

----

.. _api_RetroAchievements_Raw_Response_body:

	|godot_dictionary| / |godot_array| **body**

The response JSON body, already parsed into a |godot_dictionary| or |godot_array|.
