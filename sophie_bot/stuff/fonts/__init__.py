# Copyright (C) 2019 The Raphielscape Company LLC.
# Copyright (C) 2018 - 2019 MrYacha
#
# This file is part of SophieBot.
#
# SophieBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.


def list_all_fonts():
	from os.path import dirname, basename, isfile
	import glob

	mod_paths = glob.glob(dirname(__file__) + "/*.ttf")
	return [
		dirname(f) + '/' + basename(f)
		for f in mod_paths
		if isfile(f) and f.endswith(".ttf")
	]


ALL_FONTS = sorted(list_all_fonts())
__all__ = ALL_FONTS + ["ALL_FONTS"]
