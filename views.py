import json
import logging
import time
import traceback
import urllib   
from models  import *
from base_handler import BaseHandler
from google.appengine.api import memcache


class getRanks(BaseHandler):

    def get(self):
        playerId = self.request.get('id')
        playersBestScore = self.request.get('bs')
        playersTopScore = self.request.get('ts')

        player_obj = Player()
        player_obj.ID = playerId
        player_obj.bestScore = int(playersBestScore)
        player_obj.topScore = int(playersTopScore)
            
        self.write(Player.obtainRankFromDB(player_obj))

class getLeaderBoard(BaseHandler):

    def get(self):
        playerId = self.request.get('id')
        self.write(Player.obtainLeaderBoardFromDB(playerId))

class savePlayerDetails(BaseHandler):

    def get(self):
        playerId = self.request.get('id')
        playersName = self.request.get('name')
        playersCountry = self.request.get('country')

        player_obj = Player()
        player_obj.ID=playerId
        player_obj.name = playersName
        player_obj.country = playersCountry

        self.write(Player.savePlayerDetailsToDB(player_obj))

#code for backward compatibility

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
        self.write(dashboard.obtainRank(value))
