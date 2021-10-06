
# Simulation Course - Tel Aviv University
# Corona tests lab
# Noam Tenne

#importing libraries
import heapq
import numpy as np
import matplotlib.pyplot as plt

class Event():  # create an event object for out events
    def __init__(self, time, eventType):
        self.time = time  # event time
        self.eventType = eventType  # type of the event
        heapq.heappush(P, self)  # enter the event to the event list

    def __lt__(self, event2):  # we need to have this attribute in order to sort our events by time
        return self.time < event2.time #so that we would be able to know when to stop our while loop

np.random.seed()

# defining variables
current_time = 0.0
T = 10 * 24 * 60  # Total time of simulation, in minutes
minutes_in_day= 24*60 #24 hours, 60 minutes per hour..
P = []  # our heap
A = 0  # State of the server. [0-free,1-occupied]
Line_regular = 0  # Line for the general pop. (70%)
Line_kids = 0  # Line for the kids. (30%)
infected = False #True if the laborant is infected
time_served = 0 #time of service for the patient
time_to_replace = 0 #amount of time that passes by until the next laborant comes
replacement_time = 0 #the time the replacement was taken on
laborant_count = 0  # counts the tests for the current laborant

tests = np.zeros(10, dtype=int)  # this will tell us how many tests were made per day
time=[0] #our time axis (horizontal), index synchronized with the next array
people_in_system=[0] #our people in the system axis (vertical), index synchronized with the previous array

Event(np.random.exponential(0.5), "arriving")  # setting up our first event

def on_arrival(): #defines what happens when a new patient arrives
    global A, Line_kids, Line_regular
    if A == 0:  # if the server is free
        patient_check() #the server is indeed free, so the patient will be checked now
    else: #server isn't free
        kid_rand = np.random.random(1) #we've got to determine whether or not it is a kid
        if kid_rand <= 0.3:  # means that it's a kid
            Line_kids += 1
        else:  # it's not a kid
            Line_regular += 1

def new_arrival(): #creates a new arrival
    global current_time
    exponential_lambda = 2 if is_night_time() else 1 #determines the value of our lambda parameter depending on day or night time
    Event(current_time + np.random.exponential(exponential_lambda), "arriving")

def is_night_time(): #checks if it's night time
    global current_time, minutes_in_day
    return current_time % minutes_in_day <= 7 * 60 # the first seven hours of the day were defined as night time. 

def patient_check(): #all that happens during the service given to the patient
    global A, current_time, infected, replacement_time
    A = 1 #patient in service, so the server is now occupied.
    time_served = np.random.exponential(0.5) #time of service is exponentialy randomized
    leave_time = current_time + time_served #sets the time the test will be over on
    if infected: #if our laborant got infected
        infected = False #the new laborant will not be infected
        leave_time = max(leave_time, replacement_time + time_served) #I have to take both of them under consideration
    Event(leave_time, "leaving")

def self_test(): #all that happens while the server\laborant is testing himself
    global current_time, laborant_count, infected, time_to_replace, replacement_time, tests
    current_time += 1 # self testing takes exactly 1 minute
    if not int(current_time / (minutes_in_day))>9:
        tests[int(current_time / (minutes_in_day))] += 1 #adds another 1 to the tests per day counter array
        if np.random.random(1) > (0.998 **10):# 0.2% chance to get infected, and the server checks himeself every 10 tests
            infected=True #got infected
            time_to_replace=np.random.uniform(15,30) #time to replace takes 15 to 30 minutes
            replacement_time = time_to_replace + current_time #time of replacement is the time now+the time it took for the new laborant to come

def patient_leaving(): #defines what happens when\after the patient (finally) leaves
    global current_time, A, laborant_count, minutes_in_day, tests, infected, Line_regular, Line_kids
    laborant_count += 1 #a test was made so I count it for the laborant
    tests[int(current_time / (minutes_in_day))] += 1 #a test was made so I count it for the tests counter array
    if Line_kids > 0: #there's a kid waiting
        A = 1 #the server will treat him
        Line_kids -= 1 #that kid is no longer waiting so the line just got shorter
    elif Line_regular > 0: #no kids and there's an adult waiting in line
        A = 1 #the server will treat him
        Line_regular -= 1 #that adult is no longer waiting so the line just got shorter
    else: #no one is waiting
        A = 0 #the server is free
    people_in_system.append(Line_kids + Line_regular)  # saves the number of people currently in the system
    time.append(current_time)  # saves the current time to be synchronized with the number of people in the graph
    if laborant_count % 10 == 0: #every 10 tests the laborant needs to know
        self_test() #tests himself

#our main part : the simulation code for time advancement, mostly resemble the examples studied
while P:
    event = heapq.heappop(P)
    current_time = event.time
    if event.eventType == "arriving" and current_time<T:
        on_arrival() #deals with the patient
        new_arrival() #creates a new arrival
    elif event.eventType == "leaving" and current_time<T:
        patient_leaving()
        if A==1:
            patient_check()

# plots and other calculations:

#average amount of patients in the system:
patients_count=0
for i in range(len(time)-1):
    patients_count += people_in_system[i]*(time[i+1]-time[i])
print(f"The average number of patients in the system is {1+(patients_count/T)}")

#The lab's average daily cost:
daily_cost = 3 * tests #every test costs 3 NIS to the lab. so this array presents the daily cost
print(f"The lab's average daily cost is {np.average(daily_cost)}")

# Plot1 - Daily lab costs:
plt.plot(range(10), daily_cost)
plt.title('Daily Lab Costs')
plt.xlabel('Day')
plt.ylabel('Cost')
plt.show()

#number of people per hour:
patients_per_hour=np.zeros(24)
arrivals_per_hour=np.zeros(24)
for j in range(len(time)-1):
    hour=int((time[j]%1440)/60) #what hour of the day it is
    patients_per_hour[hour] += people_in_system[j]
    arrivals_per_hour[hour] += 1

# Plot2 - Average patients in every hour of the day:
plt.plot(range(0,24),(patients_per_hour/arrivals_per_hour))
plt.title('Average Patients in Every Hour')
plt.xlabel('Hour')
plt.ylabel('Average # of Patients')
plt.show()
