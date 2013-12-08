# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup, SoupStrainer
from urlparse import urlparse


class std_web:
    
    
    def __init__(self, main):
        self.parent = main
    
    def parse_url(self, url):
        schema = urlparse(url);
        return schema
    
    def get_all_links(self, url, data):
        
        protocol    = self.parent.protocol
        domain      = self.parent.domain
        
        soup = BeautifulSoup(data)
        links = {}
        for link in soup.findAll("a"):
            href = link.get('href')                 
            info = self.process_url(href)
            if info:
                if len(link.contents):
                    tag = link.contents[0]
                    if links.has_key(info['realpath']):
                        links[info['realpath']]['tags'].append(tag)
                    else:
                        links.update({info['realpath']:{'tags':[],'info':info}})
                        links[info['realpath']]['tags'].append(tag)
        
        return links
    
    def process_url(self, url):        
        protocol    = self.parent.protocol
        domain      = self.parent.domain     
        try:
            schema = urlparse(url);
            protocoli = protocol
            if schema[0]: 
                  protocoli = schema[0]
                    
            domaini = domain        
            if  schema[1]: 
                   domaini = schema[1]
            path = "/";
            if schema[2]:
                   path =  schema[2]      
            type=1
            
            if domain <> domaini:
                type=2
            
            nhref = u'%s://%s%s' % (protocoli, domaini, path)
            info = {'ptr': protocoli, 'dom': domaini, 'path': path,'type': type, 'realpath':nhref}
            return info;            
        except AttributeError:
            print "error parsin ", AttributeError , " " ,url  
            

            
    def get_all_headers(self, data):
        soup = BeautifulSoup(data)
        headers = {'h1':[],'h2':[],'h3':[],'h4':[],'h5':[]};
        for header in soup.findAll("h1"):
            headers['h1'].append(header.contents) 
        
        for header in soup.findAll("h2"):
             headers['h2'].append(header.contents) 
        
        for header in soup.findAll("h3"):
             headers['h3'].append(header.contents) 
    
        for header in soup.findAll("h4"):
             headers['h4'].append(header.contents) 
            
        for header in soup.findAll("h5"):
             headers['h5'].append(header.contents) 
             
        return headers

    def get_all_images(self, data):
        soup = BeautifulSoup(data)
        images = [];
        for image in soup.findAll("img"):
            images.append(image.contents) 
        
   
        return images            