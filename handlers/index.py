import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import json
import random
import os


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")



