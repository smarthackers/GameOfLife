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
        playerId = self.request.get('id')
        playersBestScore = self.request.get('bs')
        playersTopScore = self.request.get('ts')

        player_obj = Player(
            id=playerId,
            bestScore=int(playersBestScore),
            topScore=int(playersTopScore)
            )

        self.write(Player.obtainRankFromDB(player_obj))

class getScoreBoard(BaseHandler):

    def get(self):
        playerId = self.request.get('id')
        self.write(Player.obtainScoreBoardFromDB(playerId))

class savePlayerDetails(BaseHandler):

    def get(self):
        playerId = self.request.get('id')
        playersName = self.request.get('name')
        playersCountry = self.request.get('country')

        player_obj = Player(
            id = playerId,
            name = playersName,
            country = playersCountry
            )

        self.write(Player.savePlayerDetailsToDB(player_obj))

