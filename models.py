from google.appengine.api import memcache
from google.appengine.ext import ndb


class dashboard(ndb.Model):

    Key = ndb.StringProperty()
    value = ndb.IntegerProperty()

    @classmethod
    def obtainRank(cls, v):
        q = cls.query().filter(dashboard.value >= int(v))
        return q.count() + 1

