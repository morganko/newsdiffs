from baseparser import BaseParser
from BeautifulSoup import BeautifulSoup
from datetime import datetime

DATE_FORMAT = '%B %d, %Y at %l:%M%P EDT'

class ElyseeParser(BaseParser):
    domains = ['wwww.elysee.fr/']

    feeder_pages = ['http://www.elysee.fr/toutes-les-actualites/']
    feeder_pat  = '^http://www.elysee.fr[a-zA-Z-]+/article/[a-zA-Z0-9-]+/$'

    def _parse(self, html):
        soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES, fromEncoding='utf-8')

        try:
            p_tags = soup.find('div', attrs={'class':'desc post-content'}).findAll('p')
        except AttributeError:
            self.real_article = False
            return

        main_body = '\n'.join([p.getText() for p in p_tags])

        self.body = main_body

        self.meta = soup.findAll('meta')

        self.title = soup.find('meta', attrs={'property':'og:title'}).get('content')

#        author = soup.find('meta', attrs={'name':'author'}).get('content')
#        print(author)
        author = ''       
        
        if author:
            self.byline = author.getText()
        else:
            self.byline = ''

        datestr = soup.find('p', attrs={'class':'date'})#.get_text()
        
        print(datestr)
#        new_dt = datestr[:10]
#        datet = datetime.strptime(new_dt, '%Y-%m-%dT%H:%M:%S')
#        self.date = datet.strftime(DATE_FORMAT)

        self.date = "2006/11/03"
        


