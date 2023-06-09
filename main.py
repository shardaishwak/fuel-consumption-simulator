import random

asci = """

    ____             __                         __    __     ______                _____ _                 __      __            
   / __ \___  ____ _/ /    _      ______  _____/ /___/ /    / ____/___ ______     / ___/(_)___ ___  __  __/ /___ _/ /_____  _____
  / /_/ / _ \/ __ `/ /    | | /| / / __ \/ ___/ / __  /    / / __/ __ `/ ___/     \__ \/ / __ `__ \/ / / / / __ `/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /     | |/ |/ / /_/ / /  / / /_/ /    / /_/ / /_/ (__  )     ___/ / / / / / / / /_/ / / /_/ / /_/ /_/ / /    
/_/ |_|\___/\__,_/_/      |__/|__/\____/_/  /_/\__,_/     \____/\__,_/____/     /____/_/_/ /_/ /_/\__,_/_/\__,_/\__/\____/_/     
                                                                                                                                 
                                                    By Ishwak Sharda (2023)


                                Welcome to this amazing gas simulator that lets you simulate
                                the millage consumption of your car or even airplane flights!

                                Plan your fuel costs and usage in advance with this
                                application and compare fuel prices with different 
                                petrol services in Canada.

                                Furthermore, analyze how much will a flight trip will consume
                                your favourite destination!
                                                                                                      
"""
print(asci)

#flights = getFlights()
#print(flightSimulation("b777", 10000, 12.3))

## ==================== MODELS =====================

def defineFlightRoute(company, plane, departure, arrival, distance, duration, flight_type):
    return {
        "company": company,
        "plane": plane,
        "route": [departure, arrival],
        "distance": distance,
        "duration": duration,
        "flight_type": flight_type
    }

def defineAirport(code, name, country, city):
    return {
        "name": name,
        "code": code,
        "country": country,
        "city": city
    }

def defineGasStation(eid, name, premiumCost, dieselCost, petrolCost):
    return {
        "id": eid,
        "name": name,
        "premium_cost": premiumCost,
        "diesel_cost": dieselCost,
        "petrol_cost": petrolCost
    }

def defineCarRoute(departureCity, arrivalCity, distance, time, trafficPoints, trafficLightPoints, highwayPoints, cityPoints, roadConditionPoints):
    return {
        "departureCity": departureCity,
        "arrivalCity": arrivalCity,
        "trafficPoints": trafficPoints,
        "trafficLightPoints": trafficLightPoints,
        "highwayPoints": highwayPoints,
        "distance": distance,
        "time": time,
        "cityPoints": cityPoints,
        "roadConditionPoints": roadConditionPoints
    }

def defineCar(id, manufacturer, model, engine, power, gear, seat, premium, city_millage, highway_millage, average_comb_city_highway, average_millage_per_100l, fuel_capacity, weight):
    return {
        "id": id,
        "manufacturer": manufacturer,
        "model": model,
        "engine": engine,
        "power": power,
        "seat": seat,
        "premium": premium,
        "city_millage": city_millage,
        "highway_millage": highway_millage,
        "average_comb_city_highway": average_comb_city_highway,
        "average_millage_per_100l": average_millage_per_100l,
        "fuel_capacity": fuel_capacity,
        "weight": weight
    }


domesticFlights = []
internationalFlights = []
airports = []
carRoutes = []
gasStations = []
cars = []

## ==================== DATA GATHERING ====================


domesticFlights.append(defineFlightRoute("Wizz air", "b777", "YVL", "YUL", 4000, 4.5, "domestic"))
domesticFlights.append(defineFlightRoute("Wizz air", "b787", "YVL", "YYL", 3343, 4.2, "domestic"))

domesticFlights.append(defineFlightRoute("Air Canada", "a350", "YYL", "YUL", 550, 0.9, "domestic"))
domesticFlights.append(defineFlightRoute("Flair air", "b737", "YVL", "YYC", 950, 1.45, "domestic"))
domesticFlights.append(defineFlightRoute("Flair air", "b737", "YYL", "YYC", 2705, 3.8, "domestic"))
domesticFlights.append(defineFlightRoute("Flair air", "b737", "YUL", "YYC", 3006, 4.18, "domestic"))

domesticFlights.append(defineFlightRoute("Flair air", "b737", "YVL", "YOW", 3552, 4.8, "domestic"))



## calgary to vancouver
## calgary to toronto
## calgary to montreal
## vancouver to montreal
## vancouver to toronto



internationalFlights.append(defineFlightRoute("Emirates", "a380", "YYL", "DXB", 10900, 12.75, "international")) # ok
internationalFlights.append(defineFlightRoute("Air India", "b777", "YYL", "DHX", 11653, 13.5, "international")) # ok
internationalFlights.append(defineFlightRoute("Emirates", "a380", "YYL", "MXP", 7400, 9.75, "international")) # ok
internationalFlights.append(defineFlightRoute("United", "b737", "YVL", "LAX", 1804, 2.9, "international"))  ## ok b737Max
internationalFlights.append(defineFlightRoute("Air Canada", "a350", "YVL", "MXP", 7400, 10.5, "international")) #ok - check flight add a330
internationalFlights.append(defineFlightRoute("Air Canada", "b777", "YYL", "LHR", 5941, 6.9, "international")) #ok
internationalFlights.append(defineFlightRoute("Air France", "b787", "CDG", "YVL", 10680, 9.75, "international")) # b787
internationalFlights.append(defineFlightRoute("ANA", "b787", "HND", "YVL", 7845, 9.98, "international")) # b787
internationalFlights.append(defineFlightRoute("Americal Airline", "a350", "YYC", "LAX", 6287, 5.3, "international")) # b787
internationalFlights.append(defineFlightRoute("Americal Airline", "b777", "YVL", "MXP", 7400, 10.2, "international")) # b787




