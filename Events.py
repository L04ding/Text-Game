import random

event_0 = list([0,"Everything is Silent", 0, 90])
event_1 = list([1,"Raiders", 5, 30])
event_2 = list([2,"Cache Found", 1, 20])
event_3 = list([3,"Friendly Station", 1, 50])
event_4 = list([4,"Generator Emergency,", 4, 20])
event_5 = list([5,"Enemy Station", 9, 50])
event_6 = list([6,"Neutral Station", 4, 50])
event_7 = list([7,"Gas cloud", 5, 10])

def call_event( int ):

    eventlist = []
    for x in range(0,event_0[3]):
        eventlist.append(event_0[int])
    for x in range(0,event_1[3]):
        eventlist.append(event_1[int])
    for x in range(0,event_2[3]):
        eventlist.append(event_2[int])
    for x in range(0,event_3[3]):
        eventlist.append(event_3[int])
    for x in range(0,event_4[3]):
        eventlist.append(event_4[int])
    for x in range(0,event_5[3]):
        eventlist.append(event_5[int])
    for x in range(0,event_6[3]):
        eventlist.append(event_6[int])
    for x in range(0,event_7[3]):
        eventlist.append(event_7[int])
    pick = random.choice(eventlist)
    print(pick)
for x in range(0,1000):
    call_event(0)
