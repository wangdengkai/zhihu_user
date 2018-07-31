# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request

from zhihu_user.items import ZhihuUserItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhidao'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    #开始用户
    start_user = "spto"
    #获取用户详细消息url
    user_url ="https://www.zhihu.com/api/v4/members/{user}?include={include}"
    #获取用户详细信息的的条件
    user_query = "allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"
    #获取关注了的url
    follows_url = "https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}"
    #获取关注了的验证
    follows_query ="data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"

    #获取关注了的url
    followers_url = "https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}"
    # 获取关注了的query
    followers_query = "data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"

    def start_requests(self):
        # url ="https://www.zhihu.com/api/v4/members/splitter/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20"

        yield  Request(self.user_url.format(user=self.start_user,include=self.user_query,callback=self.parse_user))
        yield  Request(self.follows_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),callback=self.parse_follows)
        yield  Request(self.followers_url.format(user=self.start_user,include=self.followers_query,offset=0,limit=20),callback=self.parse_followers)

    # def parse(self, response):
    #     print("-------------")
    #     print('--',response ,'000')
    #     print(response.text)
    #     print(response.url)
    def parse_user(self,response):
        '''
        因为返回的是json格式的数据，所以这里直接通过json.loads获取结果
        :param response:
        :return:
        '''
        print('------------',response.url)
        #将响应转化为字典
        result =json.loads(response.text)
        #实例化一个用户对象
        item=ZhihuUserItem()

        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)

        yield item

        yield Request(self.follows_url.format(user = result.get("url_token"),include=self.follows_query,offset=0,limit=20),callback=self.parse_follows)

        yield Request(self.followers_url.format(user = result.get("url_token"),include=self.followers_query,offset=0,limit=20),callback=self.parse_followers)

    def parse_follows(self,response):
        '''
        用户关注列表的解析，这里返回的也是json数据 这里有两个字段data和page，其中page是分页信息
        :param response:
        :return:
        '''
        results =json.loads(response.text)
        print('results----',results)
        #获取所有关注信息
        if 'data' in results.keys():
            for result in results.get('data'):
                yield  Request(self.user_url.format(user = result.get("url_token"),include=self.user_query),callback=self.parse_user)
        #获取下一页信息
        if 'paging' in results.keys():
            if results['paging']['is_end'] == False:
                next_page = results.get('paging').get('next')

                yield Request(next_page,self.parse_follows)


    def parse_followers(self,response):
        '''
        这里其实和关乎列表的处理方法是一样的
        用户粉丝列表的解析，这里返回的也是json数据 这里有两个字段data和page，其中page是分页信息
        :param response:
        :return:
        '''

        results = json.loads(response.text)
        print('results-===',results)
        #H获取粉丝xinxi
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user = result.get("url_token"),include=self.user_query),callback=self.parse_user)

        if 'paging' in results.keys():
            if results['paging']['is_end'] == False:
                next_page = results.get('paging').get('next')

                yield Request(next_page,self.parse_follows)