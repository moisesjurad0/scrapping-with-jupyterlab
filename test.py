import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# driver2 = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
