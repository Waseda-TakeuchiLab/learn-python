# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import pathlib
import shutil

directory = pathlib.Path("//192.168.0.10/disk/references")
destination = pathlib.Path.cwd() / "dest"
keywords = ["In", "量子ドット"]


def main() -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for file in directory.glob("**/*"):
        if file.is_dir():
            continue
        if all((keyword in file.name) for keyword in keywords):
            shutil.copy(file, destination)


if __name__ == "__main__":
    main()
