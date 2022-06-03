# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import pathlib
import shutil

suffixes = ["pdf", "html"]
cwd = pathlib.Path.cwd()
for suffix in suffixes:
    dest = cwd / suffix
    dest.mkdir(exist_ok=True)
    for file in cwd.glob(f"*.{suffix}"):
        if "README" in file.name:
            continue
        if file.is_dir():
            continue
        shutil.move(file, dest / file.name)
