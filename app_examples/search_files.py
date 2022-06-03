# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import pathlib

dirctory = pathlib.Path.cwd()
suffix = ".py"


for file in dirctory.glob(f"**/*{suffix}"):
    print(file)
