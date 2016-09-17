import webapp2
import jinja2
from models import *
from views import *



app = webapp2.WSGIApplication([
    ('/getRank', getRank),
    
], debug=True)