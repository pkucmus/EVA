import os
import sys
import shutil
import shlex
import subprocess
import time
import re
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


FILE_INDEX_PATTERN = re.compile(r"^.*\((?P<index>\d+)\).*$")

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
DOWNLOADS_PATH = os.path.abspath(os.path.join(Path.home(), "Downloads"))

mime_types = [
    "image/png",
]

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 1)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", ",".join(mime_types))

driver = webdriver.Firefox(firefox_profile=profile)

driver.get(sys.argv[1])

try:
    while True:
        assembly_name = input("Provide `name` and hit enter...: ")
        input("Set the starting view and hit enter...")

        body = driver.find_element_by_tag_name("body")

        repeats = int(360 / 15)
        # repeats = int(360 / 5)

        body.send_keys(Keys.ARROW_LEFT)
        # body.send_keys(Keys.SHIFT, Keys.ARROW_LEFT)
        body.send_keys(Keys.SPACE)
        time.sleep(1)

        for i in range(0, repeats):
            body.find_element_by_css_selector("[command-id=triggerPrint]").click()
            body.find_element_by_css_selector(
                "[label=Landscape][value=Landscape]"
            ).click()
            body.find_element_by_css_selector(".os-button.os-download-image").click()
            body.send_keys(Keys.ARROW_RIGHT)
            # body.send_keys(Keys.SHIFT, Keys.ARROW_RIGHT)
            time.sleep(1)

        paths = sorted(Path(DOWNLOADS_PATH).iterdir(), key=os.path.getmtime)

        base, ext = os.path.splitext(paths[-repeats])

        shutil.move(paths[-repeats], f"{base}({repeats}){ext}")
        paths = sorted(Path(DOWNLOADS_PATH).iterdir(), key=os.path.getmtime)

        assembly_dir = os.path.join(DOWNLOADS_PATH, assembly_name)
        shutil.rmtree(assembly_dir, ignore_errors=True)
        os.mkdir(assembly_dir)
        for file_path in paths[-repeats:]:
            match = FILE_INDEX_PATTERN.match(os.path.split(file_path)[1])
            index = match.group("index")
            new_path = os.path.join(assembly_dir, f"{assembly_name}_{index}.jpg")
            subprocess.call(
                shlex.split(
                    f"convert '{file_path}' -resize 1000x773 -background white -alpha remove -quality 90 '{new_path}'"
                )
            )
            os.remove(file_path)

        shutil.rmtree(
            os.path.join(
                BASE_PATH, "assets", "images", "gifs", "source", assembly_name
            ),
            ignore_errors=True,
        )
        shutil.move(
            assembly_dir, os.path.join(BASE_PATH, "assets", "images", "gifs", "source")
        )
except KeyboardInterrupt:
    driver.quit()
