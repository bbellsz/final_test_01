#central,northern,northeastern,eastern,western,southern
def validate_express(weight,zone):
    if type(weight) == str:
        if zone == "central" or zone == "eastern" or zone == "western" or zone == "northern" or zone == "northeastern" or zone == "southern":
            return "Please input weight with float or integer."
        else:
            return "Please input weight as a float or integer, and zone is entered incorrectly."
    elif type(zone) != str:
        if weight < 0:
            return "Impossible, the weight's out of range and Please input zone with string."
        else:
            return "Please input zone with string."
    elif (type(weight) == float or type(weight) == int) and type(zone) == str:
        if weight >= 0 and (zone == "central" or zone == "eastern" or zone == "western" or zone == "northern" or zone == "northeastern" or zone == "southern"):
            return weight,zone
        elif weight >= 0 and (zone != "central" and zone != "eastern" and zone != "western" and zone != "northern" and zone != "northeastern" and zone != "southern"):
                return "Zone is entered incorrectly." 
        else:
            if weight < 0 and (zone != "central" and zone != "eastern" and zone != "western" and zone != "northern" and zone != "northeastern" and zone != "southern"):
                return "Impossible, the weight's out of range and zone is entered incorrectly."
            elif weight < 0:
                return "Impossible, the weight's out of range."
            
def calculate_express(weight,zone):
    result = validate_express(weight,zone)
    if (type(weight) == float or type(weight) == int) and type(zone) == str:
        if weight >= 0 and (zone == "central" or zone == "eastern" or zone == "western" or zone == "northern" or zone == "northeastern" or zone == "southern"):
            if weight > 20:
                price = 500
            elif weight >= 10:
                if zone == "central" or zone == "eastern" or zone == "western":
                    price = 420
                else: price = 460
            elif weight > 0: 
                if zone == "central" or zone == "eastern" or zone == "western":
                    price = 200
                else: price = 240
            elif weight == 0:
                price = 0
            return price
        else: return result
    else: return result


