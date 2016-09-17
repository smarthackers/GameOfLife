import logging
import webapp2
from webapp2_extras import jinja2
import json

from google.appengine.api import users


class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
