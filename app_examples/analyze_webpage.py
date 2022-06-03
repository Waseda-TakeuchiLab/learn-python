# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import requests
import bs4

keywords = ["Ga", "量子ドット"]
url_base = "https://confit.atlas.jp"
programs = {
    "2021年 第82回応用物理学会秋季学術講演会（オンライン）": url_base + "/guide/event/jsap2021a/class",
    "2021年 第68回応用物理学会春季学術講演会（オンライン）": url_base + "/guide/event/jsap2021s/class",
}


headers = {"Accept-Language": "ja"}
for program, url in programs.items():
    print(program)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    dl_tag = soup.find("dl", attrs={"class": "cmn-dl"})
    if dl_tag is None:
        continue
    session_urls = [
        url_base + tag.get("href") for tag in dl_tag.find_all("a")
        if isinstance(tag, bs4.Tag)
    ]
    for session_url in session_urls:
        _response = requests.get(session_url, headers=headers)
        _response.raise_for_status()
        _soup = bs4.BeautifulSoup(_response.content, "html.parser")
        title_tags = [
            tag.find("a") for tag in _soup.find_all("h1", attrs={"title": "講演名"})
            if isinstance(tag, bs4.Tag)
        ]
        for tag in title_tags:
            if all((keyword in tag.text) for keyword in keywords):
                print(tag.text)
                print(url_base + tag.get("href"))
    print()
