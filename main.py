from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
fileno = 0
query = "Asus+laptop" # Change this query according to your choice 
url=f'https://www.amazon.in/s?k={query}&crid=GFI49IGY21O8&sprefix=asus+laptop%2Caps%2C356&ref=nb_sb_noss_1'
driver.get(url)
driver.maximize_window()

try:
    boxes = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    for box in boxes:
        d = box.get_attribute("outerHTML")
        with open(f"details/{query}_{fileno}.html", "w", encoding="utf-8") as f:
            f.write(d)
            fileno +=1

        # print(d)
except Exception as e:
    print(e)

time.sleep(3)
driver.close()