# seattle to los angeles
# vancouver to los angeles
# vancouver to london



airports.append(defineAirport("YVL", "Vancouver International Airport", "Canada", "Vancouver"))
airports.append(defineAirport("YUL", "Montreal International Airport", "Canada", "Montreal"))
airports.append(defineAirport("YYL", "Toronto Pearson-Trudeau International Airport", "Canada", "Toronto"))
airports.append(defineAirport("MXP", "Malpensa International Airport", "Italy", "Milan"))
airports.append(defineAirport("DHX", "Indra-Gandhi International Airport", "India", "New Delhi"))
airports.append(defineAirport("DXB", "Dubai International Airport", "United Arab Emirated", "Dubai"))
#airports.append(defineAirport("SEA", "Seattle International Airport", "United States of America", "Seattle"))
airports.append(defineAirport("LAX", "Los Angeles International Airport", "United States of America", "Los Angeles"))
airports.append(defineAirport("LHR", "Heathrow Airport", "United States of America", "Los Angeles"))
airports.append(defineAirport("CDG", "Paris Charles de Gaulle Airport", "France", "Paris"))
airports.append(defineAirport("HND", "Haneda Airport", "Japan", "Tokyo"))
airports.append(defineAirport("YYC", "Calgary International Airport", "Canada", "Calgary"))
airports.append(defineAirport("YOW", "Ottawa International Airport", "Ottawa", "Ottawa"))


## calgary airport
## los angeles
## new york
## japan
## london

cars.append(defineCar("audi_rsq8", "Audi", "RSQ8 2022", "Twin-turbocharged and intercooled DOHC 32-valve V-8", 591,"8-speed automatic",5,True,11.9,17.5,15,6.7,85,2490))
cars.append(defineCar("porsche_panamera_4s", "Porsche", "Panamera 4S", "6-cylinder", 473, "8-speed dual clutch automatic", 5, True, 12.8, 9.8, 11.4, 5, 80, 2100))
cars.append(defineCar("honda_civic", "Honda", "Civic 2022 Hatchback", "4 cylinder", 129, "5-speed automatic", 5, False, 7.7, 6.3, 7.1, 3, 46, 1256))
cars.append(defineCar("lamborgini_evo", "Lamborghini", "Huracán EVO Coupè", "DOHC 40-valve V-10", 631, "7-speed dual-clutch automatic", 2, True, 18, 12.9, 15.7, 6.7, 83, 1.339))
cars.append(defineCar("volkswagen_golf", "Volkswagen", "Golf 2021", "4-cylinder", 147, "6-speed manual", 5, False, 8.2, 6.5, 7.5, 3, 50, 1425))

# road conditions: fog, mud, wet, bumpy, construction
carRoutes.append(defineCarRoute("University of the Fraser Valley (Abbotsford) (BC)", "Vancouver (BC)",  70, 0.95, [[35, 45], [75, 100]], [[0, 8], [85, 100]], [[7.5, 65]], [[0, 7.5], [65, 100]], [[0, 5, "mud"]]))
carRoutes.append(defineCarRoute("Vancouver (BC)", "Seattle (USA)", 156, 1.98, [[0, 20], [45, 65]], [[0, 20], [70, 100]], [[20, 70]], [[0, 20], [65, 100]], [[32,67, "wet"]]))
carRoutes.append(defineCarRoute("Toronto (Ontario)", "University of Montreal (Quebec)", 543, 5.07, 
    [[0, 8], [34, 39], [67, 73], [96, 100]], 
    [[0, 8], [25, 27], [63,67], [90, 100]], 
    [[10, 89]], 
    [[0, 8], [90, 100]], 
    [[35,37, "construction"]]
))
carRoutes.append(defineCarRoute("Vancouver (BC)", "Kelowna (BC)", 387, 4.2, [[0, 10], [89, 95]], [[0, 10], [90, 100]], [[20, 90]], [[0, 10], [90, 100]], [[40,76, "bumpy"]]))
carRoutes.append(defineCarRoute("University of the Fraser Valley (Abbotsford) (BC)", "Kelowna (BC)", 325, 3.5, [[0, 1], [89, 90]], [[0, 2], [98, 100]], [[2, 96]], [[0, 2], [98, 100]], []))
carRoutes.append(defineCarRoute("Ottawa (Ontario)", "Toronto (Ontario)", 410, 4.42, [[0, 8], [23, 45], [23, 78], [96, 100]], [[0, 10], [90, 98]], [[20, 89]], [[0, 10], [93, 100]], []))




gasStations.append(defineGasStation("g1", "Esso",  1.859, 1.789, 1.679))
gasStations.append(defineGasStation("g2", "Petrol Canada", 2.005, 2.029, 1.749))
gasStations.append(defineGasStation("g3", "Shell", 2.005, 2.029, 1.749))
gasStations.append(defineGasStation("g4", "Chevron", 1.92, 1.859, 1.689))






## ===================== INPUTS =====================

factors = ["protest", "accident_on_road", "construction", "muddy_road"]


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

## ===================== HELPERS ====================


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
    
def isBetweenInterval(array, value, totalDistance):
    ## [[1,2], [10, 20]]
    
    for interval in (array):
        if len(interval) < 2:
            raise Exception("Invalid interval. The interval should be of format [a, b, ...n]")
        if (value >= interval[0]/100*totalDistance and value <= interval[1]/100*totalDistance):
            return True
    return False

