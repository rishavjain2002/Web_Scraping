import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Go to the page (to set cookies, headers, etc.)
driver.get("https://www.anytimefitness.co.in/find-gym/")

# Use JavaScript to fetch the API data in the browser context
api_url = "https://www.anytimefitness.co.in/wp-json/anytime/v1/map-locations"
script = f"""
    return fetch("{api_url}")
        .then(response => response.json())
        .then(data => JSON.stringify(data));
"""
data_json = driver.execute_script(script)

data = json.loads(data_json)
print(data)

driver.quit()
