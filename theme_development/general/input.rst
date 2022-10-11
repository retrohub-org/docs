.. include:: /global/rh_actions.rst

.. _theme_input:

Input
=====

Input is handled by RetroHub first, then passed onto the theme. This is to ensure input works properly if an app menu is open, as well as fix some issues regarding controller input.


.. _theme_input_input_actions:

Input actions
-------------

Your theme should ideally only use input actions to ensure full compatibility, which also letting users easily remap controls to their liking. The following input actions are available:

+-----------------------+--------------------------------+-----------------------------------+
| Action                | Description                    | Default keys                      +
+=======================+================================+===================================+
| **rh_up**             | Move up                        | |action: rh_up|                   +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_down**           | Move down                      | |action: rh_down|                 +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_left**           | Move left                      | |action: rh_left|                 +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_right**          | Move right                     | |action: rh_right|                +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_accept**         | Accept a given action          | |action: rh_accept|               +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_back**           | Cancel a given action          | |action: rh_back|                 +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_major_option**   | Major/frequent option          | |action: rh_major_option|         +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_minor_option**   | Minor/rare option              | |action: rh_minor_option|         +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_theme_menu**     | Open the theme menu            | |action: rh_theme_menu|           +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_left_shoulder**  | Slide left                     | |action: rh_left_shoulder|        +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_right_shoulder** | Slide right                    | |action: rh_right_shoulder|       +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_left_trigger**   | Trigger left                   | |action: rh_left_trigger|         +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_right_trigger**  | Trigger right                  | |action: rh_right_trigger|        +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_rstick_left**    | Move the right stick left      | |action: rh_rstick_left|          +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_rstick_right**   | Move the right stick right     | |action: rh_rstick_right|         +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_rstick_up**      | Move the right stick up        | |action: rh_rstick_up|            +
+-----------------------+--------------------------------+-----------------------------------+
| **rh_rstick_down**    | Move the right stick down      | |action: rh_rstick_down|          +
+-----------------------+--------------------------------+-----------------------------------+

Input Icons
-----------

RetroHub uses `Controller Icons <https://github.com/rsubtil/controller_icons>`_ to show appropriate icons for each input method. This addon automatically switches icons between keyboard/mouse and controllers, so use it to display how to perform a given action in your theme. `Here's a quick guide to get started <https://github.com/rsubtil/controller_icons/blob/3.x/DOCS.md>`_.

Controllers and UI
------------------

Ideally your theme is fully usable with a controller, without requiring any keyboard/mouse input. If you use Godot's builtin UI nodes, you need to ensure that these nodes receive focus, and that their focus neighbors are set as well. Here are a few more tips:

- Godot will rarely set a node as focused on the first frame. Call ``grab_focus`` on ``_ready()`` to ensure there's always a focused node.
- Controls that require keyboard input, such as ``LineEdit``, ``TextEdit`` and ``SpinBox`` are automatically handled by RetroHub. If you need the virtual keyboard for another type of node, you can manually call ``RetroHubUI.show_virtual_keyboard()``. More information on the :ref:`UI section <theme_section_ui>` and in the :ref:`api_RetroHubUI` class reference.

.. note::
	To design a theme for controllers without having one available, ensure you can use your theme with only the keyboard, and that you never have to use the mouse to access some part of your theme.