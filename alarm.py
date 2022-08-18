from playsound import playsound
import datetime



alarmHour = int(input("Select the hour to wake up: "))
alarmMinute = int(input("Select the minute: "))
amPm = input("am or pm?: ").lower()
if amPm == "pm":
    alarmHour = alarmHour + 12


#always true, so it keep running
while (1 == 1):
    #not using now.hour because it takes the current hour and keep it as that
    #datetime.datetime.now().hour keeps track of the current hour 
    if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
        playsound('sample.wav')
        break


