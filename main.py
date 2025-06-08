from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_etslips():
    options = Options()
    options.headless = True
    service = Service('./chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.etslips.co.uk")
    time.sleep(5)

    # HTML class and tag names
    table = driver.find_element(By.CLASS_NAME, "ui.small.selectable.single.line.striped.unstackable.compact.table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    results = []
    # Skip header
    for row in rows[1:]:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 6:
            results.append({
                "time": cols[0].text,
                "race_number": cols[1].text,
                "name": cols[2].text,
                "reaction_time": cols[3].text,
                "elapsed_time": cols[4].text,
                "mph": cols[5].text,
            })

    driver.quit()
    return results

if __name__ == "__main__":
    data = scrape_etslips()
    for entry in data:
        print(entry)