def isBetweenIntervalRoadConditions(array, value, totalDistance):
    ## [[1,2], [10, 20]]
    if len(array) == 0:
        return [False]
    for interval in (array):
        if len(interval) < 3:
            raise Exception("Invalid interval. The interval should be of format [a, b, type]")
        if (value >= interval[0]/100*totalDistance and value <= interval[1]/100*totalDistance):
            return [True, interval[2]]
    return [False, interval[2]]

def generateRandomLight():
    randomLight = random.randint(0, 3)

    ## 60% probability of red light
    ## 20% probability of yellow light
    ## 20% probability of green light
    if (randomLight <=1):
        return "red"
    elif randomLight ==2:
        return "yellow"
    else:
        return "green"

def factorImpact(factor, average, delta):
    consumption = 0
    distanceIncrease = 0
    if factor == "protest":
        # car is stop, and is consuming 0.15 of the average consumption
        consumption = average/100*0.65*delta
    elif factor == "construction":
        ## change road or not
        randChange = random.randint(0, 1)
        if (randChange == 1):
            ## road changed, added more 
            distanceIncrease+=5
        else:
            consumption+=average/100*delta
    elif factor == "accident_on_road":
        ## more consumption as the car has to ride slowly
        consumption+=average/100*1.2*delta
    elif factor == "muddy_road":
        consumption+=average/100*1.15*delta

    printImpact(factor, consumption, distanceIncrease)

    return {
        "consumption": consumption,
        "distance": distanceIncrease,
        "factor": factor
    }

def getCars():
    return cars

def getCar(code):
    for car in cars:
        if car["code"] == code:
            return car

def findFactorIndex(arr, factor):
    for i in range(len(arr)):
        if arr[i]["factor"] == factor:
            return i
    return -1

def joinFactors(factorsImpact):
    arr = []

    for factor in factorsImpact:
        index = findFactorIndex(arr, factor["factor"])
        if (index == -1):
            arr.append({"factor": factor["factor"], "consumption": factor["consumption"], "distance": factor["distance"]})
        else:
            arr[index]["consumption"]+=factor["consumption"]
            arr[index]["distance"]+=factor["distance"]

    return arr

def generateRandomFactor(factors):
    rand = random.randint(0, len(factors)-1)
    return factors[rand]

def calculateInitialMillage(car, average, total_weight, tyreCondition, weatherCondition, timeOfYear, mood, experience, serviced):
    ## average affect by passengers
    averages = 0
    factors = 0
    
    averages += average * (car["weight"] / total_weight)*1.1
    factors+=1

    # average affect by tyre condition
    if (tyreCondition == "bad"):
        averages += 0.9 * average ## affect 10%
        factors+=1

    # average affect by weather condition
    averages += (85 + random.random()*7)/100 * average # affect between 8-15%
    factors+=1


    if (not serviced):
        # a car that has not been serviced is affected by 4%
        averages += 0.04 * average
        factors+=1
    
    if (mood == "bad"):
        # a bad mood driver does effect the average by 7%
        averages += 0.07 * average
        factors+=1
    
    if (experience > 10):
        # an experienced driver increases the average by 25%!
        averages += 1.25 * average
        factors+=1

    else:
        # a noval driver increases the fuel consumptionby 11%
        averages += 0.89 * average
        factors+=1

    if (timeOfYear == "winter" or timeOfYear == "fall"):
        averages += 0.95 * average
        factors+=1
    else:
        print("No air conditioning")

    if (weatherCondition == "snow" or weatherCondition == "rainy"):
        averages += 0.9 * average
        factors+=1
    
    if (weatherCondition == "fog"):
        averages += 0.94 * average
        factors+=1

    return ((averages)/factors)

    # average affect by time of the year
    

def findGasStations(total, premium = False):
    gasSt = []
    mini = 0
    best = gasStations[0]
    if premium:
        mini = gasStations[0]["premium_cost"]
    else:
        mini = gasStations[0]["petrol_cost"]
    for i in range((total)):
        gas = gasStations[i]
        price = 0
        if premium:
            price = gas["premium_cost"]
        else:
            price = gas["petrol_cost"]
        
        if price < mini:
            best = gas
            mini = price
        gasSt.append(gas)
    return [gasSt, best]

def printGasStations(stations, bestName):
    print("="*28 + " GAS STATIONS " + "="*28)
    print("| %-2s | %-20s | %-12s | %-10s | %-10s |" % ("ID", "Station", "Premium (L)", "Diesel (L)", "Petrol (L)"))
    print("| %-2s | %-20s | %-12s | %-10s | %-10s |" % ("", "", "", "", ""))
    for i in range(len(stations)):
        gas = stations[i]
        if bestName == gas["name"]:
            print("| %-2d | %-20s | %-12f | %-10f | %-10f |" % (i+1, gas["name"] + " (best)", gas["premium_cost"], gas["diesel_cost"], gas["petrol_cost"]))
        else:
            print("| %-2d | %-20s | %-12f | %-10f | %-10f |" % (i+1, gas["name"], gas["premium_cost"], gas["diesel_cost"], gas["petrol_cost"]))
    print("="*70)

def getCities():
    validSet = []
    for route in carRoutes:
        dep = route["departureCity"]
        arr = route["arrivalCity"]

        if dep not in validSet:
            validSet.append(dep)
        if arr not in validSet:
            validSet.append(arr)

    return validSet

def getRoutesFromCity(city):
    routes = []
    for route in carRoutes:
        dep = route["departureCity"]
        arr = route["arrivalCity"]

        if dep == city or arr == city:
            routes.append(route)
    return routes



