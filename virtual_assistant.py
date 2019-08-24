#! This program will randomly select items from lists to help decide where to
# go for lunch or what kind of music to listen to.

import random, datetime
from datetime import date, time

print('\n' + ' _ (╭ರ‿⊙)' * 8 + """\n\nHello I am your virtual assistant. I am designed to give you random
choices about where to eat or what type of music to listen to. Let's begin.\n""")
input('Press enter to continue...')


def lunch():
    
    #Lists defined

    restaurants = ['Jimmy Johns', 'Big Guys', 'Subway', 'Carls Jr.',
                   'Burger King', 'Mc Donalds', 'Arbys', 'The taco truck']

    fridayRestaurants = ['Cafe Rio', 'Zupas', "Mo Bettah's", 'Grinders', 'Apollo Burger', "Pat's BBQ", 'Chungas', "Dickey's"]

    weekend_restaurants = ['Cafe Rio', "Applebee's", 'Longhorn\'s', 'Cafe Trang', 'Kneaders', 'Zupas', 'Bombay House', 'Costa Vida']

    todays_restaurants = []
    
    yesResponses = ['Flavor Town, here we come!', 'Good choice!', 'Oh nice, I took your mom there last week.', "Lovely, you won't regret it!"]
        
    noResponses = ['Dodged a bullet there.', 'Not in the mood eh? Very well.',
                   "Yeah I wouldn't eat there either.", "Can't say I'm surprised.",
                   "What's wrong with that place? Everyone usually likes it there."]

    driverResponses = ['Grab your keys Bitch! ','Buckle up mother fucker. ', 'Yeet! ', 'Lets turn up! ',
                       'This lunch is going to be straight fire! ', 'Lets skrrt on out of here. ', 'Lets get this bread. ']

    actualDestination = []
    actualDrivers = []
    
    drivers = ['Giuliano', 'Taylor', 'Josh', 'Austin', 'Skyler', 'Zach']

    while True:

        todays_cal = date.today()   # Assigns a value of the calendar date: e.g. 2019-12-31
        print(todays_cal)
        todays_int = date.weekday(todays_cal)   # Assigns a value depending on the day of the week: e.g. Friday == 4
        print(todays_int)
        if todays_int == 4:
            todays_list = 'Friday'
            todays_restaurants = fridayRestaurants
        elif todays_int == 5 or todays_int == 6:
            todays_list = 'weekend'
            
            todays_restaurants = weekend_restaurants
        else:
            todays_list = 'weekday'
            todays_restaurants = restaurants

        print('\n\n' + (' _ (っ˘ڡ˘ς)' * 6) + '\n\nIt looks like today is ' + todays_cal.strftime('%A') + ' and therefore we will be using the ' + todays_list + ' list for selection.')
        

        print('\n' + ' _ ( ˘▽˘)っ♨' * 6 + '\n\nSo far we have a total of ' + str(len(todays_restaurants)) + ' places in the list')
        input('\nReady to start the randomizer?\n\nPress "Enter to continue"...\n')

        random.shuffle(todays_restaurants)
            
        for place in todays_restaurants:
            try:
                if final_answer == True:
                    break
            except:
                pass
            
            final_answer = ''
            correct_answer = False
            final_answer = False

            while not correct_answer:
                print('\n' + ' _ (⊃｡•́‿•̀｡)⊃━∈･*:.｡. .｡.:*･゜ﾟ･*･*:.｡. .｡.:*･゜ﾟ･*･*:.｡. .｡.:*･゜ﾟ･*☆' + '\n\nDoes ' + place + ' sound good?\n')
                restaurantAnswer = input('yes or no\n\n')
                
                if restaurantAnswer.lower() == 'yes' or restaurantAnswer.lower() == 'y':
                    print('\n' + random.choice(yesResponses))
                    actualDestination.append(place)
                    correct_answer = True
                    final_answer = True
                    print('\n' + ' _ (ﾉ^ヮ^)ﾉ*:・ﾟ✧' * 4 + '\n\nNice choice!\n\n')
                    break
                elif restaurantAnswer.lower() == 'no' or restaurantAnswer.lower() == 'n':                
                    print('\n' + random.choice(noResponses) + '\n')
                    correct_answer = True
                else:
                    print('\nTry that again\n')
                
                  
        if restaurantAnswer.lower() == 'no' or restaurantAnswer.lower() == 'n':
            repeat = input('That was all the choices. Do you want to repeat this step?\n\n(yes or no)\n\n')          
            if repeat.lower() == 'yes' or repeat.lower() == 'y':
                continue
            elif repeat.lower() == 'no' or repeat.lower() == 'n':
                print('\n' + (' _ ╭∩╮(︶︿︶)╭∩╮' * 5) + '\n\nWell good luck choosing a place without me.\n')
                mysteryDestination = 'who the fuck knows'
                input('Enter to continue...')
        
        # Assumes a driver needs to be picked based on the day of the week. To be used to determine if the driver picking loop needs to be used.       

        while True:  
            if  todays_int < 5:
                driver_assumption = 'do'
            else:
                driver_assumption = 'do not'        
            drivers_needed = input('Since today is ' + todays_cal.strftime('%A') + '. I am going to that assume you ' + driver_assumption + " need help deciding who's driving.\n\nIs this correct?\n(yes or no)")
            if drivers_needed.lower() == 'yes' or drivers_needed.lower() == 'y':
                drivers_needed = True
                break
            elif drivers_needed.lower() == 'no' or drivers_needed.lower() == 'n':
                driver_needed = False
                break
            else:
                print('Please try that again.')
                continue
        # TODO: Not allow an input greater than the length of the driver list
        
        while True:
            print('\nSo far our VDC drivers list is ' + str(len(drivers)) + ' long.\n')
            numOfdrivers = input('How many drivers are needed today?\n\n')
            if numOfdrivers.isdecimal():
                break                    
            else:
                print('Input must be a number')
                    

        while int(numOfdrivers) > len(actualDrivers):
            thisDriver = random.choice(drivers)
            print('\nIs ' + thisDriver + ' going to lunch today?\n')
            driverAnswer = input('yes or no?\n')

            if driverAnswer.lower() == 'yes' or driverAnswer.lower() == 'y':
                print('\n' + thisDriver + ', ' + random.choice(driverResponses) + " You're driving!\n")
                actualDrivers.append(thisDriver)
                drivers.remove(thisDriver)

            elif driverAnswer.lower() == 'no' or driverAnswer.lower() == 'n':
                drivers.remove(thisDriver)
                continue

        try:
            mysteryDestination
            print('\nLooks like we are going to ' + mysteryDestination + ' and the driver(s) are ' + (', and '.join(str(aD)for aD in actualDrivers)) + '.')
        except:
            print('\nLooks like we are going to ' + str(actualDestination)[2:-2] + ' and the driver(s) are ' + (', and '.join(str(aD)for aD in actualDrivers)) + '.')

        break
    
    


