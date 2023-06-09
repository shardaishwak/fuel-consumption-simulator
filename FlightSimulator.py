import random

a350 = {
    "code": "a350",
    "name": "Airbus A350",

    "average_consumption": 11.2, # L/hour/passenger,
    "ground_consumption": 0.27,
    "take_off_consumption": 12.6,
    "max_passengers": 325,

    "max_other_weight": 0.3,
    "max_travel_distance": 16_600,
    "max_luggage": 2,
    "max_luggage_weight": 23, # kg
    "max_luggage_and_passenger_weight": 50100, # kg
    "max_fuel_capacity": 164_000, # L
    "max_total_weight": 283_900, # kg
    "headwind_consumption": 0.245, # perc
    "tailwind_consumption": -0.1, # perc , negative is efficient
    "max_other_weight_perc": 100,
    "taxing_fuel_usage": 260/0.8, # # If 1 kilogram of water is 1 litre, 0.8 kilograms of jet fuel is 1 litre.
    "snow_weight": 100,
    "max_speed": 950,
    "empty_flight_fuel": 2485
}

a380 = {
    "code": "a380",
    "name": "Airbus A380",

    "average_consumption": 16.21, # L/hour/passenger, the calculation is based on the fact that a plane consumes around 11000L per hour. And given that an average weight of a passenger and cargo together can be counted for 150  each, we found the calculation
    "ground_consumption": 0.4,
    "take_off_consumption": 18.2,
    "max_passengers": 615,

    "max_other_weight": 0.4,
    "max_travel_distance": 15_288,
    "max_luggage": 2,
    "max_luggage_weight": 30, # kg
    "max_luggage_and_passenger_weight": 98_376, # kg
    "max_fuel_capacity": 320_000, # L
    'max_total_weight': 757_000, # kg
    "headwind_consumption": 0.3, # perc
    "tailwind_consumption": -0.1, # perc , negative is efficient
    "snow_weight": 200,
    "taxing_fuel_usage": 450/0.8, # kg
    "max_other_weight_perc": 0.19*0.79, # pass + lugg + cargo in perc
    "max_speed": 1185,
    "empty_flight_fuel": 3246
}   

b777 = {
    "code": "b777",
    "name": "Boeing 777-300ER",

    "average_consumption": 12.7, # L/hour/passenger,
    "ground_consumption": 0.3,
    "take_off_consumption": 13.2,
    "max_passengers": 400,

    "max_other_weight": 0.27, # pass + lugg + cargo in perc
    "max_travel_distance": 16_600,
    "max_luggage": 2,
    "max_luggage_weight": 30, # kg
    "max_luggage_and_passenger_weight": 39_000, # kg
    "max_fuel_capacity": 171_350, # L
    "max_total_weight": 299_371, # kg
    "headwind_consumption": 0.21, # perc
    "tailwind_consumption": -0.15, # perc , negative is efficient
    "snow_weight": 100,
    "max_other_weight_perc": 0.15 ,# pass + lugg + cargo in perc
    "taxing_fuel_usage": 210/0.8, # kg
    "max_speed": 905,
    "empty_flight_fuel": 2735

}

b787 = {
    "code": "b787",
    "name": "Boeing 787-8 Dreamliner",

    "average_consumption": 10.7, # L/hour/passenger,
    "ground_consumption": 0.25,
    "take_off_consumption": 11.2,
    "max_passengers": 246,

    "max_other_weight": 0.34, # pass + lugg + cargo in perc
    "max_travel_distance": 14_140,
    "max_luggage": 2,
    "max_luggage_weight": 23, # kg
    "max_luggage_and_passenger_weight": 34_100, # kg
    "max_fuel_capacity": 156_461, # L
    "max_total_weight": 224_837, # kg
    "headwind_consumption": 0.178, # perc
    "tailwind_consumption": -0.19, # perc , negative is efficient
    "snow_weight": 86,
    "max_other_weight_perc": 0.19 ,# pass + lugg + cargo in perc
    "taxing_fuel_usage": 189/0.8, # kg
    "max_speed": 1085,
    "empty_flight_fuel": 2286

}

