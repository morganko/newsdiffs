from baseparser import BaseParser
from BeautifulSoup import BeautifulSoup
from datetime import datetime

DATE_FORMAT = '%B %d, %Y at %l:%M%P EDT'

class Rue89Parser(BaseParser):
    domains = ['www.rue89.com']

    feeder_pages = ['http://www.rue89.com/']
#    feeder_pat  = '^http://www.rue89.com/\d{4}/\d{2}/\d{2}/[a-zA-Z0-9-]+$'
#    feeder_pat  = '^http://www.rue89.com/'
    feeder_pat  = ''
    def _parse(self, html):
        soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES, fromEncoding='utf-8')

        try:
            p_tags = soup.find('div', attrs={'id':'article'}).findAll('p')
        except AttributeError:
            self.real_article = False
            return

        main_body = '\n'.join([p.getText() for p in p_tags])

        self.body = main_body

        self.meta = soup.findAll('meta')

        self.title = soup.find('meta', attrs={'itemprop':'name'}).get('content')
        
        author = soup.find('a', attrs={'class':'author'}).getText()
        
        if author:
            self.byline = author.getText()
        else:
            self.byline = ''

        datestr = soup.find('span', attrs={'class':'date'}).get('datetime')
#        new_dt = datestr[:19]
#        datet = datetime.strptime(new_dt, '%Y-%m-%dT%H:%M:%S')
#        self.date = datet.strftime(DATE_FORMAT)
        self.date = 21/03/2013       


