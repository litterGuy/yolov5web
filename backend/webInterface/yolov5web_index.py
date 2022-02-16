#!/usr/bin/env python
# encoding: utf-8

import os

import tornado.gen
import tornado.web

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Index(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        self.render(os.path.join(BASE_PATH, 'dist/index.html'))
