from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                          options=options)

driver.get("https://www.ecb.europa.eu/press/pubbydate/html/index.en.html?name_of_publication=Speech&boardmember=Christine%20Lagarde")
driver.maximize_window()

print("Wating to load wesite")
time.sleep(10)

# Scroll to load all dynamic content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for loading
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Once fully loaded, parse the content
soup = BeautifulSoup(driver.page_source, 'html.parser')
entries = []

# Get the top-level <dl> only
main_dl = soup.find('dl')

# Loop through top-level <dt> and <dd> pairs only
for tag in main_dl.find_all(['dt', 'dd'], recursive=False):
    if tag.name == 'dt':
        current_dt = tag.text.strip()
    elif tag.name == 'dd':
        title_div = tag.find('div', class_='title')
        speech_title = title_div.get_text(strip=True) if title_div else None
        link_tag = title_div.find('a') if title_div else None
        href = link_tag['href'] if link_tag else None
        full_url = f"https://www.ecb.europa.eu{href}" if href else None

        entries.append({
            "date_or_term": current_dt,
            "speech_title": speech_title,
            "url": full_url
        })

driver.quit()


df = pd.DataFrame(entries)
print(df.head())
df.to_csv('ecb_speeches.csv', index=False)
