from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_columns', None)

browser = webdriver.Chrome('./chromedriver.exe')
url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1"
browser.get(url)
time.sleep(2)
accept_button = browser.find_element_by_id("onetrust-accept-btn-handler")
time.sleep(1)
accept_button.click()
time.sleep(2)
browser.find_element_by_css_selector(".stats-table-pagination__select:nth-child(1) option").click()
time.sleep(2)
soup = BeautifulSoup(browser.page_source, "html.parser")
headers = soup.select(".nba-stat-table__overflow table thead tr:nth-child(1)")
rows_soup = soup.select(".nba-stat-table__overflow table tbody tr")
columns = ['ID']
columns.extend([col.get_text(strip=True) for col in headers[0] if col.get_text(strip=True) != ""])

# df = pd.DataFrame([], columns=columns)
# for i in range(len(rows)):
# df.append([x.get_text(strip=True) for x in rows[i] if x.get_text(strip=True) != ""])
# print([x.get_text(strip=True) for x in rows[i] if x.get_text(strip=True) != ""])
# print(df)
rows = []
for i in range(len(rows_soup)):
    rows.append([x.get_text(strip=True) for x in rows_soup[i] if x.get_text(strip=True) != ""])
    # print([x.get_text(strip=True) for x in rows[i] if x.get_text(strip=True) != ""])

with open('stats.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for row in rows:
        writer.writerow(row)
