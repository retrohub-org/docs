#!/usr/bin/env python3

# Reads systems and emulators JSON files from RetroHub and
# bootstraps pages with their description

from genericpath import exists
from re import fullmatch
import sys
import os
import json
from typing import Dict

def print_help(program_name):
	print(f"Usage:{program_name} <systems_file> <emulators_file> <output_dir> [--overwrite]")
	print(f"\tsystems_file = Systems JSON information from RetroHub")
	print(f"\temulators_file = Emulators JSON information from RetroHub")
	print(f"\toutput_dir = Root directory of \"docs\" repository to write generated files")
	print(f"\t--overwrite [optional] = Default doesn't override already existing files. Use this flag to override all files")

def convert_category(category):
	if category == "console":
		return "Console"
	elif category == "modern_console":
		return "Modern Console"
	elif category == "arcade":
		return "Arcade"
	elif category == "computer":
		return "Computer"
	elif category == "engine":
		return "Game Engine"
	print(f"\tUnmapped category \"{category}\", using raw value...")
	return category

def expand_definition(base, obj_list):
	if "extends" in base:
		for obj in obj_list:
			if obj["name"] == base["extends"]:
				tmp = obj.copy()
				for key in base:
					tmp[key] = base[key]
				return tmp
	return base

if "-h" in sys.argv or "--help" in sys.argv:
	print_help(sys.argv[0])
	sys.exit(0)


if len(sys.argv) < 4:
	print_help(sys.argv[0])
	sys.exit(-1)

systems_file = sys.argv[1]
emulators_file = sys.argv[2]
output_dir = sys.argv[3]
overwrite = "--overwrite" in sys.argv


# Start
system_data = {}
emulator_map = {}
emulator_systems = {}
with open(systems_file, "r") as sys_f:
	with open(emulators_file, "r") as emu_f:
		system_data = json.load(sys_f)
		emulator_data = json.load(emu_f)

print("|SYSTEMS|")
for system in system_data:
	system = expand_definition(system, system_data)
	system_name = system["name"]
	out_path = os.path.join(output_dir, "user_guide", "systems", "system_list", f"{system_name}.rst")
	if not overwrite and exists(out_path):
		print(f"[{system_name}] Already exists, skipping...")
		continue

	output = f""".. image:: /global/assets/systems/{system_name}-photo.png
	:width: 25%

.. image:: /global/assets/systems/{system_name}-logo.png
	:width: 73%

.. _system_{system_name}:

{system["fullname"]}
{'=' * len(system["fullname"])}

Basic Information
~~~~~~~~~~~~~~~~~
- **Short name:** ``{system_name}``
- **Type:** {convert_category(system["category"])}
- **Supported extensions:** {len(system["extension"])}
"""

	for extension in system["extension"]:
		output += f"	- {extension}\n"

	output += """\nNotes
~~~~~

There are no special notes for this system. Games should work out of the box.

Emulators
~~~~~~~~~"""
	for emulator in system["emulator"]:
		emulator_name = list(emulator.keys())[0] if isinstance(emulator, dict) else emulator
		output += f"""
- :ref:`emulator_{emulator_name}`"""
		if not emulator_name in emulator_systems:
			emulator_systems[emulator_name] = [system_name]
		else:
			emulator_systems[emulator_name].append(system_name)

	with open(out_path, "w") as f:
		f.writelines(output)
		print(f"[{system_name}] -> {out_path}")

print("|EMULATORS|")
for emulator in emulator_data:
	emulator = expand_definition(emulator, emulator_data)
	emulator_name = emulator["name"]
	out_path = os.path.join(output_dir, "user_guide", "emulators", "emulator_list", f"{emulator_name}.rst")
	if not overwrite and exists(out_path):
		print(f"[{emulator_name}] Already exists, skipping...")
		continue

	output = f""".. image:: /global/assets/emulators/{emulator["name"]}.png
	:width: 25%

.. _emulator_{emulator_name}:

{emulator["fullname"]}
{'=' * len(emulator["fullname"])}

Notes
~~~~~

There are no special notes for this emulator. Games should work out of the box.

Supported systems
~~~~~~~~~~~~~~~~~"""
	for system_name in emulator_systems[emulator_name]:
		output += f"""
- :ref:`system_{system_name}`"""

	with open(out_path, "w") as f:
		f.writelines(output)
		print(f"[{emulator_name}] -> {out_path}")

print("Add this to index of systems:\n\"\"\"")
print(".. toctree::")
print("\t:maxdepth: 1\n")
for system in system_data:
	print(f"\tsystem_list/{system['name']}")
print("\"\"\"")

print("Add this to index of emulators:\n\"\"\"")
print(".. toctree::")
print("\t:maxdepth: 1\n")
for emulator in emulator_data:
	print(f"\temulator_list/{emulator['name']}")
print("\"\"\"")