from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.collegevine.com/schools/best-colleges-for-computer-science'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

with open ('collegevine.csv', 'w', encoding="utf8", newline='') as file:
    writer = writer(file)
    header = ['Rank', 'School name']
    writer.writerow(header) 
    colleges = soup.find_all('div', class_="t--column-Name")
    for college in colleges:
        name = college.find('a', class_="text-primary").text
        rank = college.find('div', class_="t--ranking-badge-computer-science").text
        info = [rank, name]
        writer.writerow(info)