## ===================== PRINTS =====================


def printImpact(factor, fuel, distance):
    print()
    print("=========="*2+ f"=== HAZARD! ==" +"=========="*2)
    print("|  %-50s|" % ("Type: " + factor))
    if fuel > 0:
        print("|  %-50s|" % ("Hazzard fuel impact: " + str(round(fuel, 2)) + " Litre"))

    if distance > 0 :
        print("|  %-50s|" % ("Hazzard distance impact: " + str(round(distance, 2)) + " km"))

    print("=========="*2+ "==============" + "=========="*2)
    print()

def printTrafficLight(color, fuel):
    print()
    print("==========="*2+ f"{color}" +"=========="*2)
    if fuel > 0:
        print("|  %-50s|" % ("Fuel impact: " + str(round(fuel, 2)) + " Litre"))
        print("=========="*2+ "==============" + "=========="*2)
    print()


## =================== CAR MAIN =====================

def carPrompts():
    cities = getCities()
    cars = getCars()

    print("Here are the recorded cities: ")
    for i in range(len(cities)):
        city = cities[i]
        print(f"\t [{i+1}]: {city}")

    print()
    departureCityInt = int(input(f"? Enter the departure city number (1 to {len(cities)}): "))
    departureCity = cities[departureCityInt-1]
    print("You selected:", departureCity)
    print()

    print("Here is the list of destinations:")
    routes = getRoutesFromCity(departureCity)
    print()
    print("==%-2s===%-22s= DESTINATIONS ==%-14s===%-12s" % ("="*2, "="*22, "="*14, "="*12))
    print("| %-2s | %-40s | %-10s | %-10s |" % ("ID", "Destination", "Distance", "Time"))
    for i in range(len(routes)):
        route = routes[i]
        arr = 0
        if route["arrivalCity"] == departureCity:
            arr = route["departureCity"]
        else:
            arr = route["arrivalCity"]
        
        print("| %-2d | %-40s | %-10s | %-10s |" % (i+1, arr, str(route["distance"]) + " km", str(route["time"]) + " hr"))

    print("==%-2s===%-22s===============%-14s===%-10s" % ("="*2, "="*26, "="*14, "="*10))
    print()
    routeInt = int(input(f"? Enter the route ID (1 to {len(routes)}): "))
    route = routes[routeInt-1]
    

    destinationCity = ""
    if route["arrivalCity"] == departureCity:
        destinationCity = route["departureCity"]
    else:
        destinationCity = route["arrivalCity"]
    
    print("You selected route: ", f"{departureCity} to {destinationCity}")
    print()
    print("It is time to select the vehicle. Here is a list of available vehicles:")

    print("==%-2s===%-22s= CARS ==%-37s===%-7s" % ("="*2, "="*22, "="*37, "="*7))
    print("| %-2s | %-40s | %-25s | %-5s |" % ("ID", "Model", "Average fuel (L / 100km)", "Seat"))
    for i in range(len(cars)):
        car = cars[i]
        print("| %-2d | %-40s | %-25s | %-5s |" % (i+1, car["manufacturer"] + " " + car["model"], str(car["average_comb_city_highway"]), str(car["seat"])))

    print("==%-2s===%-22s=========%-37s===%-7s" % ("="*2, "="*22, "="*37, "="*7))
    print()


    carInt = int(input(f"? Select your car (1 to {len(cars)}): "))
    car = cars[carInt-1]

    print("="*47 + " YOUR CAR " + "="*47)
    print("| %-17s | %-80s |" % ("Manufacturer", car["manufacturer"]))
    print("| %-17s | %-80s |" % ("Model", car["model"]))
    print("| %-17s | %-80s |" % ("Engine", car["engine"]))
    print("| %-17s | %-80s |" % ("Power", str(car["engine"])+ " hp"))
    print("| %-17s | %-80s |" % ("Seat", car["seat"]))
    print("| %-17s | %-80s |" % ("City millage", str(round(car["city_millage"], 2)) + " L / 100km"))
    print("| %-17s | %-80s |" % ("Highway millage", str(round(car["highway_millage"], 2)) + " L / 100km"))
    print("| %-17s | %-80s |" % ("Average millage", str(round(car["average_comb_city_highway"], 2)) + " L / 100km"))
    print("| %-17s | %-80s |" % ("Fuel capacity", str(round(car["fuel_capacity"], 2)) + " L"))
    print("| %-17s | %-80s |" % ("Weight", str(car["weight"]) + " kg"))
    print("="*20 + "==========" + "="*74)
    print()

    
    begin = input("Type 'start' to begin with the simulation: ")
    if begin.lower() == 'start':
        print()

        print("=== BEGINNING WITH THE SIMULATION ===")
        print()
        return carSimulation(car, destinationCity, route["distance"], route["time"], route["trafficPoints"], route["trafficLightPoints"], route["highwayPoints"], route["cityPoints"], route["roadConditionPoints"])
    
    ## print a summary of the route


