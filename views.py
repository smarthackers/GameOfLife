import json
import logging
import time
import traceback
import urllib   
from models  import *
from base_handler import BaseHandler
from google.appengine.api import memcache


class getRank(BaseHandler):

    def get(self):
        key = self.request.get('id')
        value = self.request.get('score')

        d_obj = dashboard(
            id=key,
            key=key,
            value=int(value)
            )
        d_obj.put()
        self.write(dashboard.obtainRank(key, value))




