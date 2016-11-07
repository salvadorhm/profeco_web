#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import json


render = web.template.render('views/',cache=False)
        
urls = (
    '/','index',
    '/values(.*)', 'values',
    '/about','about',
)

class index:
    def GET(self):
        return render.index()

class values:        
    def GET(self, datos):
        datos=[]
        with open('data/profeco.json','r') as file:
            datos = json.load(file)
        return render.values(datos['results'])

class about:
    def GET(self):
        return render.about()

if __name__ == "__main__":
    app = web.application(urls, globals(), autoreload=False)
    web.config.debug = True
    app.run()