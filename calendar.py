"""
Creates a calculator that lets the user view, add an event, update an existing event, and deleting an existing event. 
"""

from time import sleep, strftime

first_name = 'Colin'

calendar = {

}

# welcome message function 
def welcome():
    print "Welcome to your calendar, " + first_name + "."
    print "The calendar is opening..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Time: " + strftime("%H:%M:%S")
    sleep(1)
    print "What would you like to do?"

#start calendar function with logic for user input 
def start_calendar():
    welcome()
    start = True
    while start:
          user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
          user_choice = user_choice.upper()
          if user_choice == "V":
              if len(calendar.keys()) < 0:
                  print "The Calendar is empty."
              else:
                  print calendar 
          elif user_choice == "U":
                date = raw_input("What date? ")
                update = raw_input("Enter the update: ")
                calendar[date] = update
                print "The update is successful."
                print calendar 
          elif user_choice == "A":
                event = raw_input("Enter event: ")
                date = raw_input("Enter date (MM/DD/YYYY): ")
                if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                    print "Invalid date entered."
                    try_again = raw_input("Try Again? Y for Yes, N for No: ")
                    try_again = try_again.upper()
                    if try_again == "Y":
                        continue
                    else:
                        start = False 
                else: 
                    calendar[date] = event
                    print "Event added successfully."
                    print calendar 
          elif user_choice == "D":
                if len(calendar.keys()) < 1:
                    print "The calendar is empty."
                else:
                    event = raw_input("What event?")
                    for date in calendar.keys():
                        if event == calendar[date]:
                            del calendar[date]
                            print "The event was deleted"
                            print calendar
                        else:
                            print "Incorrect event specified."
          elif user_choice == "X":
                start = False 
          else:
                print "Invalid Command."
                start = False

start_calendar()
