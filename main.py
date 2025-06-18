from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                          options=options)
driver.get("https://ecos.bok.or.kr/#/SearchStat")
driver.maximize_window()

print("Wating to load wesite")
time.sleep(10)

# Wait for the "English" button to be clickable and click it
try:
    english_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'langChange') and contains(text(), 'English')]"))
    )
    english_button.click()
    print("✅ Clicked the 'English' button.")
except Exception as e:
    print("❌ Failed to find or click the 'English' button:", e)

time.sleep(10)



try:
    
    # Now wait for the child element to be visible and clickable
    time.sleep(15)
    child1 = driver.find_element(By.XPATH, "//span[contains(text(), '2.1. National Income and Product')]")
    child1.click()
    print("✅ Clicked '2.1. National Income and Product'")

    time.sleep(15)
    child2 = driver.find_element(By.XPATH, "//span[contains(text(), '2.1.1. Main Indicators of National Accounts')]")
    child2.click()
    print("✅ Clicked '2.1.1. Main Indicators of National Accounts'")

    time.sleep(15)
    child3 = driver.find_element(By.XPATH, "//span[contains(text(), '2.1.1.1. Main Annual Indicators (reference year 2020)')]")
    child3.click()
    print("✅ Clicked '2.1.1.1. Main Annual Indicators (reference year 2020)")
    
    time.sleep(15)
    addToList = driver.find_element(By.XPATH, "//div[@class='content-box-foot']//button[text()='Add to List']")
    addToList.click()
    print("✅ Add to List")

    time.sleep(15)
    viewList = driver.find_element(By.XPATH, "//div[@class='content-box-foot']//button[text()='View List']")
    viewList.click()
    print("✅ View List")

    time.sleep(20)
    original_data_btn = driver.find_element(By.XPATH, "//div[@class='input-box-group']//button[text()='Original Data Download']")
    original_data_btn.click()
    print("✅ Clicked 'Original Data Download'")


    time.sleep(20)
    download_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-popup') and text()='Download']")
    download_button.click()
    print("✅ Clicked 'Download' button.")

except Exception as e:
    print("❌ Failed to click '2. National Accounts':", e)