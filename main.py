import webapp2
import jinja2
from models import *
from views import *



app = webapp2.WSGIApplication([
    ('/getRank', getRank),
    ('/getScoreBoard', getScoreBoard),
    ('/savePlayerDetails', savePlayerDetails)
], debug=True)