def carSimulation(car, destination, distance, duration, trafficIntervals, trafficLightIntervals, highwayIntervals, cityIntervals, roadConditionsIntervals):


    passengers = getPassengers(car["seat"])
    print("Passengers on car: " + str(passengers))
    print()

    excessive_carrage = getExcessiveCarrage()
    print("Excessive carriage on car: " + str(excessive_carrage))
    print()

    towingWeight = getTowingWeight()
    print("Towing carriage on car: " + str(towingWeight))
    print()

    ## if peak hours, apply all trafficPoints. If not, only some random (max 30%)
    departureTime = getTime()
    print("Departure time is " + str(departureTime))
    print()

    tyreConditions = ["good", "bad"]
    tyreCondition = getInputWithComparisonList("Enter the tyre condition " + str(tyreConditions) + ": ", tyreConditions, "good") ## or good or mildy
    print("Tyre condition: ", tyreCondition)
    print()

    typeOfYears = ["winter", "summer", "fall", "autumn"]
    timeOfYear = getInputWithComparisonList("Enter the season " + str(typeOfYears) + ": ", typeOfYears, "fall") ## or summer or fall 
    print("Season: ", timeOfYear)
    print()

    weatherConditions = ["snow", "rain", "fog", "sun"]
    weatherCondition = getInputWithComparisonList("Enter the weather condition " + str(weatherConditions) + ": ", weatherConditions, "sun") ## or raining, sun, fog
    print("Weather condition: ", weatherCondition)
    print()

    moods = ["angry", "relaxed", "cheerful"]
    mood = getInputWithComparisonList("Enter the driver's mood " + str(moods) + ": ", moods, "relaxed") ## or angry 
    print("Mood: ", mood)
    print()


    experience = getExperience()
    print("Experience: " + str(experience))
    print()


    serviced = getServiced()
    print("Serviced: ", serviced)
    print()

    total_weight = car["weight"] + passengers * 75 + excessive_carrage + towingWeight

    # calculate the millage from the initial conditions
    averageCityMillage = calculateInitialMillage(car, car["city_millage"], total_weight, tyreCondition, weatherCondition, timeOfYear, mood, experience, serviced)
    averageHighwayMillage = calculateInitialMillage(car, car["highway_millage"], total_weight, tyreCondition, weatherCondition, timeOfYear, mood, experience, serviced)
    averageCombinationMillage = calculateInitialMillage(car, car["average_comb_city_highway"], total_weight, tyreCondition, weatherCondition, timeOfYear, mood, experience, serviced)
    #averageMillagePer100 = calculateInitialMillage(car, car["average_millage_per_100l"], total_weight, tyreCondition, weatherCondition, timeOfYear, mood, experience, serviced)
    print()
    print()
    print("========="*2 + "INITIAL CALCULATIONS" + "=========="*2)
    print("|  %-30s | %-22s |" % ("Average city millage: ", str(round(averageCityMillage, 2)) + " Litre / 100 km"))
    print("|  %-30s | %-22s |" % ("Average highway millage: ", str(round(averageHighwayMillage, 2)) + " Litre / 100 km"))
    print("|  %-30s | %-22s |" % ("Average combined millage: ", str(round(averageCombinationMillage, 2)) + " Litre / 100 km"))
    print("========="*2 + "===================" + "=========="*2)
    print()
    print()

    distance_travelled = 0
    consumed = 0
    delta = 5

    totalRedLights = 0
    totalConsumptionForRedLights = 0

    totalYellowLights = 0
    totalConsumptionForYellowLights = 0

    totalGreenLights = 0

    totalConsumptionForRoadCondition = 0

    totalConsumptionInCity = 0
    totalConsumptionInHighway = 0
    totalConsumptionInGeneralRoad = 0

    totalDistanceInCity = 0
    totalDistanceInHighway = 0
    totalDistanceInGeneralRoad = 0
    
    factorsImpact = []

    while(distance_travelled < distance):
        distance_travelled+=delta
        print("_"*40)
        print("Distance travelled: ", distance_travelled, "km")
        print("Total consumed: ", round(consumed, 2), "Litre")
        print()
        print()

        ## TODO: if total condumed so far > fuel capactiy, get 2 random petrol pumps and add them into an arrya. at the end we will show the prices.

        isTraffic = isBetweenInterval(trafficIntervals, distance_travelled, distance)
        isTrafficLight = isBetweenInterval(trafficLightIntervals, distance_travelled, distance)
        isHighway = isBetweenInterval(highwayIntervals, distance_travelled, distance)
        isCity = isBetweenInterval(cityIntervals, distance_travelled, distance)
        isRoadCondition = isBetweenIntervalRoadConditions(roadConditionsIntervals, distance_travelled, distance)

        if (isCity or isTraffic or isTrafficLight):
            # be more precise in the cities
            if delta != 1:
                print("========== ENTERING CITY: MAKEING THE SIMULATION MORE PRECISE BY DECREASING THE DELTA ==========")
            delta = 1
        else:
            if delta != 5:
                print("========== EXITING CITY: MAKEING THE SIMULATION MORE WIDE BY INCREASING THE DELTA ==========")
            delta = 5



        if (isRoadCondition[0]):
            condition = isRoadCondition[1]
            road_condition_consumption = 0
            if (condition == "fog"):
                road_condition_consumption+=0.1
                print(condition, " consumption: ", road_condition_consumption)

            elif (condition == "mud"):
                road_condition_consumption+=0.2
                print(condition, "consumption: ", road_condition_consumption)

            elif (condition == "wet"):
                road_condition_consumption+=0.08
                print(condition, "consumption: ", road_condition_consumption)

            elif condition == "bumpy":
                road_condition_consumption+=0.16
                print(condition, "consumption: ", road_condition_consumption)

            elif condition == "construction":
                road_condition_consumption+=0.24
                print(condition, "consumption: ", road_condition_consumption)

            else:
                pass

            totalConsumptionForRoadCondition+=road_condition_consumption
            consumed+=road_condition_consumption
        ## we are in the traffic
        ## TODO: traffic between 7:9
        if isTraffic:
            local_consumption = 0
            ## +1 km for millage
            dlt = (delta + 1)
            if (isHighway):
                print("========== TRAFFIC ON HIGHWAY ==========")
                local_consumption = averageHighwayMillage/100*dlt
                totalConsumptionInHighway+=local_consumption
                totalDistanceInHighway+=dlt
            elif isCity:
                print("========== TRAFFIC IN CITY ==========")
                local_consumption = averageCityMillage/100*dlt
                totalConsumptionInCity+=local_consumption
                totalDistanceInCity+=dlt
            else:
                print("========== TRAFFIC INTERVAL ==========")
                local_consumption = averageCombinationMillage/100*dlt
                totalConsumptionInGeneralRoad+=local_consumption
                totalDistanceInGeneralRoad+=dlt
            
            consumed+=local_consumption ## add the traffic millage consumption: +2 km more
        
        ## Traffic light
        if isTrafficLight:
            print("========="*2+ "= TRAFFIC LIGHT AREA" + "========"*2)

            light = generateRandomLight()


            # TODO: simulate traffic light
            local_consumption = 0
            # average stop at traffic light: 0.1L/minute
            if (isCity):
                totalDistanceInCity+=delta
                if (light == "red"):
                    local_consumption = averageCityMillage/100*(delta) + 0.19 # consume 0.1L for each red light as waiting time is 1 minute
                    totalConsumptionForRedLights+=local_consumption
                    totalRedLights+=1
                    printTrafficLight("= Red light ", local_consumption)
                elif (light == "yellow"):
                    local_consumption = averageCityMillage/100*(delta) + 0.07 # consume 0.1L for each red light as waiting time is 1 minute
                    totalConsumptionForYellowLights+=local_consumption
                    totalYellowLights+=1
                    printTrafficLight("Yellow light ", local_consumption)
                else:
                    printTrafficLight("Green light =", 0)
                    totalGreenLights+=1
                
            else:
                if (light == "red"):
                    local_consumption = averageCombinationMillage/100*(delta) + 0.1
                    totalConsumptionForRedLights+=local_consumption
                    totalRedLights+=1
                    printTrafficLight("= Red light ", local_consumption)
                elif light == "yellow":
                    local_consumption = averageCombinationMillage/100*(delta) + 0.05
                    totalConsumptionForYellowLights+=local_consumption
                    totalYellowLights+=1
                    printTrafficLight("Yellow light ", local_consumption)
                else:
                    totalGreenLights+=1
                    printTrafficLight("Green light =", 0)

            consumed+=local_consumption
            totalConsumptionInCity+=local_consumption
            totalDistanceInCity+=delta
        
        if isHighway and not isTraffic and not isTrafficLight:
            print("========== ON HIGHWAY ==========")
            totalDistanceInHighway+=delta
            randPerc = random.randint(0, 9)

            # 30% chances of a factor affecting
            if (randPerc < 3):
                ## TODO: make tis random!
                eventImpact = factorImpact(generateRandomFactor(factors), averageHighwayMillage, delta)
                factorsImpact.append(eventImpact)
                
                consumed+=eventImpact["consumption"]
                distance+=eventImpact["distance"]

                totalConsumptionInHighway+=eventImpact["consumption"]
            else:
                consumed+=averageHighwayMillage/100*delta
                totalConsumptionInHighway+=averageHighwayMillage/100*delta
            ## TODO: ADD RANOM FACTORS: ACCTIDENT, CHANGE OF ROUTE
            

        
        if isCity and not isTraffic and not isTrafficLight:
            print("On road to city")
            totalDistanceInCity+=delta
            randPerc = random.randint(0, 9)

            # 30% chances of a factor affecting
            if (randPerc < 3):
                eventImpact = factorImpact(generateRandomFactor(factors), averageCityMillage, delta)
                factorsImpact.append(eventImpact)
                consumed+=eventImpact["consumption"]
                distance+=eventImpact["distance"]

                totalConsumptionInCity+=eventImpact["consumption"]
            else:
                consumed+=averageCityMillage/100*delta
                totalConsumptionInCity+=averageCityMillage/100*delta

        if (not isTraffic and not isTrafficLight and not isCity and not isHighway):
            ## TODO: ADD RANOM FACTORS: ACCTIDENT, CHANGE OF ROUTE
            totalDistanceInGeneralRoad+=delta
            randPerc = random.randint(0, 9)

            # 30% chances of a factor affecting
            if (randPerc < 3):
                eventImpact = factorImpact(generateRandomFactor(factors), averageCombinationMillage, delta)
                factorsImpact.append(eventImpact)
                
                consumed+=eventImpact["consumption"]
                distance+=eventImpact["distance"]

                totalConsumptionInGeneralRoad+=eventImpact["consumption"]
            else:
                consumed+=averageCombinationMillage/100*delta
                totalConsumptionInGeneralRoad+=averageCombinationMillage/100*delta


    spacing = "| %-42s | %10s %-17s |"
    print()
    print()
    print()
    print("="*32 + " SUMMARY TABLE " + "="*30)
    print("="*38 + "=============" + "="*26)
    print(spacing % ("", "", ""))
    print(spacing % ("Passengers", passengers, ""))
    print(spacing % ("Destination", destination, ""))
    print(spacing % ("Weather", weatherCondition, ""))
    print(spacing % ("", "", ""))
    print(spacing % ("Red lights", totalRedLights, ""))
    print(spacing % ("Red lights consumption", round(totalConsumptionForRedLights, 2), "Litre"))

    print(spacing % ("Yellow lights", totalYellowLights, ""))
    print(spacing % ("Yellow lights consumption", round(totalConsumptionForYellowLights, 2), "Litre"))
    print(spacing % ("Green lights", totalGreenLights, ""))


    print(spacing % ("", "", ""))
    print(spacing % ("Consumption for road conditions", round(totalConsumptionForRoadCondition, 2), "Litre"))
    print(spacing % ("", "", ""))

    print(spacing % ("Consumption in city", round(totalConsumptionInCity, 2), "Litre"))
    print(spacing % ("Consumption in highway", round(totalConsumptionInHighway, 2), "Litre"))
    print(spacing % ("Comsumption on general road", round(totalConsumptionInGeneralRoad, 2), "Litre"))
    print(spacing % ("", "", ""))

    print(spacing % ("Travel distance in city", totalDistanceInCity, "km"))
    print(spacing % ("Travel distance on highway", totalDistanceInHighway, "km"))
    print(spacing % ("Travel distance in general road", totalDistanceInGeneralRoad, "km"))
    print(spacing % ("", "", ""))


    if (totalDistanceInCity > 0):
        print(spacing % ("Final average consumption on city",  round(totalConsumptionInCity /totalDistanceInCity * 100, 2), "Litre / 100 km"))
    if (totalDistanceInHighway > 0):
        print(spacing % ("Final average consumption on highway", round(totalConsumptionInHighway /totalDistanceInHighway * 100, 2), "Litre / 100 km"))
    if totalDistanceInGeneralRoad > 0:
        print(spacing % ("Final average consumption on general road", round(totalConsumptionInGeneralRoad /totalDistanceInGeneralRoad * 100, 2), "Litre / 100 km"))

    print(spacing % ("", "", ""))
    print(spacing % ("Total overall consumption", round(consumed, 2), "Litre"))
    print(spacing % ("Overall average after consumption", round(consumed / distance * 100, 2), "Litre / 100 km"))
    print(spacing % ("Overall distance travelled",distance, "km"))
    print("="*38 + "=============" + "="*26)

    print()


    factors_compressed = joinFactors(factorsImpact)
    print("Consumption because of random factors")
    print("="*30 + " FACTORS CONSUMPTION " + "="*31)
    print("="*36 + "=====================" + "="*25)
    

    spacing = "| %-42s | %-15s | %-15s |"
    print(spacing % ("Factor", "Consumption", "Distance"))
    for factor in factors_compressed:
        print(spacing % (factor["factor"], str(round(factor["consumption"], 2)) + " Litre", str(round(factor["distance"], 2)) + " km"))
    print("="*82)



    return {
        "red_lights": totalRedLights,
        "red_light_consumption": totalConsumptionForRedLights,
        "yellow_lights": totalYellowLights,
        "yellow_lights_consumption": totalConsumptionForYellowLights,
        "road_conditions_consumption": totalConsumptionForRoadCondition,
        "city_consumption": totalConsumptionInCity,
        "highway_consumption": totalConsumptionInHighway,
        "general_road_consumption": totalConsumptionInGeneralRoad,
        "city_distance": totalDistanceInCity,
        "highway_distance": totalDistanceInHighway,
        "general_road_distance": totalDistanceInGeneralRoad,
        "total_consumption": consumed,
        "final_distance": distance,
        "factors": factorsImpact,
        "factors_compressed": joinFactors(factorsImpact),
        "car": car
    }



















