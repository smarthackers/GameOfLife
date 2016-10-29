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
        checkBestScoreRank = (cls.query().filter(Player.bestScore >= currentPlayer.bestScore).count()) + 1
        checkTopScoreRank = (cls.query().filter(Player.topScore >= currentPlayer.topScore).count()) + 1
        return dict(br=checkBestScoreRank, tr=checkTopScoreRank)

    @classmethod
    def obtainScoreBoardFromDB(cls, currentUsersPlayerId):
    	leaderBoardOutput = {'globalRank' : [], 'globalBestTen' : [], 'globalTopTen' : []}
    	currentPlayer = cls.query().filter(Player.id = currentUsersPlayerId).get()
    	
    	checkAboveRankersOnScoreBoard = cls.query().filter(Player.bestScore > currentPlayer.bestScore).order("bestScore")
    	for p in checkAboveRankersOnScoreBoard.run(limit = 5)
        	leaderBoardOutput['globalRank'].append(json.dumps(p.__dict__))

        leaderBoardOutput['globalRank'].append(json.dumps(currentPlayer.__dict__))

        remainingEntries = 10 - len(leaderBoardOutput['globalRank'])
        checkEqualOrBelowRankersOnScoreBoard = cls.query().filter(Player.bestScore <= currentPlayer.bestScore).order("-bestScore")
        for p in checkEqualOrBelowRankersOnScoreBoard.run(limit = remainingEntries)
        	leaderBoardOutput['globalRank'].append(json.dumps(p.__dict__))

        checkTenBestScoreRanks = cls.query().order("-bestScore")
        for p in checkTenBestScoreRanks.run(limit = 10)
        	leaderBoardOutput['globalBestTen'].append(json.dumps(p.__dict__))

        checkTenTopScoreRanks = cls.query().order("-topScore")
        for p in checkTenTopScoreRanks.run(limit = 10)
        	leaderBoardOutput['globalTopTen'].append(json.dumps(p.__dict__))
    
        return leaderBoardOutput


    @classmethod
    def savePlayerDetailsToDB(cls, currentPlayer):
    	player = cls.query().filter(Player.id = currentPlayer.id).get()
    	player.name = currentPlayer.name
    	player.country = currentPlayer.country
    	return player.put()