b737 = {
    "code": "b737",
    "name": "Boeing 737MAX 8-Passenger",

    "average_consumption": 12.698, # L/hour/passenger,
    "ground_consumption": 0.2,
    "take_off_consumption": 15.2,
    "max_passengers": 189,

    "max_other_weight": 0.34, # pass + lugg + cargo in perc
    "max_travel_distance": 6_510,
    "max_luggage": 1,
    "max_luggage_weight": 23, # kg
    "max_luggage_and_passenger_weight": 25_580, # kg
    "max_fuel_capacity": 96_461, # L
    "max_total_weight": 184_837, # kg
    "headwind_consumption": 0.148, # perc
    "tailwind_consumption": -0.28, # perc , negative is efficient
    "snow_weight": 79,
    "max_other_weight_perc": 0.19 ,# pass + lugg + cargo in perc
    "taxing_fuel_usage": 154/0.8, # kg
    "max_speed": 876,
    "empty_flight_fuel": 1759 # L / hour = fuel of the aircraft only
}



flights = {
    "a380": a380,
    "b777": b777,
    "a350": a350,
    "b787": b787,
    "b737": b737
}

## ======================== INPUTS =======================

def timeFormat(time):
    splitted = time.split(":")
    if (len(splitted) > 2):
        raise Exception("invalid.")
    hours = int(splitted[0])
    if (hours > 12):
        raise Exception("Invalid hours.")
    other = splitted[1:][0]
    
    minutes = int(other[:2])
    if (minutes > 60):
        raise Exception("Invalid minutes")

    day_time = other[2:]

    if (day_time != "PM" and day_time != "AM" and day_time != "am" and day_time != "pm"):
        raise Exception("invalid day.")

    if (day_time == "PM" or day_time == "pm"):
        hours+=12
    return [hours, minutes]

## GET TIME INPUT WITH FORMAT
def getTime():
    while(True):
        try:
            time = input("? Enter the departure time (format HH:MMPM/AM such as 12:00AM): ")
            formTime = timeFormat(time)

            return formTime
        except Exception as err:
            print(err)

## GET TOTAL PASSENGERS ON THE PLANE
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

## GET EXCESSIVE CARGO CARRAIGAGE
def getExcessiveCarrage():
    while(True):
        try:
            excessive_carrage = input("? Enter the weight (kg) of the luggage (press enter or 0 if none): ")
            if not excessive_carrage:
                return 0
            
            excessive_carrage = int(excessive_carrage)
            if (excessive_carrage < 0):
                raise Exception(f"The weight cannot be negative.")
            
            return excessive_carrage
        except Exception as err:
            print(err)

## GET THE WIND DIRECTION INPUT
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

## GET A POSITIVE VALUE
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

## GET AVERAGE LUGGAGE WEIGHT
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

## GET FEMALE RATIO
def getRatio():
    while(True):
        try:
            inp = input("? Enter the female ratio (between 0 and 1, a float number such as 0.4 = 40% women): ")
            if not inp:
                return 0
            
            inp = float(inp)
            if (inp < 0 or inp > 1):
                raise Exception(f"Invalid ratio: value can be between 0 and 1")
            
            return inp
        except Exception as err:
            print(err)

## GET AN INPUT FROM A LIST OF POSSIBLE VALUES
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



## ======================= HELPERS =======================


# GET A RANDOM FLOAT VALUE BETWEEN A AND B
def randomDouble(a, b):
    return a + random.random()*b

## RETURN THE LIST OF FLIGHTS
def getFlights():
    return flights

## COMPUTE AND FIND ANOTHER FLIGHT THAT SATISFIED THE FOLLOWING CONDITIONS
def findAnotherFlight(field, weight):
    possibleFlights = []
    for flight in flights:
        if flights[flight][field] >= weight:
            possibleFlights.append(flight)

    return possibleFlights



## ======================== PRINT ========================

# PRINT THE RESULT OF AN IMPACT IN A TABLE
def printImpact(typee, fuel, distance):
    if fuel == 0 and distance == 0:
        print("No hazzard impact.")
    else:
        print()
        print("=========="*2+ "IMPACT SUMMARY" +"=========="*2)
        print("|  %-50s|" % ("Type: " + typee))
        print("|  %-50s|" % ("Hazzard fuel impact: " + str(round(fuel, 2)) + " Litre"))
        print("|  %-50s|" % ("Hazzard distance impact: " + str(round(distance, 2)) + " km"))
        print("=========="*2+ "==============" + "=========="*2)
        print()

