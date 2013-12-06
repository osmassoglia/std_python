# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup, SoupStrainer
from urlparse import urlparse


class std_web:
    def get_all_links(self, url, data):
        schemabase = urlparse(url);
        protocol    = schemabase[0]
        domain      = schemabase[1]
        
        soup = BeautifulSoup(data)
        links = {}
        for link in soup.findAll("a"):
            protocoli= protocol
            domaini = domain
            href = link.get('href')
            schema = urlparse(href);
            if schema[0]: 
                protocoli = schema[0]
                
            if  schema[1]: 
                domaini = schema[1]
            
            nhref = u'%s://%s%s' % (protocoli,domaini,schema[2])
            #print nhref
            tag = link.contents
            if links.has_key(nhref):
                links[href].append(tag)
            else:
                links.update({href:[]})
                links[href].append(tag)
        
        return links
            
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