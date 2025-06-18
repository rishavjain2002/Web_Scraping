from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

urls = [
    "https://www.sherwin-williams.com/homeowners/products/duration-home-interior-acrylic-latex",
    "https://www.sherwin-williams.com/homeowners/products/emerald-urethane-trim-enamel",

    # Add more URLs as needed
]

# List to store data
data = []

for url in urls:
    print(f"\nProcessing: {url}")
    driver.get(url)
    time.sleep(5)

    # Make dropdown visible (optional depending on page)
    dropdown_id = "attrValue_ATT_calc_size__volume_or_weight_+_item_"
    try:
        driver.execute_script(f'document.getElementById("{dropdown_id}").style.display = "block";')
        time.sleep(2)
        select_element = Select(driver.find_element(By.ID, dropdown_id))
        select_element.select_by_visible_text("5 Gallon")
        print("Selected '5 Gallon'")
        time.sleep(5)  # wait for price to update
    except Exception as e:
        print(f"Dropdown not found or couldn't select '5 Gallon': {e}")

    # Extract product name and price
    try:
        name = driver.find_element(By.CSS_SELECTOR, "h2.pdp__title").text.strip()
    except:
        name = "N/A"

    try:
        price = driver.find_element(By.CSS_SELECTOR, 'div[itemprop="price"]').text.strip()
    except:
        price = "N/A"

    print(f"Name: {name}, Price: {price}")
    data.append({"URL": url, "Product Name": name, "Price": price})

# Close the browser
driver.quit()

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("products_5Gallons.csv", index=False)
print("\nData saved to 'products.csv'")