## PLANE

##  ============================= GATHERING DATA =============================

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


## ============================== INPUT METHODS ==============================

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

def getAirportCode( airports, type):
    while True:
        try:
            airportSelect = input(f"? Enter the {type} airport code: ")
            isValid = checkIfValidCode(airportSelect, airports)

            if not isValid:
                raise Exception("you entered an invalid code. we could not find any airport with that code.")
            
            return airportSelect
        except Exception as err: 
            print(err)

def checkIfValidCode(code, airports):
    for airport in airports:
        if airport["code"] == code:
            return True
    return False


## ============================== LOGIC METHODS ==============================
def getDomesticAirports():
    arr = []
    valid = []
    for domesticRoute in domesticFlights:
        dep = domesticRoute["route"][0]
        for airport in airports:
            if airport["code"] == dep and dep not in valid:
                arr.append(airport)
                valid.append(dep)
        
        dep = domesticRoute["route"][1]
        for airport in airports:
            if airport["code"] == dep and dep not in valid:
                arr.append(airport)
                valid.append(dep)
    return arr

def getAirportInfo(code):
    for airport in airports:
        if code == airport["code"]:
            return airport
    return ""

def getFlightsFromAirport(flights, airport):
    validFlights = []
    for flight in flights:
        if airport in flight["route"]:
            if flight["route"][0] != airport:
                if flight["route"][0] not in validFlights:
                    validFlights.append(flight["route"][0])
            else:
                if flight["route"][1] not in validFlights:
                    validFlights.append(flight["route"][1])
    return validFlights

