import scrapy
from scrapyscript import Job, Processor

processor = Processor(settings=None)


class PythonSpider(scrapy.spiders.Spider):
    name = "myspider"

    def start_requests(self):
        yield scrapy.Request(self.url)

    def parse(self, response):
        data = response.xpath("//title/text()").extract_first()
        return {'title': data}


job = Job(PythonSpider, url="http://www.python.org")
results = processor.run(job)

print(results)
