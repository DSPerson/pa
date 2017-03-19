# coding:utf8
#解析器
from bs4 import BeautifulSoup
import re
import urllib.parse
class HtmlParser(object):


    def _get_new_url(self, page_url, soup, is_full):
        links = soup.find_all('a', href=re.compile(r'-chapter-'))
        if len(links) == 0:
            print('匹配失败')
            return
        new_urls = set()
        for link in links:
            new_url = link['href']
            if is_full:
                new_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_url)
        return new_urls


        pass

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        #https://hellotranslations.wordpress.com/2015/01/30/dou-po-cang-qiong-chapter-1/
        title = soup.find_all('div', class_='collapseomatic_content')
        res_data['title'] = title.get_text()
        summry_node = soup.find('div', itemprop='articleBody').find_all('p')
        if len(summry_node) > 2:
            summry_node = summry_node[1].get_text()
        res_data['summary'] = summry_node

        with open('') as f:
            f.read()
        return res_data


    def parse(self, page_url, html_cont, is_full):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='ut-8')
        new_urls = self._get_new_url(page_url, soup, is_full)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data