# PRINT THE FLIGHT INFORMATION
def printFlight(flight):
    print("""
        ----------------------
        |AIRCRAFT INFORMATION|
        ----------------------
    """)
    print("\tCode: ", flight["code"])
    print("\tAircraft: ", flight["name"])
    print()
    print("\tAverage consumption: ", flight["average_consumption"], "Litre per hour per passenger")
    print("\tGround consumption: ", flight["ground_consumption"], "Litre per hour per passenger")
    print("\tTake-off consumption: ", flight["take_off_consumption"], "Litre per hour per passenger")
    print("\tHead wind consumption: ", flight["headwind_consumption"]*100, "Litre")
    print("\tTail wind consumption: ", flight["tailwind_consumption"]*100), "Litre"
    print()
    print("\tMaximum passengers: ", flight["max_passengers"])
    print("\tMaximum extra weight percentage: ", flight["max_other_weight"]*100)
    print("\tMaximum travel distance: ", flight["max_travel_distance"], "km")
    print("\tMaximum luggage weight: ", flight["max_luggage_weight"], "kg")
    print("\tMaximum luggage allowance: ", flight["max_luggage"])
    print("\tMaximum passengers and luggage weight: ", flight["max_luggage_and_passenger_weight"], "kg")
    print("\tMaximum fuel capacity: ", flight["max_fuel_capacity"], "Litre")
    print("\tMaximum overall weight: ", flight["max_total_weight"], "kg")
    print("\tMaximum speed: ", flight["max_speed"], "km / h")

# GET HAZZARDS DESCRIPTION FROM HAZZARD CODE
def flightHazzardText(hazzard):
    if hazzard == "deicing":
        return ("🚨 The flight went the process of deicing. Flight is delayed and ground fuel is consumed.")
    elif hazzard == "engine_startup_problem":
        return ("🚨 There were some problems with startin the plane engine. Flight is delayed and ground fuel is consumed.")
    elif hazzard == "ventilation_problem":
        return ("🚨 Cabin ventilation malfunction. Flight is delayed and ground fuel is consumed.")
    elif hazzard == "tail_wind":
        return ("🚨 Air coming from the back of the plane. Helps with fuel consumption and take off.")
    elif hazzard == "litiguous_on_plane":
        return ("🚨 There was a flight onboard the plane when the plane was on land. Flight delayed.")
    elif hazzard == "medical":
        return ("🚨 Medical emergency on land. Fuel is consumed as the motors are active on ground and delayed.")
    elif hazzard == "head_wind":
        return ("🚨 Head wind on runway, More power is required for takeoff, resulting in excessive fuel usage.")
    elif hazzard == "no_runway_available":
        return ("🚨 Could not allocate the runway: needs to take longer distance and delayes are expected")
    elif hazzard == "bad_runway":
        return ("🚨 Bad runway: more fuel consumed because of the inertia.")
    elif hazzard == "thunderstorm_land":
        return ("🚨 There was a thunderstorm on land: fuel consumed as the flight is waiting with active motors.")
    elif hazzard == "raining_land":
        return ("🚨 It is raining on land: fuel consumed as the flight is waiting with active motors.")
    elif hazzard == "fight_air":
        return ("🚨 SEVERE DISRUPTION! The flight had to make an emergency landing to the previous aiport.Some passengers being fighting. Affecting fuel for return.")
    elif hazzard == "medical_emergency":
        return ("🚨 SEVERE DISRUPTION! The flight had to make an medical emergency landing to the previous aiport.Someone is feeling really ill. Affecting fuel for return.")
    elif hazzard == "bird_strike":
        return ("🚨 SEVERE DISRUPTION! The flight had to make an emergency landing to the previous aiport.A number of birds damaged the motor. Affecting fuel for return.")

    elif hazzard == "engine_malfunctioning":
        return ("🚨 SEVERE DISRUPTION! The flight had to make an emergency landing to the previous aiport.The engine stopped working. Affecting fuel for return.")
    elif hazzard == "thunderstorm_air":
        return ("🚨 SEVERE DISRUPTION! Severe storm. Fligh delayed and additional distace added because of route change.")
    elif hazzard == "raining_air":
        return ("🚨 SEVERE DISRUPTION! Severe raining. Fligh delayed and additional distace added because of route change.")
    elif hazzard == "no_taxiing":
        return ("🚨 Problem! No taxing found. Flight is waiting with fuel on ground consumption.")
    elif hazzard == "tailed_landing":
        return ("🚨 Plane failed to land. Making a U turn to try again. Fuel and distance consumed.")
    elif hazzard == "round_turn":
        return ("🚨 Runway was occupied, required taking a round turn.")
    elif hazzard == "failed_landing":
        return "🚨 The flight failed the attempt to land."



## ======================== MAIN =========================


