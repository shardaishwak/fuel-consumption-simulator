import random

## ===================== MODEL ======================

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

cars = []

factors = ["protest", "accident_on_road", "construction", "muddy_road"]


cars.append(defineCar("audi_rsq8", "Audi", "RSQ8 2022", "Twin-turbocharged and intercooled DOHC 32-valve V-8", 591,"8-speed automatic",5,True,11.9,17.5,15,6.7,85,2490))
cars.append(defineCar("porsche_panamera_4s", "Porsche", "Panamera 4S", "6-cylinder", 473, "8-speed dual clutch automatic", 5, True, 12.8, 9.8, 11.4, 5, 80, 2100))
cars.append(defineCar("honda_civic", "Honda", "Civic 2022 Hatchback", "4 cylinder", 129, "5-speed automatic", 5, False, 7.7, 6.3, 7.1, 3, 46, 1256))
cars.append(defineCar("lamborgini_evo", "Lamborghini", "Huracán EVO Coupè", "DOHC 40-valve V-10", 631, "7-speed dual-clutch automatic", 2, True, 18, 12.9, 15.7, 6.7, 83, 1.339))
cars.append(defineCar("volkswagen_golf", "Volkswagen", "Golf 2021", "4-cylinder", 147, "6-speed manual", 5, False, 8.2, 6.5, 7.5, 3, 50, 1425))





# trafficPoints: percentage of destination, such as a range [[10, 13]] meaning that there can be a trafficPoint between that element. Every city has its own so it will 
# be easy to customize for each city and make the code easier to adjust

# trafficLightPoints: percentage of destination, such as a range [[80, 100, 35]]. The first two elements are the percentage range where the traffic simulation should activate
# the last number is the number of traffic lights



## ===================== INPUTS =====================



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


## ===================== MAIN =======================

# highway points: range between which the user is driving on highway
## everything outside highInterval and cityInterval will be considered as a normal driviing condition, with current average
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
                    local_consumption = averageCombinationMillage/100*(delta) + 0.1
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


## trafficPoints, trafficlights, highway, city, [[a, b, "flatstreet"]]: roadConditions
#(simulate(cars[0], "rome", 100, 2.5, [[10, 20]], [[30, 80]], [[40, 50]], [[0, 0]], [[0, 0, "mud"]]))