def music():

    genres = ['Pop', 'Classic Rock', 'Country', 'Rock', 'Hip Hop', 'rap', "80's", "90's", 'EDM', 'Alternative', "All Genre's", 'Todays Hits: 2014 to present',
              "Austin's choice", "Giuliano's choice", "Zach's choice", 'Todays Hits: 2019', 'Indie Folk', 'Party', 'Reggae', 'AJR']

    musicalDeclaration = ['Ahh music, the purest form of communication.\n\nLets hope we can set the proper mood today!\n',
                          "What's it going to be today?\n\nRockin' out?\n\nSomething slow?\n\nThe fates will decide...\n",
                          "Time for some musical inspiration!\n\n"] 
    musicChoice = []

    while True:

        random.shuffle(genres)

        print('\n' + '(^o^)/♫•*¨*•.¸¸♪♫•*¨*•.¸¸♪♫•*¨*•.¸¸♪\n' + random.choice(musicalDeclaration))
        input('\nPress enter to see what the randomizer has in store for us today...\n')

        for types in genres:
            print('\n' + ' _ (⊃｡•́‿•̀｡)⊃━∈･*:.｡. .｡.:*･゜ﾟ･*･*:.｡. .｡.:*･゜ﾟ･*･*:.｡. .｡.:*･゜ﾟ･*☆\n' + '\nDoes ' + types + ' sound okay?\n')
            genreChoice = input('\nyes or no\n')
            if genreChoice.lower() == 'yes' or genreChoice.lower() == 'y':
                musicChoice.append(types)
                break

            elif genreChoice.lower() == 'no' or genreChoice.lower() == 'n':
                print('Very well, lets try another...')
        

        if genreChoice.lower() == 'no' or genreChoice.lower() == 'n':
            print('\nThat was all the choices in list so far. Would you like to repeat the list?\n')
            listRepeat = input('\nyes or no\n')

            if listRepeat.lower() == 'yes' or listRepeat.lower() == 'y':
                continue
            elif listRepeat.lower() == 'no' or listRepeat.lower() == 'n':
                print('\nYou sure are good at wasting time. Lets do this again sometime!\n')
                break
           

        print('It sounds like we will be listening to ' + str(musicChoice)[2:-2] + ' today!')
        break   
   
def typeOfhelp():

    while True:

        helpType = input('\n\n' + ' _ (つ°ヮ°)つ' * 6 + """\n\nwhat do you need my help deciding for you today?\n
                        The choices so far are:\n\n1 - lunch\n\n2 - music\n\n0 - End program\n\n(Enter either a typed out choice or the corresponding number)\n\n""") 
        if helpType == '1' or helpType == 'lunch':
            lunch()
        elif helpType == '2' or helpType == 'music':
            music()
        elif helpType == '0' or helpType == 'end':
            print('Goodbye. Have a nice day!')
            break
        elif helpType != '0' or helpType != '1' or helpType != '2':
            print('\n\nRead the instructions sloooowly...\n\nAnd try again...')

typeOfhelp()
