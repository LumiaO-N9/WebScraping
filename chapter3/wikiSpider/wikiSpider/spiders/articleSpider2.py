from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import WikispiderItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class ArticleSpider(CrawlSpider):
    name = "article2"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        "http://en.wikipedia.org/wiki/Python_%28programming_language%29"
    ]
    rules = [
        Rule(
            LxmlLinkExtractor(allow=('(/wiki/)((?!:).)*$')),
            callback="parse_item",
            follow=True)
    ]

    def parse_item(self, response):
        item = WikispiderItem()
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is :' + title)
        item['title'] = title
        return item
