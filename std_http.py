# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen, URLError
import httplib2


class std_http:
    
    def check_url(self, url):
        req = Request(url)
        try:
            response = urlopen(req)
        except URLError, e:
            if hasattr(e, 'reason'):
                return False
            
            elif hasattr(e, 'code'):
                return False
        else:
            return True
    def get_page(self, url):
        http = httplib2.Http()
        status, response = http.request(url)        
        return [status, response]

    def normalize_url(self,url):
        return quote(url, safe="%/:=&?~#+!$,;'@()*[]")
