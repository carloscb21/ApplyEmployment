from flask import Flask
from selenium import webdriver
from pathlib import Path
from utils.broswer_options import get_basic_setup

browser_setup = get_basic_setup()
options = browser_setup.options
# web_home_path = browser_setup.web_home_path
driver_path = browser_setup.driver_path

application = Flask(__name__, static_url_path="")

with application.app_context():
    driver = webdriver.Chrome(executable_path=str(Path().absolute()) + driver_path, options=options)
    server_status = ""




