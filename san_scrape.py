import requests
from bs4 import BeautifulSoup

URL = 'https://www.sanforce-tech.com/emergency-drivers/energy-saving/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_="grid-container")
print(results.prettify())