.. include:: /global/godot_api.rst

.. _api_TTS:

TTS
===

This is a helper class to handle text-to-speech functionality.

Virtual Methods
---------------

.. note::
	These methods should be implemented in other scripts to control TTS output. When a node gets focused, the TTS system will traverse the nodes and it's parents recursively in search of one of these methods, and if existing, use it's text output instead.

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - |godot_string|
	  - :ref:`tts_text <api_TTS_tts_text>`
	* - |godot_string|
	  - :ref:`tts_tree_item_text <api_TTS_tts_tree_item_text>`
	* - |godot_string|
	  - :ref:`tts_range_value_text <api_TTS_tts_range_value_text>`
	* - |godot_string|
	  - :ref:`tts_popup_menu_item_text <api_TTS_tts_popup_menu_item_text>`

----

.. _api_TTS_tts_text:

	|godot_string| **tts_text** (focused: |godot_control|)

Generic TTS text method. This is called when a node gets focused. The ``focused`` parameter is the node that got focused, and is a child of either the node where this script is, or of one of this children.

This method should return the text to be spoken, which overrides the default implementation. If it returns an empty string, the TTS system will continue traversing the parent methods, and use the default implementation if no further node overrides it.

.. code-block:: gdscript

	func tts_text(focused):
		if focused is $MyLabel:
			# Override output in this particular case
			return "Hey, my label got focused!"
		# We're not interested in this node, so return an empty string
		return ""

----

.. _api_TTS_tts_tree_item_text:

	|godot_string| **tts_tree_item_text** (item: |godot_tree_item|, tree: |godot_tree|)

Specific TTS text for a focused cell on a |godot_tree| node.

This method should return the text to be spoken, which overrides the default implementation. If it returns an empty string, the TTS system will continue traversing the parent methods, and use the default implementation if no further node overrides it.

----

.. _api_TTS_tts_range_value_text:

	|godot_string| **tts_range_value_text** (value: |godot_float|, range: |godot_range|)

Specific TTS text for a focused |godot_range| node. It supplies the current node's value to customize how it is presented to the user.

This method should return the text to be spoken, which will be appended to the default implementation. If it returns an empty string, the TTS system will continue traversing the parent methods, and use the default implementation if no further node overrides it.

.. warning::
	Always use the supplied value, not the range's value. The TTS system might use different values, such as minimum/maximum ranges.


.. code-block:: gdscript

	func tts_range_value_text(value, range):
		if range is $FilesizeRange:
			# This range works with file sizes, so add a suffix
			return "%d megabytes" % value
		# We're not interested in this node, so return an empty string
		return ""

----

.. _api_TTS_tts_popup_menu_item_text:

	|godot_string| **tts_popup_menu_item_text** (idx: |godot_int|, menu: |godot_popupmenu|)

Specific TTS text for a focused |godot_popupmenu| node. It supplies the currently selected menu item.

This method should return the text to be spoken, which will be appended to the default implementation. If it returns an empty string, the TTS system will continue traversing the parent methods, and use the default implementation if no further node overrides it.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - void
	  - :ref:`speak <api_TTS_speak>`
	* - void
	  - :ref:`stop <api_TTS_stop>`
	* - |godot_bool|
	  - :ref:`is_speaking <api_TTS_is_speaking>`
	* - |godot_string|
	  - :ref:`singular_or_plural <api_TTS_singular_or_plural>`

----

.. _api_TTS_speak:

	void **speak** (text: |godot_string|, interrupt: |godot_bool| = ``true``)

Speaks the given text. If ``interrupt`` is ``true``, the current speech is interrupted, ttherwise, the new text is queued.

.. code-block:: gdscript

	TTS.speak("Hello")
	TTS.speak("World!", false)
	# Will speak "Hello World!"

----

.. _api_TTS_stop:

	void **stop** ()

Stops any current speech immediately.

----

.. _api_TTS_is_speaking:

	|godot_bool| **is_speaking** ()

Returns whether the TTS system is currently speaking any sentence.

----

.. _api_TTS_singular_or_plural:

	|godot_string| **singular_or_plural** (count: |godot_int|, singular: |godot_string|, plural: |godot_string|)

Returns the singular or plural form of a word depending on the given count. Useful if using variables and the final text needs to change due to pluralization.

.. code-block:: gdscript

	var count = 5
	TTS.speak("You have %d %s" % [
		count,
		TTS.singular_or_plural(count, "apple", "apples")
	])