import json
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from celery import shared_task

from .mongodb.connect import db


@shared_task
def work_process(search_list):
    print('------------ work_process -----------')
    data_to_insert = scraping(search_list)
    print(data_to_insert)

    if len(data_to_insert) > 0:
        db.moskali.insert_many(data_to_insert)


def scraping(date_list: list) -> list:
    url = 'https://index.minfin.com.ua/ua/russian-invading/casualties/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select_one('ul[class=see-also] > li[class=gold]')

    result = []

    for current_date in date_list:
        result_date = {}
        result_date.update({"date": datetime.strptime(current_date, "%d.%m.%Y").isoformat()})
        try:
            losses = content.find('span', attrs={"class": "black"}, text=current_date).parent \
                .find('div', attrs={"class": "casualties"}).find('div').find('ul')
        except AttributeError as err:
            print(f'Error for {err}')
            continue

        for l in losses:
            title, quantity = l.text.split("—")
            title = title.strip()
            quantity = re.search(r"\d+", quantity).group()
            result_date.update({title: int(quantity)})
        result.append(result_date)
    return result
