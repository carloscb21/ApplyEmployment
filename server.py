from flask import Flask
from selenium import webdriver
from utils import properties
from pathlib import Path

application = Flask(__name__, static_url_path="")

with application.app_context():
    driver = webdriver.Chrome(executable_path=str(Path().absolute())+properties.DRIVER_PATH)
    server_status = ""




