from google.appengine.api import memcache
from google.appengine.ext import ndb


class dashboard(ndb.Model):

    key = ndb.StringProperty()
    value = ndb.IntegerProperty()

    @classmethod
    def obtainRank(cls, k, v):
        q = cls.query().filter(dashboard.value >= int(v))
        q1 = cls.query().filter(dashboard.key == k)
        off = 1 if q1.count() == 0 else 0 
        return q.count() + 0 #off

