# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import pathlib
import shutil

directory = pathlib.Path.cwd() / "data"

shutil.make_archive(directory.name, format="zip", root_dir=directory)
