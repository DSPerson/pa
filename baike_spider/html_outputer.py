# conding:utf8
class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.data.append(new_data)

        pass


    def output_html(self):
        print(self.data)
        pass
        # fout = open('output.html', 'w+')
        # fout.write('<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>')
        #
        # fout.write('<html>')
        # fout.write('<body>')
        # fout.write('<table>')
        # for data in self.data:
        #     fout.write('<tr>')
        #     fout.write("<td> %s </td>" % (data['url']))
        #     fout.write("<td> %s </td>" % (data['title'].encode('utf-8')))
        #     #fout.write("<td> %s </td>" % (data['summary'].encode('utf-8')))
        #     fout.write('</tr>')
        #
        # fout.write('</table>')
        # fout.write('</body>')
        # fout.write('</html>')
