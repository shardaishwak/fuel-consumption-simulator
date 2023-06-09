import random

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