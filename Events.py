import random

def call_eventlist():

    # events are ordered as "event number, event name, event danger, event likelihood, event text"

    event_list =[]

    event_0 = list([0, "Everything is Silent", 0, 90,])
    event_list.append(event_0)

    event_1 = list([1, "Raiders", 5, 30,])
    event_list.append(event_1)

    event_2 = list([2, "Cache Found", 1, 20,])
    event_list.append(event_2)

    event_3 = list([3, "Friendly Station", 1, 50,])
    event_list.append(event_3)

    event_4 = list([4, "Generator Emergency,", 4, 20,])
    event_list.append(event_4)

    event_5 = list([5, "Enemy Station", 9, 50,])
    event_list.append(event_5)

    event_6 = list([6, "Neutral Station", 4, 50,])
    event_list.append(event_6)

    event_7 = list([7, "Gas cloud", 5, 10,])
    event_list.append(event_7)

    event_8 = list([8, "Pirate Cruiser", 9, 10,])
    event_list.append(event_8)

    return(event_list)


def call_event():
    # events are ordered as "event number, event name, event danger, event likelihood, event text"
    event_list = call_eventlist()

    event_pool = []


    for n in range(0, len(event_list)):

        event_grab = event_list[n]
        event_likley = event_grab[3]
        for x in range(0, event_likley):
            event_pool.append(event_grab)

    pick = random.choice(event_pool)
    return(pick)


def call_specific_event(int):
    event_list = call_eventlist()
    return event_list[int]
