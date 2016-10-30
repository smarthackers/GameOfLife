import webapp2
import jinja2
from models import *
from views import *



app = webapp2.WSGIApplication([
    ('/getRanks', getRanks),
    ('/getScoreBoard', getScoreBoard),
    ('/savePlayerDetails', savePlayerDetails),
    #code for backward compatibility
    ('/getRank', getRank)
], debug=True)