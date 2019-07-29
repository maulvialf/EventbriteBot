from bs4 import BeautifulSoup
from requests import *
import model
import crud
import json
import datetime

def crawlpage(page_id):
	url  = "https://www.eventbrite.com/d/indonesia--jakarta-pusat/all-events/?page={}".format(page_id)
	x    = get(url)
	soup = BeautifulSoup(x.content, 'html.parser')
	data = json.loads(soup.find('script', type='application/ld+json').text)
	# add data
	listevents = []
	for event in data:
		
		if(float(event["offers"]["lowPrice"]) > 0 or float(event["offers"]["lowPrice"]) > 0):
			continue
		
		newitem       = model.Event()
		newitem.judul = event["name"]
		newitem.link  = event["url"]
		dateformat = "%Y-%m-%d"
		newitem.waktu_berlangsung =  datetime.datetime.strptime(event["startDate"], dateformat)
		newitem.waktu_event       = datetime.datetime.strptime(event["startDate"], dateformat)
		newitem.status = 0
		listevents.append(newitem)		

	return listevents

def checkWebUpdate():
	pageindex 			= 1
	updated 			= 0
	is_there_new_update = 0
	while(updated == 0):	
		# get 20 item
		listevents = crawlpage(pageindex)
		# cek item satu persatu
		for event in listevents:
			if(crud.checkdata(event) == False):
				is_there_new_update = 1
				crud.addRecord(event)
			else:
				updated = 1
				break

		pageindex += 1

	return is_there_new_update