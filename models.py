import json
from google.appengine.api import memcache
from google.appengine.ext import ndb


class Player(ndb.Model):

    name = ndb.StringProperty()
    bestScore = ndb.IntegerProperty()
    topScore = ndb.IntegerProperty()
    country = ndb.StringProperty()

    def __init__(self):
        self.name = ""
        self.bestScore = 0
        self.topScore = 0
        self.country = ""

    @classmethod
    def obtainRankFromDB(cls, currentPlayer):
    	currentPlayer.put()
        checkBestScoreRank = (cls.query().filter(Player.bestScore >= int(currentPlayer.bestScore)).count()) + 1
        checkTopScoreRank = (cls.query().filter(Player.topScore >= int(currentPlayer.topScore)).count()) + 1
        return "{\"bestRank\":" +str(checkBestScoreRank) + ", \"topRank\":" + str(checkTopScoreRank) +"}"

    @classmethod
    def obtainScoreBoardFromDB(cls, currentUsersPlayerId):
    	scoreBoardOutput = {'values' : []}
    	currentPlayer = cls.query().filter(Player.id = currentUsersPlayerId).get()
    	
    	checkAboveRankersOnScoreBoard = cls.query().filter(Player.bestScore > currentPlayer.bestScore).order("bestScore")
    	for p in checkTopTenBestScoreRanks.run(limit = 5)
        	scoreBoardOutput['values'].append(json.dumps(p.__dict__))

        scoreBoardOutput['values'].append(json.dumps(currentPlayer.__dict__))

    	checkBelowRankersOnScoreBoard = cls.query().filter(Player.bestScore <= currentPlayer.bestScore).order("-bestScore")
        
        remainingEntries = 10 - len(scoreBoardOutput['values'])
        for p in checkTopTenBestScoreRanks.run(limit = remainingEntries)
        	scoreBoardOutput['values'].append(json.dumps(p.__dict__))

        checkTopTenBestScoreRanks = cls.query().order("-bestScore")
        for p in checkTopTenBestScoreRanks.run(limit = 10)
        	scoreBoardOutput['values'].append(json.dumps(p.__dict__))

        checkTopTenTopScoreRanks = cls.query().order("-topScore")
        for p in checkTopTenTopScoreRanks.run(limit = 10)
        	scoreBoardOutput['values'].append(json.dumps(p.__dict__))
    
        return scoreBoardOutput


    @classmethod
    def savePlayerDetailsToDB(cls, currentPlayer):
    	player = cls.query().filter(Player.id = currentPlayer.id).get()
    	player.name = currentPlayer.name
    	player.country = currentPlayer.country
    	return player.put()
