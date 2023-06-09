from utilities import timeFormat

def getPassengers(maximum):
    while(True):
        try:
            passenger = input("? Enter the number of passengers (max. " + str(maximum)+ "): ")
            if not passenger:
                return 1
            
            passenger = int(passenger)
            if (passenger < 0 or passenger > maximum):
                raise Exception(f"Invalid passengers number. You added {passenger} but the possible passengers are 1 or " + str(maximum))
            
            return passenger
        except Exception as err:
            print(err)

def getPositiveInt(inputText, errorText):
    while(True):
        try:
            inp = input(inputText)
            if not inp:
                return 0
            
            inp = int(inp)
            if (inp < 0):
                raise Exception(errorText)
            
            return inp
        except Exception as err:
            print(err)

def getExcessiveCarrage():
    while(True):
        try:
            excessive_carrage = input("? Enter the weight of the luggage (press enter or 0 if none): ")
            if not excessive_carrage:
                return 0
            
            excessive_carrage = int(excessive_carrage)
            if (excessive_carrage < 0):
                raise Exception(f"The weight cannot be negative.")
            
            return excessive_carrage
        except Exception as err:
            print(err)

def getTowingWeight():
    while(True):
        try:
            towingWeight = input("? Enter the weight (kg) of towing (press enter or 0 if none): ")
            if not towingWeight:
                return 0

            towingWeight = int(towingWeight)
            if (towingWeight < 0):
                raise Exception(f"The weight cannot be negative.")

            return towingWeight
        except Exception as err:
            print(err)

def getTime():
    while(True):
        try:
            time = input("? Enter the departure time (format HH:MMPM/AM such as 12:00AM): ")
            formTime = timeFormat(time)

            return formTime
        except Exception as err:
            print(err)
        

def getInputWithComparisonList(text, array, default):
    while(True):
        try:
            inp = input(text)
            if not inp:
                return default

            if inp not in array:
                raise Exception("The value you added is not inside the possible values of "+str(array))
            
            return inp
        except Exception as err:
            print(err)

def getExperience():
    while(True):
        try:
            years = input("? Enter the experience years: ")
            if not years:
                return 0
            
            years = int(years)
            if (years < 0):
                raise Exception(f"The experience cannot be negative.")
            
            return years
        except Exception as err:
            print(err)

def getServiced():
    while(True):
        try:
            service = input("? Is the car serviced (yes or no): ")
            if not service or (service).lower() == "no":
                return False
            
            if ((service).lower() == "yes"):
                return True
            else:
                raise Exception(f"Invalid. Only yes or no")
            
        except Exception as err:
            print(err)


##  FLIGHT INPUTS!
def getAverageLuggage(maximum):
    while(True):
        try:
            inp = input(f"? Enter the average weight (kg) of the luggage (max. {maximum}kg): ")
            if not inp:
                return 0
            
            inp = int(inp)
            if (inp < 0 or inp > maximum):
                raise Exception(f"The luggage weight can be between 0 and {str(maximum)}")
            
            return inp
        except Exception as err:
            print(err)

def getRatio():
    while(True):
        try:
            inp = input("? Enter the female ratio (between 0 and 1): ")
            if not inp:
                return 0
            
            inp = float(inp)
            if (inp < 0 or inp > 1):
                raise Exception(f"Invalid ratio: value can be between 0 and 1")
            
            return inp
        except Exception as err:
            print(err)

def getWindDirection():
    while(True):
        try:
            inp = input("? Enter the wind direction (head or tail): ")
            if not inp or inp == "tail":
                return "tail_wind"

            if inp == "head":
                return "head_wind"

            raise Exception("The wind direction can be head or tail")
        except Exception as err:
            print(err)

