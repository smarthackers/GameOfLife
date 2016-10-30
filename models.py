import json
from google.appengine.api import memcache
from google.appengine.ext import ndb


class Player(ndb.Model):

    ID = ndb.StringProperty()
    name = ndb.StringProperty()
    bestScore = ndb.IntegerProperty()
    topScore = ndb.IntegerProperty()
    country = ndb.StringProperty()

    def __init__(self):
        ndb.Model.__init__(self)
        self.ID = ""
        self.name = ""
        self.bestScore = 0
        self.topScore = 0
        self.country = ""

    @classmethod
    def obtainRankFromDB(cls, currentPlayer):
    	currentPlayer.put()
        checkBestScoreRank = (cls.query(Player.bestScore >= currentPlayer.bestScore).count())
        checkTopScoreRank = (cls.query(Player.topScore >= currentPlayer.topScore).count())
        return dict(br=checkBestScoreRank, tr=checkTopScoreRank)

    @classmethod
    def obtainLeaderBoardFromDB(cls, currentUsersPlayerId):
    	leaderBoardOutput = {'globalRank' : [], 'globalBestTen' : [], 'globalTopTen' : []}
    	currentPlayer = cls.query(Player.ID == currentUsersPlayerId).get()
    	
    	checkAboveRankersOnScoreBoard = cls.query(Player.bestScore > currentPlayer.bestScore).order(Player.bestScore).fetch(limit=5)
    	for p in checkAboveRankersOnScoreBoard:
        	leaderBoardOutput['globalRank'].append(p.to_dict()))

        leaderBoardOutput['globalRank'].append(currentPlayer.to_dict()))

        remainingEntries = 10 - len(leaderBoardOutput['globalRank'])
        checkEqualOrBelowRankersOnScoreBoard = cls.query(Player.bestScore <= currentPlayer.bestScore).order(-Player.bestScore).fetch(limit=remainingEntries)
        for p in checkEqualOrBelowRankersOnScoreBoard:
        	leaderBoardOutput['globalRank'].append(p.to_dict()))

        checkTenBestScoreRanks = cls.query().order(-Player.bestScore).fetch(limit=10)
        for p in checkTenBestScoreRanks:
        	leaderBoardOutput['globalBestTen'].append(p.to_dict()))

        checkTenTopScoreRanks = cls.query().order(-Player.topScore).fetch(limit=10)
        for p in checkTenTopScoreRanks:
        	leaderBoardOutput['globalTopTen'].append(p.to_dict()))
    
        return leaderBoardOutput


    @classmethod
    def savePlayerDetailsToDB(cls, currentPlayer):
    	player = cls.query(Player.ID == currentPlayer.ID).get()
    	player.name = currentPlayer.name
    	player.country = currentPlayer.country
    	return player.put()

#code for backward compatibility

class dashboard(ndb.Model):

    key = ndb.StringProperty()
    value = ndb.IntegerProperty()

    @classmethod
    def obtainRank(cls, score):
        return cls.query(dashboard.value >= int(score)).count()