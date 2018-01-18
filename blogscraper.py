import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog_spider'
    start_urls = ['http://www.designsbyarose.com/?cat=65']

    def parse(self, response):
        BLOG_SELECTOR = '//body/div'
        for blog in response.xpath(BLOG_SELECTOR):

            TITLE_SELECTOR = '//h2/a/text()'
            DATE_SELECTOR = '//div[@class="post-info"]/span[@class="date published time"][1]/text()'
            AUTHOR_SELECTOR = '//div/span/span/a/text()'
           
            yield {
                'title': blog.xpath(TITLE_SELECTOR).extract(),
                'date': blog.xpath(DATE_SELECTOR).extract(),
                'author': blog.xpath(AUTHOR_SELECTOR).extract(),
            
            }

