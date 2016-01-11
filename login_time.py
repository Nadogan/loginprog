import re
import string

separated_login = []
separated_logout = []
parsed_login = []
parsed_logout = []
p = re.compile('\d\d:\d\d \D\D', re.IGNORECASE)

def timesplit(input, target):
	timeformat = string.replace(input,":", " ")

	a = timeformat.split(" ")
	
	target.append(a[0])
	target.append(a[1])
	target.append(a[2])

print "Enter login time, format XX:XX XM."
login_time = raw_input("> ")

while True:
	if p.match(login_time) == None:
		print "Please re-enter login time using the format XX:XX XM."
		login_time = raw_input("> ")
	else:
		break

print "Enter logout time, format XX:XX XM."
logout_time = raw_input("> ")

while True:
	if p.match(logout_time) == None:
		print "Please re-enter login time using the format XX:XX XM."
		login_time = raw_input("> ")
	else:
		break
		
timesplit(login_time, separated_login)
timesplit(logout_time, separated_logout)

def time_parse(hr, min, APM, target):
	hour = int(hr)
	min = int(min) / 60 * 100
	if APM == "PM" or APM == "pm":
		hour = hour + 12
	else:
		pass
	target.append(hour)
	target.append(min)
	
time_parse(separated_login[0], separated_login[1], separated_login[2], parsed_login)
time_parse(separated_logout[0], separated_logout[1], separated_logout[2], parsed_logout)

login_value = parsed_login[0] + parsed_login[1]
logout_value = parsed_logout[0] + parsed_logout[1]

if logout_value - login_value <= 12:
	print "You gotta work longer man."
elif logout_value - login_value > 12:
	print "You gotta leave."
else:
	exit(0)