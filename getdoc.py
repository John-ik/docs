from bs4 import BeautifulSoup as bs
import requests
import sys

# url = 'https://en.cppreference.com/w/cpp/header'
# r = requests.get(url)

# soup = bs(r.text, "html.parser")

# --------------------------------------------------

# all_td = soup.find_all("tr", class_="t-dsc")
# with open("output.txt", "w") as f:
#     for td in all_td:
#         a = td.find('a')
#         href = a.get('href')
#         f.write(href + "\n")

# --------------------------------------------------


site = 'https://en.cppreference.com/w/cpp/'
p = sys.argv[1]
r = requests.get(site+p)
soup = bs(r.text, "html.parser")

head_bs = soup.find("head")
head_bs.clear()

print(soup, file=open("out.md", "w"))


        # f.write(href + "\n")
