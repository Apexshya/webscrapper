import scrapy

class JobItem(scrapy.Item):
    detail_url = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    contract_type = scrapy.Field()
    job_type = scrapy.Field()
    location = scrapy.Field()
    
    
    
    # scrapy crawl job_spider -o items.csv
