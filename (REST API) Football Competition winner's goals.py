import math
import os
import random
import re
import sys


import requests, json

def getWinnerTotalGoals(competition, year):
	count = 0
	#Getting Winner
	winnerUrl = "https://jsonmock.hackerrank.com/api/football_competitions?name="+competition+"&year="+str(year)
	winnerReq = requests.get(winnerUrl)
	winnerData = json.loads(winnerReq.text)
	for winners in winnerData['data']:
		winner = winners['winner']
	
	
	team1Url = "https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team1="+winner+"&page=1"
	teamUrl_req = requests.get(team1Url)
	teamUrl_data = json.loads(teamUrl_req.text)
	for i in range(1,teamUrl_data['total_pages']+1):
		team1Url_complete = "https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team1="+winner+"&page="+str(i)
		teamUrl_req_com = requests.get(team1Url_complete)
		teamUrl_data_com = json.loads(teamUrl_req_com.text)
		for data in teamUrl_data_com['data']:
			count = count + int(data['team1goals'])
	
	team2Url = "https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team2="+winner+"&page=1"
	teamUrl_req2 = requests.get(team2Url)
	teamUrl_data2 = json.loads(teamUrl_req2.text)
	for i in range(1,teamUrl_data2['total_pages']+1):
		team2Url_complete = "https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team2="+winner+"&page="+str(i)
		teamUrl_req_com2 = requests.get(team2Url_complete)
		teamUrl_data_com2 = json.loads(teamUrl_req_com2.text)
		for data in teamUrl_data_com2['data']:
			count = count + int(data['team2goals'])
	
	return count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	competition = input().strip()
	year = int(input().strip())
	result = getWinnerTotalGoals(competition,year)
	fptr.write(str(result) + '\n')
	fptr.close()


