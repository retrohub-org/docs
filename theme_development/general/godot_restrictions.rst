Godot restrictions
==================

Despite a theme being essentially a Godot project, not everything can be used as expected. The following features are restricted or outright unavailable to use:

- **Project Settings**: Any custom value that's saved as a project setting (anything set under the Project tab) is lost when exporting the project, as the settings file is neither exported nor used in RetroHub. Custom input actions, physics layer names, render/window settings and others will be lost when the theme is exported.
- **Singletons**: Since Singletons/AutoLoads are set in the project settings, this information is not saved on exporting. Furthermore, Godot loads singletons internally, so this functionality is not exposed in GDScript to modify them at runtime. To overcome this, you can preload the singleton script/scene and propagate it in scripts as necessary:

.. code-block:: gdscript

	var MySingleton := preload("res://path/to/MySingleton.gd")

	MySingleton.do_something()

	foo(MySingleton)

	def foo(MySingleton):
		MySingleton.do_something()

- **Localization**: There's no support for localization files yet. RetroHub will offer some mechanism to support localization in themes in the future.
- **Root Viewport**: RetroHub runs themes in a dedicated viewport. This means that the root viewport is not the same as the one in the editor. Do not depend on any specific behavior of the root viewport, such as using it to detect the true screen size.
- **Viewport scaling & stretching**: RetroHub simulates the ``2D`` stretch and ``keep_height`` aspect properties for `handling multiple resolutions <https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html#stretch-settings>`_. This is to ensure a UI designed for the base resolutions scales well on other resolutions, particularly for TVs. Right now, themes have no control over this behavior, but in the future it may be possible to override this.
- **Controller Input**: Controller input is finicky by default for UI elements. If you try to use the joystick for selecting UI elements, you'll find it goes all over the place and doesn't allow for proper selection of elements. This is an issue from Godot that's `yet to be solved at the time of writing <https://github.com/godotengine/godot-proposals/issues/4911>`_. RetroHub has a global system to that "hijacks" controller input and solves this problem, so when your theme is exported, it should work normally. For development, avoid using the stick for navigation, and use the DPAD/keyboard instead. For more details on how to ensure controller input works in your theme, check the :ref:`theme_input` section.
- **Video Playback**: Playback of x264/x265 files (``.mp4``) files will not work outside of RetroHub's official builds. Godot cannot support these codecs because `"H.264 and H.265 cannot be supported in core Godot, as they are both encumbered by software patents." <https://docs.godotengine.org/en/stable/tutorials/animation/playing_videos.html>`_.
