



import scrapy

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    page_number = 1  
    start_urls = ['https://www.reed.co.uk/jobs/data-analyst-jobs']

    custom_settings = {
        'FEEDS': {
            'items.csv': {'format': 'csv'},
        }
    }

    def parse(self, response):
        
        if response.css('h2.job-card_jobResultHeading__title__IQ8iT a::attr(href)').get():
            # Extract detail URL of each job from the current page
            job_urls = response.css('h2.job-card_jobResultHeading__title__IQ8iT a::attr(href)').getall()
            for job_url in job_urls:
                absolute_job_url = 'https://www.reed.co.uk' + job_url
                yield scrapy.Request(absolute_job_url, callback=self.parse_job_details)

            # Pagination handling
            self.page_number += 1  
            next_page = f"https://www.reed.co.uk/jobs/data-analyst-jobs?pageno={self.page_number}"
            yield response.follow(next_page, callback=self.parse)
        else:
            # If it's a different format, handle it differently
            # Extracting detail URL of each job from the current page
            job_urls = response.css('a.job-title::attr(href)').getall()
            for job_url in job_urls:
                yield scrapy.Request(job_url, callback=self.parse_job_details)

    def parse_job_details(self, response):
        # Check the format (job listing page)
        if response.css('h2.job-card_jobResultHeading__title__IQ8iT a::attr(href)').get():
            # Extracting job details from the job detail page
            title = response.xpath('//div[contains(@class, "col-xs-12")]/h1/text()').get()

            
            #salary
            salary = response.xpath('//span[@itemprop="baseSalary"]/span/text()').get()
            salary = salary.strip() if salary else None  
            if not salary:
                salary = response.xpath('//span[@data-qa="salaryLbl"]/text()').get()
                salary = salary.strip() if salary else None
                
                if not salary:
                    salary = response.xpath('//span/meta[@itemprop="currency"][@content="GBP"]/following-sibling::span[@data-qa="salaryLbl"]/text()').get()
                    salary = salary.strip() if salary else None  
                    
                    if salary is not None:
                        salary = salary.strip()

            
            
            
            
              #contract-type      
            
            contract_type = response.xpath('//span[@data-qa="jobTypeMobileLbl"]/a[1]/text()').get()
            
            
            #job-type
            job_type = response.xpath('//span[@data-qa="jobTypeMobileLbl"]/a[2]/text()').get()

            # Extracting location
            location_elements = response.css('span[data-qa="localityMobileLbl"]')
            location = ''
            for element in location_elements:
                location += element.css('::text').get().strip() + ', '

            
            location = location.rstrip(', ')

            
            region = response.css('span[data-qa="regionMobileLbl"]::text').get()

            
            if region:
                if location:
                    location += ', ' + region
                else:
                    location = region

            job_details = {
                'Detail URL': response.url,
                'Title': title,
                'Salary': salary,
                'Contract Type': contract_type,
                'Job Type': job_type,
                'Location': location,
            }
            yield job_details
        else:
            # If it's a different format, extract details accordingly
            title = response.css('.col-xs-12 h1::text').get()
            
            salary = response.xpath('//span[@itemprop="baseSalary"]/span/text()').get()
            salary = salary.strip() if salary else None  # First attempt to extract salary
            
            if not salary:
                salary = response.css('span[data-qa="salaryLbl"]::text').get()
                salary = salary.strip() if salary else None  # Second attempt to extract salary
                
            if salary is not None:
                salary = salary.strip()
                

    
            contract_type = response.css('span[itemprop="employmentType"] a::text').get()
            
            job_type = response.xpath('//span[@itemprop="employmentType"]/a[2]/text()').get()
            job_type = job_type.strip()

            location_elements = response.css('span[itemprop="addressLocality"]')
            location = ''
            for element in location_elements:
                location += element.css('::text').get().strip() + ', '
            location = location.rstrip(', ')

            # Extracting secondary location from alternative HTML format
            secondary_location = response.css('span[data-qa="localityLbl"]::text').get()
            if secondary_location:
                location += ' ' + secondary_location.strip()

            job_details = {
                'Detail URL': response.url,
                'Title': title,
                'Salary': salary,
                'Contract Type': contract_type,
                'Job Type': job_type,
                'Location': location,
            }
            yield job_details













