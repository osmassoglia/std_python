# -*- coding: utf-8 -*-
import sys
import MySQLdb as dbapi
 

class std_db:
    def __init__(self):
        self.link          = "";
        self.linkDict     = "";
        self.db             = "";
        self.resources      = "";
        self.params         = {'host':'127.0.0.1', 'charset':'utf8', 'port':3306, 'use_unicode':True};
    
    def selectDb(self, name):
        try:
            self.db.select_db(name)
            return True;
        except:
            print 'Cannot select the database %s ' % name
            return False
 
    
    def tableExist(self, table):
        try:
            return self.execute('show tables like "%s";' % table)
            
        except:
            return False;
            
    def _getParams(self):
        
        return self.params;
    
    def setParams(self, args = False):
        
        for d in args:
            self.params[d] = args[d]
    
    def connect(self):
        args              = self._getParams();
        self.db          = dbapi.connect(host = args['host'], user = args['user'], passwd = args['passwd'], charset = args['charset'], port = args['port'], use_unicode = args['use_unicode'])
        self.link          = self.db.cursor()


    def commit(self):
        link = self._getLink();
        if link:
            link.execute('commit;')
            
    
    def last_insert_id(self):
        self.execute('select last_insert_id() as id')
        return self.fetchOne()[0]
    
    def execute(self, query, args = {}):
        link = self._getLink();
        if link:
            try:
                self.resources = link.execute(query, args);
                if self.resources:
                    return True;
                else:
                    self.resources = False;
                    return False;            
                
            except:
                print 'Execute get an error, Please check the SQL : %s ' % (query % self.db.literal(args));
    ##            print 'Error %s %s %s' % (RuntimeError.value, TypeError, NameError)
                return False;

            
    def fetchOne(self):
        link = self._getLink();
        if self.resources:
            return link.fetchone();
        
    def getResource(self):
        return self.resources;
    
    def fetchAll(self):
        link = self._getLink();
        res = [];
        if self.resources:
            return link.fetchall()


    def setLink(self, dict = False):
        if self._getLink():
            if dict:
                self.link = self.db.cursor(dbapi.cursors.DictCursor)
            else:
                self.link = self.db.cursor()

    def _getLink(self):
        if self.link:
            return self.link;
        else:    
            print 'You must connect first';
            return False;
        
        
    def getSetting(self):
        return self.link.paramstyle
