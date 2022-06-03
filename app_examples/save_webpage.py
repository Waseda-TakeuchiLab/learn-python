# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import pathlib
import requests


savedir = pathlib.Path.cwd() / "webpages"
urls = []


savedir.mkdir(parents=True, exist_ok=True)
for url in urls:
    response = requests.get(url)
    response.raise_for_status()
    filename = response.url.split("/")[-1]
    with open(savedir / filename, mode="wb") as f:
        f.write(response.content)
