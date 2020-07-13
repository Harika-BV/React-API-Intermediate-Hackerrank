import math
import os
import random
import re
import sys
import json, requests

def getNumDraws(year):
	count=0
	#Getting Pages
	
	base_url = "https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&page=1"
	base_url_req = requests.get(base_url)
	base_url_data = json.loads(base_url_req.text)
	total_pages = base_url_data['total_pages']
	
	for i in range(0,10):
		search_url_find_page = "https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&team1goals="+str(i)+"&team2goals="+str(i)+"&page=1"
		search_url_req_find = requests.get(search_url_find_page)
		search_url_data_find = json.loads(search_url_req_find.text)
		count = count + int(search_url_data_find['total'])
		
	return count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	year = int(input().strip())
	result = getNumDraws(year)
	fptr.write(str(result) + '\n')
	fptr.close()


