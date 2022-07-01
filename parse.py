import time
from threading import Thread
import re
import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/news/"


def start_request():
    glob_mass = [[], [], [], [], [], [], [], [], [], [], []]
    headers = {'User-agent': 'your bot 0.1'}
    response = requests.get(url=url, headers=headers)
    print(response.status_code)

    if response.status_code == 200:
        content = response.content

        text = BeautifulSoup(response.text, 'lxml')

        title = text.find_all('a', class_="tm-article-snippet__title-link")
        img = text.find_all('img', class_="tm-article-snippet__lead-image")
        description = text.find_all('div',
                                    class_="article-formatted-body article-formatted-body article-formatted-body_version-2")

        index = 0
        for i_title in title:
            title_text = re.sub('<[^>]+>', '', str(i_title))
            title_a = (str(i_title).split('"'))[5]

            glob_mass[index].append(title_text)
            glob_mass[index].append(title_a)

            if index == 9:
                break
            index += 1

        index = 0
        for i_img in img:
            img_a = (str(i_img).split('"'))[3]

            glob_mass[index].append(img_a)

            if index == 9:
                break
            index += 1

        index = 0
        for i_description in description:
            description_text = re.sub('<[^>]+>', '', str(i_description))

            glob_mass[index].append(description_text)

            if index == 9:
                break
            index += 1
        return glob_mass

print(start_request())