def findFlight(routes, departure, arrival):
    validRoutes = []
    for route in routes:
        if departure in route["route"] and arrival in route["route"]:
            validRoutes.append(route)
    return validRoutes

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


## ============================== PRINT METHODS ==============================

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




def printFlightRouteSmall(route):
    dep = route["route"][0]
    arr = route["route"][1]
    airportInfoDeparture = getAirportInfo(dep)
    airportInfoArrival = getAirportInfo(arr)


    print()
    print("Departure code: ", dep)
    print("Departure airport: ", airportInfoDeparture["name"], "(" + airportInfoDeparture["country"] + ")")
    print("Arrival code: ", arr)
    print("Arrival airport: ", airportInfoArrival["name"], "(" + airportInfoArrival["country"] + ")")

def printFlightRoute(route, i):
    airportInfoDeparture = getAirportInfo(route["route"][0])
    airportInfoArrival = getAirportInfo(route["route"][1])
    planes = getFlights()
    plane = planes[route["plane"]]

    print("="*33 + "AIRCRAFT PROVIDER #" + str(i) + "="*34)
    print("| %-20s | %-60s |" % ("Company", route["company"]))
    print("| %-20s | %-60s |" % ("Plane", plane["name"]))
    print("| %-20s | %-60s |" % ("Airport 1", airportInfoDeparture["name"]))
    print("| %-20s | %-60s |" % ("Airport 2", airportInfoArrival["name"]))
    print("| %-20s | %-60s |" % ("Distance", str(route["distance"])+" km"))
    print("| %-20s | %-60s |" % ("Duration", str(route["duration"])+" hours"))
    print("| %-20s | %-60s |" % ("Flight type", route["flight_type"]))
    print("="*87)
    print()