# MAIN FLIGHT SIMULATION THAT REQUIRED 3 PARAMERS
## FLIGHT_NAME = FLEET CODE SUCH AS b777 FOR A BOEING 777
## DESTINATION_DISTANCE = HOW FAR IS THE DESTINATION
## FLIGHT_DURATION = HOW LONG WILL THE FLIGHT TAKE TO REACH THE DESTINATION
def flightSimulation(flight_name, destination_distance, flight_duration):

    plane = flights[flight_name]

    ## TODO: check for input validation

    #input passengers
    passengers = getPassengers(plane["max_passengers"])
    print("Passengers: ", passengers)
    print()

    #input luggage
    luggage = getPositiveInt("? Enter the number of luggage: ", "The onboard luggage value is invalid.")
    print("Total luggage: ", str(luggage))
    print()

    #input average mass luggage
    average_luggage_mass=getAverageLuggage(plane["max_luggage_weight"])
    print("Average luggage weight: ", str(average_luggage_mass))
    print()

    #input extra luggage
    onboard_luggage = getPositiveInt("? Enter the number of onboard luggage: ", "The onboard luggage value is invalid.")
    print("Onboard luggage: ", str(onboard_luggage))
    print()

    #input extra cargo
    extra_cargo_weight = getPositiveInt("? Enter the cargo weight(kg): ", "Invalid cargo weight")
    print("Cargo weight: ", str(extra_cargo_weight))
    print()

    # female ration
    female_male_ratio = getRatio()
    print("Female ratio: ", str(female_male_ratio))
    
    male = 1 - female_male_ratio
    print("Male ratio: ", str(male))
    print()

    total_passenger_luggage_weight = male * passengers * 88 + female_male_ratio * passengers * 67 + luggage * average_luggage_mass + onboard_luggage * 8
    gas_required_per_hour = (passengers + luggage/3+extra_cargo_weight/75+onboard_luggage/8) * plane["average_consumption"] + plane["empty_flight_fuel"]

    ## CHECKING 
    ## Choose another flight if the current one cannot satisfy the need.
    print("Check #1: Total luggage and passenger weight:", total_passenger_luggage_weight, "kg")
    if (total_passenger_luggage_weight >= plane["max_luggage_and_passenger_weight"]):
        print("❌ Excessive passengers and/or luggage. There is no enought space in the plane. Maximum possible:", plane["max_luggage_and_passenger_weight"], "kg")

        possibleFlights = findAnotherFlight("max_luggage_and_passenger_weight", total_passenger_luggage_weight)
        if (len(possibleFlights) == 0):
            print("There is no flight that can satisfy the weight. We are sorry. This flight was the biggest available.")
            return
        print()
        print("The flight options are: ")
        for flight in possibleFlights:
            printFlight(flights[flight])
        
        print()
        code = input("Please enter the flight code: ")
        new_plane = flights[code]
        if not new_plane:
            print("Invalid code. Terminating program.")
            return
        
        plane = new_plane

        print()
        print("New aircraft selected: ")
        printFlight(plane)
        print()
        
    
    ## CHECKING IF TOTOAL WEIGHT CAN BE CARRIED
    print("Result #1: Flight possible.")
    print()
    print("Check #2: Total overall weight:", total_passenger_luggage_weight+extra_cargo_weight, "kg")

    if (total_passenger_luggage_weight+extra_cargo_weight >= plane["max_other_weight"] * plane["max_total_weight"]):
        print("❌ Flight is overweighted. The flight cannot carry this much weight")

        possibleFlights = findAnotherFlight("max_other_weight", total_passenger_luggage_weight+extra_cargo_weight)
        if (len(possibleFlights) == 0):
            print("There is no flight that can satisfy the weight. We are sorry.")
            return
        print()
        print("The flight options are: ")
        for flight in possibleFlights:
            printFlight(flights[flight])
        
        print()
        code = input("Please enter the flight code: ")
        new_plane = flights[code]
        if not new_plane:
            print("Invalid code. Terminating program.")
            return
        
        plane = new_plane

        print()
        print("New aircraft selected: ")
        printFlight(plane)
        print()

    
    ## CHECK IF THE FUEL CONSUMPTION IS POSSIBLE GIVEN THE TOTAL FUEL
    print("Result #2: Flight possible.")
    print()
    print("Check #3: Fuel consumption", gas_required_per_hour * flight_duration, "Litre")
    if (gas_required_per_hour * flight_duration >= plane["max_fuel_capacity"]):
        print("❌Insufficient fuel capacity. The flight cannot make to the destination. Required: ", gas_required_per_hour * flight_duration)

        possibleFlights = findAnotherFlight("max_fuel_capacity", gas_required_per_hour * flight_duration)
        if (len(possibleFlights) == 0):
            print("There is no flight that can satisfy the fuel. We are sorry.")
            return
        print()
        print("The flight options are: ")
        for flight in possibleFlights:
            printFlight(flights[flight])
        
        print()
        code = input("Please enter the flight code: ")
        new_plane = flights[code]
        if not new_plane:
            print("Invalid code. Terminating program.")
            return
        
        plane = new_plane

        print()
        print("New aircraft selected: ")
        printFlight(plane)
        print()

    
    print("Result #3: Flight possible.")
    total_passenger_luggage_weight += extra_cargo_weight

    print()
    # departure time
    departureTime = getTime()
    print("Departure time: ", str(departureTime))
    print()

    # input weather
    weatherConditions = ["snow", "rain", "fog", "sun"]
    weather = getInputWithComparisonList("? Enter the weather condition " + str(weatherConditions) + ": ", weatherConditions, "sun") ## or raining, sun, fog
    print("Weather condition: ", weather)
    print()


    #input wind direction
    windConditions = ["head_wind", "tail_wind"]
    wind_direction = getWindDirection()# or tail
    print("Wind direction: ", wind_direction)
    print()

    # DISPLAYING INITIAL CALULATIONS
    print("="*37 + "INITIAL CALCULATION" + "="*37)
    print("| %-40s | %20s %-8s |" % ("Total weight", round(total_passenger_luggage_weight, 2), "kg"))
    print("| %-40s | %20s %-8s |" % ("Gas required per hour", round(gas_required_per_hour, 2), "Litre/hour"))
    print("| %-40s | %20s %-8s |" % ("Total gas for travel", round(gas_required_per_hour * flight_duration, 2), "Litre"))
    print("="*86)



    ## DEFINING THE LIST OF HAZZARDS: EACH TYPE OF ROUTE HAS ITS OWN HAZZARDS
    hazzards_on_land_snow = ["deicing", "engine_startup_problem", "ventilation_problem", "tail_wind"]
    #["snow", "attack", "bad_passenger", "medical", "engine_problem", "air_conditioning_problem", "late_passenger", "no_runway", "deicing"]

    hazzards_on_land = ["litiguous_on_plane", "medical", "thunderstorm_land", "raining_land"]

    hazzards_on_runway = ["no_runway_available", "bad_runway"]

    hazzards_in_air = ["fight_air", "medical_emergency", "bird_strike", "engine_malfunctioning", "thunderstorm_air", "raining_air"]

    hazzards_on_landing = ["no_taxiing", "bad_runway"]
    hazzards_on_before_landing = ["failed_landing", "round_turn"]

    ## run every 10km
    ## after 200km, skip by 50km because in air

    total_fuel_hazzards = 0
    total_distance_hazzards = 0
    distance_travelled = 0
    air_hazzards = 0
    runway_hazzards = 0
    total_hazzards = []

    ## HANDING IMPACT OF EACH HAZZARD. 
    ## IT CAN IMPACT ON THE FUEL, DISTANCE, WEIGHT OR DELAY
    def calculateImpactOfHazzard(hazzard, distance_travelled):
        additional_fuel = 0
        additional_distance = 0
        additional_weight = 0
        flight_delay = 0
        print(flightHazzardText(hazzard))

        
        ## delay, additiona fuel
        if hazzard == "deicing" or hazzard == "ventilation_problem" or hazzard == "engine_startup_problem":
            delay = randomDouble(0.3, 1.7)
            flight_delay+=delay
            additional_fuel+=(plane["taxing_fuel_usage"] * delay)
        
        # dealy and additional fuel
        elif hazzard == "medical":
            delay = randomDouble(0.3, 2.5)
            flight_delay+=delay
            additional_fuel+=plane["taxing_fuel_usage"]
        
        # additional fuel and distance increased
        elif hazzard == "head_wind":
            additional_distance+=20
            additional_fuel+=1.1*gas_required_per_hour*0.50 # For 30 minutes from takeoff to stability, there is a consumption higer than 10% of average fuel
        
        elif hazzard == "tail_wind":
            additional_fuel-=1.1*gas_required_per_hour*0.50 # For 30 minutes from takeoff to stability, there is a consumption higer than 10% of average fuel
        # could not allocate the runway: needs to take longer distance and delayes are expected
        
        elif hazzard == "no_runway_available":
            additional_distance = 10
            additional_fuel+=0.05 * gas_required_per_hour
            flight_delay = randomDouble(0.1, 0.9); # from 0.1 hour to 0.9 hours
        
        elif hazzard == "litiguous_on_plane":
            ## flight gets delayed
            flight_delay+=randomDouble(0.1, 0.4)
        
        elif hazzard == "fight_air":
            # there was a fight when the flight was in air
            ## consequence: emergency descending to the previous airport, requiring more fuel
            ## we can consider that the flight returns to the original airport and does not descend to the near airport, for simplicity
            after = randomDouble(0.05, 0.2) # in between 5% and 20% of total distance
            additional_distance+=distance_travelled*2
            flight_delay+=flight_duration*after*2
        
        elif hazzard == "medical_emergency":

            ## TODO: insert petrol 
            after = randomDouble(0.05, 0.4) # in between 5% and 20% of total distance
            additional_distance+=distance_travelled*2
            flight_delay+=flight_duration*after*2
        
        elif hazzard == "bird_strike":
            after = randomDouble(0.1, 0.2) # in between 5% and 20% of total distance
            additional_distance+=distance_travelled*2
            flight_delay+=flight_duration*after*2
        
        elif hazzard == "engine_malfunctioning":
            after = randomDouble(0.1, 0.35) # in between 5% and 20% of total distance
            additional_distance+=distance_travelled*2
            flight_delay+=flight_duration*after*2
        
        elif hazzard == "failed_landing":
            # descending: consuming less gas
            additional_fuel-=0.8*gas_required_per_hour*0.2 #
            # ascending again
            additional_fuel+=1.2*gas_required_per_hour*0.15
            additional_distance+=200
        
        # NO TAXING FOUND: FUEL FOR WAITING AND MORE DELAY FOR PASSENGERS
        elif hazzard == "no_taxiing":
            delay = randomDouble(0.3, 1.5)
            flight_delay+=delay
            additional_fuel+=plane["taxing_fuel_usage"]
        
        # THUNDERSTORM: CHANGE OF DIRECTION: MORE DISTANCE AND DELAY
        elif hazzard == "thunderstorm_air" or hazzard == "raining_air":
            randDistance = randomDouble(120, 500)
            flight_delay+=randDistance*plane["max_speed"] # finding delay time from distance and max speed in air
            additional_distance+=randDistance
        
        ## THUNDERSTORM ON LAND: DELAY, FUEL CONSUPTION HAND HEAVY WEIGHT WHEN LIFTING OFF
        elif hazzard == "thunderstorm_land" or hazzard == "raining_land":
            headwindHazzard = calculateImpactOfHazzard("head_wind", distance_travelled)
            additional_distance+=headwindHazzard["distance"]
            additional_fuel+=headwindHazzard["fuel"]
            additional_weight+=headwindHazzard["weight"]
            flight_delay+=headwindHazzard["delay"]
            additional_fuel+=100
        
        ## BAD RUNWAY: MORE 15% CONSUMPTION 
        elif hazzard == "bad_runway":
            additional_fuel+=0.2*gas_required_per_hour*0.15
        
        ## ROUND TURN : FAILED LANDING ATTEMPT: MORE DISTANCE TO COVER
        elif hazzard == "round_turn":
            randDistance = randomDouble(50, 150)
            additional_distance+=randDistance
        
        else:
            print("Hazzard not recognized in the system.")

        print()
        printImpact(hazzard, additional_fuel, additional_distance)

        ## RETURNING THE CALCULATION RESULTS
        result = {
            "hazzard": hazzard,
            "fuel": additional_fuel,
            "weight": additional_weight,
            "distance": additional_distance,
            "delay": flight_delay
        }
        ## APPENDING TO THE LIST OF HAZZARDS
        total_hazzards.append(result)
        return result

    

    ## GENERATING A BUNCH OF RANDOM HAZZARDS AND CALCULATE THE HAZZARD
    def generateRandomFactorAndCalculateImpact(hazzards, total):
        randHazzards = random.randint(0, total)
        print("Randomizing impact result: ", randHazzards)

        ## CARRY TOTAL IMPACT PER SIMULATION
        total_distance = 0
        total_fuel = 0
        total_delay = 0
        total_weight = 0

        ## LOOP FOR A RANDOM VALUE BETWEEN O AND TOTAL RANDOM HAZZARDS FOUND
        for i in range(randHazzards):
            if len(hazzards) == 0:
                break
            # OTHER RANDOMIZATION FOR THE PROBABILITY OF HAVING THE HAZZARD
            randFactor = random.randint(0, len(hazzards)-1)
            ## FINDINT THE HAZZARD CODE FROM THE LIST
            hazzard = hazzards[randFactor]
            
            ## REMOVE THE HAZZARD FROM THE LIST: WILL NOT HAPPENA AGAIN
            hazzards.pop(randFactor)

            # check for the type of hazzard
            impact = calculateImpactOfHazzard(hazzard, distance_travelled)
            total_distance+=impact["distance"]
            total_fuel+=impact["fuel"]
            total_delay+=impact["delay"]
            total_weight+=impact["weight"]

            #print(f"{impact}")

        ## NOT HAZZARD FOUND
        if (total_fuel == 0 and total_distance == 0):
            print("No hazzard impact.")

        ## RETURNING THE IMPACT
        total_impact = {
            "distance": total_distance,
            "fuel": total_fuel,
            "delay": total_delay,
            "weight": total_weight
        }
        #print("Total impact after generation: ", total_impact)
        return total_impact


    # impact because of wind direction
    ## INITIAL IMPACT
    impact = calculateImpactOfHazzard(wind_direction, distance_travelled)
    total_fuel_hazzards+=impact["fuel"]
    total_distance_hazzards+=impact["distance"]
    
    ## LOOP UNTIL DESTINATION IS NOT REACHED
    while(distance_travelled < destination_distance):
        print()
        print()
        ## HAZZARDS ON LAND
        if (distance_travelled < 10):
            ## hazzards on land
            impact = {}
            print("_"*70)

            ## GENERATING HAZZARS ON LAND WITH SNOW
            if (weather == "snow"):
                print()
                print("GENERATING RANDOM HAZZARDS FOR SNOW WEATHER")
                impact = generateRandomFactorAndCalculateImpact(hazzards_on_land_snow, 3)
            else:
                ## GENERATING HAZZARS ON LAND WITHOUT SNOW
                print()
                print("GENERATING RANDOM HAZZARDS FOR LAND")
                impact = generateRandomFactorAndCalculateImpact(hazzards_on_land, 3)
                
            ## UPDATE FULE AND DISTANCE
            total_fuel_hazzards+=impact["fuel"]
            total_distance_hazzards+=impact["distance"]
        
        ## TAKEOFF: 10-30KM
        elif (distance_travelled > 10 and distance_travelled < 30):
            ## hazzards on runway
            ## TODO: make the time function
            ## RENDER HAZZARDS ONLY IF THERE IS HIGH PEEK IN FLIGHTS
            if (runway_hazzards < 1 and departureTime[0] >= 4 and departureTime[0] <= 10):
                print("_"*70)
                print()
                print("GENERATING RANDOM HAZZARDS FOR TAKE-OFF")
                impact = generateRandomFactorAndCalculateImpact(hazzards_on_runway, 1)


                total_fuel_hazzards+=impact["fuel"]
                total_distance_hazzards+=impact["distance"]
        
        # HAZZARDS IN AIR: 30KM TO 60% OF TOTAL TRAVEL DISTANCE
        elif (distance_travelled > 30 and distance_travelled < 0.6*destination_distance):
            # hazzards in air
            ## HAZZARDS ARE LIMITED TO 2 HAZZARDS IN AIR ONLY
            ## THIS IS BECAUSE AIR HAZZARS HAVE A BIG IMPACT ON FUEL, SUCH AS RETURN TO THE PREVIOUS AIRPORT
            if (air_hazzards < 2):
                print("_"*70)
                print()
                print("GENERATING RANDOM HAZZARDS IN AIR")
                impact = generateRandomFactorAndCalculateImpact(hazzards_in_air, 2)


                total_fuel_hazzards+=impact["fuel"]
                total_distance_hazzards+=impact["distance"]
                air_hazzards+=1
            
        ## LANDING HAZZARDS
        elif (distance_travelled>0.9*destination_distance and distance_travelled < 0.95 * destination_distance):
            # on landing
            # peak times between 9:00AM AND 12:00PM OR 14:00 OR 16:00
            print("_"*70)
            print()
            print("GENERATING RANDOM HAZZARDS FOR BEFORE LANDING")
            impact = generateRandomFactorAndCalculateImpact(hazzards_on_before_landing, 2)

            total_fuel_hazzards+=impact["fuel"]
            total_distance_hazzards+=impact["distance"]
                

            # taxiing HAZZARS
        elif (distance_travelled>0.95*destination_distance):
            print("_"*70)
            print()
            print("GENERATING RANDOM HAZZARDS FOR TAXING AFTER LAND")
            impact = generateRandomFactorAndCalculateImpact(hazzards_on_landing, 2)

            total_fuel_hazzards+=impact["fuel"]
            total_distance_hazzards+=impact["distance"]
            

           
            
        print("-"*70)
        print("Approximate fuel consumption based on 80-percent average speed:", round(gas_required_per_hour * (distance_travelled / (plane["max_speed"]*0.8))+total_fuel_hazzards + gas_required_per_hour * (total_distance_hazzards / (plane["max_speed"]*0.8)), 2), "Litre")
        print("Distance travelled:", distance_travelled, "km")
        print()

        ## HOW PRECISE SHOULD THE OUTPUT BE
        ## FOR FIRST 200 KM, SKIP BY 7.5KM PER LOOP
        if (distance_travelled < 200):
            distance_travelled+=7.5
        else:
            ## SKIP BY 20 KM PER LOOP
            distance_travelled+=30
            
    print()
    print()

    ## FINAL CALCULATIONS OF THE DISTANCE TO FUEL, OVERALL FUEL AND FUEL WEIGHT
    distance_to_fuel = gas_required_per_hour * (total_distance_hazzards / (plane["max_speed"]*0.8))
    total_overall_consumption = (gas_required_per_hour * (distance_travelled / (plane["max_speed"]*0.8))+total_fuel_hazzards + gas_required_per_hour * (total_distance_hazzards / (plane["max_speed"]*0.8))) ## gas_required_per_hour * flight_duration + distance_to_fuel ## 
    fuel_weight = total_overall_consumption * 0.84 # 1L = 0.84 kg

    ## DISPLAYING FINAL RESULT IN A TABLE
    print("="*37 + "=============" + "="*26)
    print("="*37 + "SUMMARY TABLE" + "="*26)
    print("| %-40s | %20s %-8s |" % ("Total duration", round(flight_duration), "hours"))
    print("| %-40s | %20s %-8s |" % ("Total weight", round(total_passenger_luggage_weight, 2), "kg"))
    print("| %-40s | %20s %-8s |" % ("Gas per hour", round(gas_required_per_hour, 2), "Litre"))
    print("| %-40s | %20s %-8s |" % ("Total fuel for original distance", round(gas_required_per_hour * flight_duration, 2), "Litre"))
    print("| %-40s | %20s %-8s |" % ("Total fuel consumed by hazzards", round(total_fuel_hazzards, 2), "Litre"))
    print("| %-40s | %20s %-8s |" % ("Total distance increase", round(total_distance_hazzards, 2), "km"))
    print("| %-40s | %20s %-8s |" % ("Total fuel because of distance increase", round(distance_to_fuel, 2), "Litre"))
    print("| %-40s | %20s %-8s |" % ("Total fuel overall", round(total_overall_consumption, 2), "Litre"))
    
    print("="*75)

    print()
    print("List of total hazzards that happened in the simulation.")
    print()
    ## RENDERING THE LIST OF HAZZARS
    for hazzard in total_hazzards:
        
        print(flightHazzardText(hazzard["hazzard"]))
        print("Fuel: " + str(round(hazzard["fuel"])) +" litre")
        print("Distance: " + str(round(hazzard["distance"])) + " km")
        print()


    return {
        "passengers": passengers,
        "luggage": luggage,
        "onboard_luggage": onboard_luggage,
        "extra_cargo": extra_cargo_weight,
        "departure_time": departureTime,
        "weather": weather,
        "wind_direction": wind_direction,
        "total_duration": flight_duration,
        "total_weight": total_passenger_luggage_weight,
        "total_weight_with_fuel": fuel_weight + total_passenger_luggage_weight,

        "gap_per_hour": gas_required_per_hour,
        "total_fuel_without_hazzards": gas_required_per_hour * flight_duration,
        "total_fuel_for_hazzards": total_fuel_hazzards,
        "total_distance_increase": total_distance_hazzards, # this represents hazzards that required fuel directly
        "total_fuel_by_distance_hazzards_increase": distance_to_fuel, # this calculates the fuel from the hazzards that added more distance. 
        "total_overall_fuel": total_overall_consumption,
        "total_fuel_weight": fuel_weight
    }




#simulate("b777", 5000, 6.5)
    
## we might be assigned the headwind side if too much traffic and flight is late