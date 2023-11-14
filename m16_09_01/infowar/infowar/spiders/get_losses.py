import json
import re
from datetime import datetime

import scrapy


def get_next_link():
    with open('links.json', 'r', encoding='utf-8') as fd:
        result = json.load(fd)
    return [link.get('href') for link in result]


class GetLossesSpider(scrapy.Spider):
    name = "get_losses"
    allowed_domains = ["index.minfin.com.ua"]
    start_urls = ["https://index.minfin.com.ua/ua/russian-invading/casualties"]

    def parse(self, response, **kwargs):
        content = response.css('ul[class=see-also] li[class=gold]')
        parse_elements = {}

        for li in content:
            date_key = li.xpath('span/text()').get()
            try:
                date_key = datetime.strptime(date_key, "%d.%m.%Y").isoformat()
            except ValueError:
                print(f"Error for {date_key}")
                continue
            parse_elements.update({"date": date_key})

            casualties = li.xpath('div/div/ul/li')

            for casual in casualties:
                # casual.css('*::text').extract()
                name, quantity, *_ = ''.join(casual.css('*::text').extract()).split("—")
                name = name.strip()
                quantity = re.search(r"\d+", quantity).group()
                parse_elements.update({name: quantity})

            yield parse_elements

        for next_link in get_next_link():
            yield scrapy.Request(self.start_urls[0] + next_link, method='GET')
