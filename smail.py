#!/usr/bin/env python
# -*- coding: utf-8 -*-
# smail 0.1
# @pirate_security

import smtplib, time, sys, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Erstelle eine Python Liste von einer .txt bei der in jeder Zeile eine Emailadresse steht
##########################################################################################
def ComposeMailingListFromTxt():
	empfaengerliste = []
	for emailaddress in maillistealstxt:
			emailaddress = emailaddress.strip()
			empfaengerliste.append(emailaddress)
	return empfaengerliste

# Warte eine zufällige Zeitdauer zwischen 1 und 2 Sekunden
##########################################################
def Idler():
	random.seed()
	# prep int zwischen 1 und 2
	secondsToSleep = random.random()
	secondsToSleep = secondsToSleep + 1
	i = str(secondsToSleep)
	# die eigentliche sleep function
	time.sleep(secondsToSleep)
	return secondsToSleep

# Hauptfunktion: Sende an alle in der Liste
###########################################	
def MailToAllInList():
	sender = "your@email.de"
	s = smtplib.SMTP('smtp.youremail.de:mailport')
	s.starttls()
	s.ehlo()
	s.login('your@email.de', 'yourpassword')
	mailedtolist =[]
	empfaengerliste = ComposeMailingListFromTxt()
	for emailaddress in empfaengerliste:
		# Emailcontainer mit korrektem MIME Typ erstellen
		msg = MIMEMultipart('alternative')
		msg['Subject'] = 'Pythonmailer Test'
		msg['From'] = "your@email.de"
		msg['To'] = emailaddress
		# plain-text und an HTML version
		text = "Falls der Newsletter nicht richtig angezeigt wird, können Sie ihn unter (Link) lesen."
		# Aufnahme von text/plain und text/html & Fuege parts in den Emailcontainer
		msg.attach((MIMEText(text, 'plain'))
		msg.attach((MIMEText(html, 'html'))
		# Datum nach RFC 2822 Internet Email standard.
		msg['Date'] = time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.gmtime())
		msg['User-Agent'] = "PyRateSec (Python v2.7)"
		# Email senden
		s.sendmail(sender, emailaddress, msg.as_string())
		mailedtolist.append(1)
		nummer = len(mailedtolist)
		x = Idler()
		x = str(x)
		print "Mail Nr. %d gesendet an %r | Warte %s Sekunden" % (nummer,emailaddress,x)
		
		
	s.quit()

if __name__ == "__main__":
	err = sys.stderr.write
	if len(sys.argv) != 3:
				sys.exit(err("""
##################################################################################################
##                                                                                              ##
## Gebrauchsanleitung: python %s <.html  mit Email-Inhalt> <.txt mit Email-Liste> ##
##                                                                                              ##
##################################################################################################
""" % (sys.argv[0],)))

	else:
		html = (open(sys.argv[1],"r")).read()
		maillistealstxt = (open(sys.argv[2],"r")).readlines()
		MailToAllInList()

		print "\nAlles fertig :)"
