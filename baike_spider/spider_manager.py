# coding:utf-8
from baike_spider import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        try:
            self.urls.add_new_url(root_url)
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print('cunnent is ', count, 'craw', '网址', new_url)
                html_cont = self.downloader.download(new_url)  # 页面数据
                new_urls, new_data = self.parser.parse(new_url, html_cont, False)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
                if count == 1:
                    break
        except:
            print('craw failed')

        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'https://hellotranslations.wordpress.com/2015/01/30/dou-po-cang-qiong-chapter-1/'
    #root_url = 'https://www.baidu.com'
    objc_spider = SpiderMain()
    objc_spider.craw(root_url)
