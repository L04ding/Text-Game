import random
Raid = "Raid"
Discovery = "Discovery"
Event3 = "Event3"
eventpool = [Raid,Discovery,Event3]
def callevent( bool ):
	if bool == True:
		pick = random.randint(0,len(eventpool))
		print(eventpool[pick])
	else:
		print("There was no event")

yesevent = input("do you want an event")
if "y" in yesevent or "Y" in yesevent:
	callevent(True)
else:
	callevent(False)
input("")
