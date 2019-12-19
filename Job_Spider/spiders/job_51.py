# -*- coding: utf-8 -*-
import scrapy
from Job_Spider.items import Job51Item
from Job_Spider.data_url.url_list import url_list


class Job51Spider(scrapy.Spider):
    name = 'job_51'
    allowed_domains = ['m.51job.com', 'msearch.51job.com']
    start_urls = url_list

    def parse(self, response):
        url_list = response.xpath('//div[@class="items"]/a/@href').getall()
        if url_list:
            for url in url_list:
                yield scrapy.Request(url, callback=self.parse_detail)
        
        next_url = response.xpath('//div[@class="paging"]/a[@class="next"]/@href').get()
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        # item = Job51Item()
        url = response.request.url
        job_name = response.xpath('//div[@class="jt"]/p/text()').get()
        job_release_date = response.xpath('//div[@class="jt"]/span/text()').get()
        job_location = response.xpath('//div[@class="jt"]/em/text()').get()
        job_wage = response.xpath('//p[@class="jp"]/text()').get()
        job_tag = response.xpath('//div[@class="jd"]/span/text()').getall()
        company_name = response.xpath('//p[@class="c_444"]/text()').get()
        company_tag = response.xpath('//div[@class="at"]/text()').get()
        job_description_tag = response.xpath('//div[@class="welfare"]/span/text()').getall()
        work_place = response.xpath('//a[@class="arr a2"]/span/text()').get()
        item = dict(url=url, 
                    job_name=job_name, 
                    job_release_date=job_release_date, 
                    job_location=job_location,
                    job_wage = job_wage,
                    job_tag = ' | '.join(job_tag),
                    company_name = company_name,
                    company_tag = company_tag,
                    job_description_tag = ' | '.join(job_description_tag),
                    work_place = work_place
                    )
        yield item
