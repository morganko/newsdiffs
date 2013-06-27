from baseparser import BaseParser
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import re

DATE_FORMAT = '%B %d, %Y at %l:%M%P EDT'
MONTH = {'Janvier':1,u'F\xe9vrier':2,'Mars':3,'Avril':4,'Mai':4,'Juin':6,'Juillet':7,u'Ao\xfbt':8,'Septembre':9,'Octobre':10,'Novembre':11,u'D\xe9cembre':12}

class ElyseeParser(BaseParser):
    domains = ['wwww.elysee.fr']

    feeder_pages = ['http://www.elysee.fr/toutes-les-actualites/']
    feeder_pat  = '^http://www.elysee.fr/[a-zA-Z-]+/article/[a-zA-Z0-9-]+/$'

    def _parse(self, html):
        soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES, fromEncoding='utf-8')

        try:
           p_tags = soup.find('div', attrs={'id':re.compile(r"^listen-content-[0-9]+$")}).findAll('p')
        except AttributeError:
            self.real_article = False
            return

        main_body = '\n'.join([p.getText() for p in p_tags])

        self.body = main_body

        self.meta = soup.findAll('meta')

        self.title = soup.find('meta', attrs={'property':'og:title'}).get('content')

        author = soup.find('meta', attrs={'name':'author'}).get('content')
        
        self.byline = author
        datestr = soup.find('p', attrs={'class':'date'}).getText()
        tmp=datestr.split(' ')
        new_dt=str(tmp[4])+'-'+str(MONTH[tmp[3]])+'-'+str(tmp[2])
        datet = datetime.strptime(new_dt, '%Y-%m-%d')
        self.date = datet.strftime(DATE_FORMAT)

