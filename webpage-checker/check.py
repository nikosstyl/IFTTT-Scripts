import pytz
from os import write
from time import strftime, strptime
import requests
from datetime import datetime
import os.path
from dateutil.parser import parse as parsedate


key = "Insert your key here"
event = "Insert your event here"
utc=pytz.UTC

x = requests.head('Insert the page you want to follow')
url_time = parsedate(x.headers['last-modified'])
mflag = False
if not os.path.isfile('last.date') :
	ldatetxt = open('last.date', 'w')
	mflag =  True
ldatetxt = open('last.date','r+')
ldate = ldatetxt.read()

if mflag == True or not ldate :
	ldatetxt.write(url_time.strftime("%m/%d/%Y, %H:%M:%S"))
	print('The file was empty!')
	ldatetxt.close()
	exit()

if url_time > utc.localize(datetime.strptime(ldate, "%m/%d/%Y, %H:%M:%S")) :
	requests.post('https://maker.ifttt.com/trigger/'+event+'/with/key/'+key)
	ldatetxt.seek(0,0)
	ldatetxt.write(url_time.strftime("%m/%d/%Y, %H:%M:%S"))
	print('Website UPDATED')
else :
	print('Website is same')

ldatetxt.close()
