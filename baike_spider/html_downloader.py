# conding:utf8
from urllib import request
import http.cookiejar
class HtmlDownloader(object):


    def download(self, new_url):
        if new_url is None:
            return
        req = request.Request(new_url)
        req.add_header('user-agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        response = request.urlopen(req)
        if response.getcode() != 200:#200 就是成功
            return None
        return response.read()