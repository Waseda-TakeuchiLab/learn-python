# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import selenium.webdriver as wd
from selenium.webdriver.common import by, keys
from selenium.common import exceptions
import chromedriver_binary  # noqa

query = "waseda university"


options = wd.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--headless")
driver = wd.Chrome(options=options)
driver.implicitly_wait(1)
try:
    driver.get("https://google.com")
    search_box = driver.find_element(by.By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(keys.Keys.RETURN)
    search = driver.find_element(by.By.ID, "search")
    for a in search.find_elements(by.By.TAG_NAME, "a"):
        try:
            h3 = a.find_element(by.By.TAG_NAME, "h3")
            print(h3.text, a.get_attribute("href"))
        except exceptions.NoSuchElementException:
            continue
finally:
    driver.quit()
