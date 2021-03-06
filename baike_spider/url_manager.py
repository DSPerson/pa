# conding:utf8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


        pass

    #像管理器添加新的url
    def add_new_url(self, root_url):
        if root_url is None:
            return
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)


    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0


    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url



