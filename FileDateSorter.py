from os import listdir, path
import os
from datetime import datetime
import shutil

# Regular Expression
import re

reg = r"^[0-9]+-(0?[1-9]|[12][0-9]|3[01])$"

dirs = listdir("./")
for d in dirs:
	if d == "FileDateSorter.py":
		continue
	if re.match(reg, d):
		continue
	
	ts = path.getmtime(d)
	t = datetime.utcfromtimestamp(ts).strftime('%Y-%m')
	splits = t.split('-')
	year = splits[0]
	month = splits[1]
	folder = year + '-' + month
	if not path.exists(folder):
		os.mkdir(folder)
	shutil.move(d, folder+'/'+d)
	print('Move ' + d + ' to ' + folder + '/' + d)