def printFlightRoutes(routes):
    for i in range(len(routes)):
        route = routes[i]
        printFlightRoute(route, i+1)

def printAirport(airport):
    print("="*35 + "AIRPORT" + "="*35)
    print("| %-20s | %-50s |" % ("Code", airport["code"]))
    print("| %-20s | %-50s |" % ("Name", airport["name"]))
    print("| %-20s | %-50s |" % ("city", airport["city"]))
    print("| %-20s | %-50s |" % ("Country", airport["country"]))
    print("="*77)
    print()

def printAirportWithCode(code):
    airport = getAirportInfo(code)
    printAirport(airport)

## ============================== MAIN ==============================

def flightPrompts():
    while True:
        try:

            flightType = input("? Enter 'international' for international flights or 'domestic': ")
            if ((flightType).lower() != "international" and (flightType).lower() != "domestic"):
                raise Exception("Invalid choice: 'international' or 'domestic' possible only.")
            print("Flight type: ", flightType)

            #TODO: show planes
            ## show flight options
            
            routes = 0
            local_airports = {}
            if (flightType == "international"):
                '''
                for route in internationalFlights:
                    printFlightRouteSmall(route)
                '''
                    
                routes = internationalFlights
                local_airports = airports
            else:
                '''
                for route in domesticFlights:
                    printFlightRouteSmall(route)
                '''
                routes = domesticFlights
                local_airports = getDomesticAirports()

            print()
            
            # showind the list of airports to depart from
            for airport in local_airports:
                
                printAirport(airport)
            ## Get the departure airport code
            departureAirport = getAirportCode(local_airports, "departure")

            # showind the list of flights departing from the departure airport
            print()
            print("Here is the list of flights from that airport: ")
            arrivalAirports = (getFlightsFromAirport(routes, departureAirport))
            for arrivalCode in arrivalAirports:
                printAirportWithCode(arrivalCode)


            ## getting the arrival airport input
            arrivalAirport = getAirportCode(airports, "arrival")
            ## checking if the arrival airport exists

            '''
            departureAirport = input("? Enter the departure airport code: ")
            arrivalAirport = input("? Enter the arrival airport code: ")
            '''

            ## checking if a valid route can be enstablished. Meaning that the user has inputted correctly.
            validFlights = findFlight(routes, departureAirport, arrivalAirport)
            if (len(validFlights) == 0):
                raise Exception("No flight found. try again.")

            ## Selecting the airline
            selection = 0
            print()
            print("HERE ARE THE FLIGHTS THAT WE FOUND")
            printFlightRoutes(validFlights)
            if (len(validFlights) == 1):
                pass
                    ## continue loop
            else:
                selection = int(input("? Multiple airlines found. Select one (between 1 and " + str(len(validFlights)) + "): "))
                if (selection > len(validFlights) or selection < 1):
                    raise Exception("Invalid value.")
            
            route = validFlights[selection-1]
            if not route:
                print("An error occured. Could not enstablish a route")

            ## returning the route for simulation
            return route
        except Exception as err:
            print(err)
            print("Restarting the app...")
            
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













typeOfUsage = input("? Enter 'car' for car gas millage simulation or 'plane' for flight simulation: ")
if typeOfUsage != "car" and typeOfUsage != "plane":
    print("Invalid choice: 'car' or 'plane' only.")
print()

if typeOfUsage == "plane":
    route = flightPrompts()
    print("\n\n")
    begin = input("Type 'start' to begin with the simulation: ")
    if begin.lower() == 'start':
        print("BEGINNING FLIGHT SIMULATION")
        print()

        flight = getFlights()[route["plane"]]
        printFlight(flight)
        print()
        
        flightSimulation(route["plane"], route["distance"], route["duration"])
elif typeOfUsage == "car":
    results = carPrompts()
    if results:
        print()
        fill = input("Would you like to compute the price of the fuel (yes or no)?: ")
        if (fill == "yes"):
            if (results["car"]["premium"]):
                print("Your car requires premium fuel.")
            prices = findGasStations(4, results["car"]["premium"])
            printGasStations(prices[0], prices[1]["name"])

            selectionId = int(input(f"Enter the selection ID (1 to {(4)}): "))
            station = prices[0][selectionId-1]

            print()
            print("You selected:", station["name"])
            if results["car"]["premium"]:
                print("You selected:", station["name"])
                print("Gas price:", station["premium_cost"], "CA$ / L")
                print("Your total cost is: ", round(station["premium_cost"] * results["total_consumption"], 2), "CA$")
            else:
                print("Gas price:", station["petrol_cost"], "CA$ / L")
                print("Your total cost is: ", round(station["petrol_cost"] * results["total_consumption"], 2), "CA$")










