def get_hill_rating(drop, distance, hill_type):
    # Create a dictionary
    steepness_dict = {
        "Downhill" : 1.2,
        "Slalom" : 0.9,
        "Giant Slalom" : 1.0
    }
    # Calculate the dificulty value
    dificulty = drop / distance * steepness_dict[hill_type]
    # return following instructions
    if dificulty <= 0.1:
        return "Green"
    elif 0.1 < dificulty <= 0.25:
        return "Blue"
    else:
        return "Black"

if __name__ == '__main__':
    print(get_hill_rating(95, 900, "Slalom"))
    print(get_hill_rating(620, 2800, "Downhill"))
    print(get_hill_rating(420, 1680, "Giant Slalom"))
    print(get_hill_rating(250, 3000, "Downhill"))
    print(get_hill_rating(110, 900, "Slalom"))
    print(get_hill_rating(380, 1500, "Giant Slalom"))