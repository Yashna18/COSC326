# The following program takes in user input coordinates and returns
# a formatted version that is then outputted to the GeoJSON.json
# file in this folder.
# @author - Yashna Shetty

import re
import sys

# helper functions

# @param - user input
# @return - just the numbers within the coordinates


def num_only_coord(user_coords):
    coord_num = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", user_coords)
    return coord_num

# @param - user input
# @param - number of digits only within the user input
# @return = a full list of the entire user input


def whole_line_coord(user_coords, length_num):
    if length_num == 2:
        list_coord = re.findall(
            r"[-+]?(?:\d*\.\d+|\d+|[A-Za-z]+)", user_coords)
    elif length_num == 4:
        list_coord = list_coord = re.findall(
            r"[-+]?(?:\d*\.\d+|\d+)|[^ \n](?:[A-Za-z]+|[\'°]?)", user_coords)
    elif length_num == 6:
        list_coord = list_coord = re.findall(
            r"[-+]?(?:\d*\.\d+|\d+)|[^ \n](?:[A-Za-z]+|[\"\'°]?)", user_coords)

    return list_coord

# @param - a full list of the user input
# @param - a list of latitudes
# @param - a list of longitudes
# @return - the position of the specified latitude or longitude in the full list


def verify_lat_long(list_coord, lat_dir, long_dir):
    pos_lat_long = [None, None]
    countx = 0
    county = 0
    for x1 in lat_dir:
        for y1 in list_coord:
            if x1 == y1:
                pos_lat_long[0] = list_coord.index(y1)
                countx += 1
                if countx > 1:
                    print(
                        "Unable to process: There can only be one latitude per coordinate line")
                    return False
    for x2 in long_dir:
        for y2 in list_coord:
            if x2 == y2:
                pos_lat_long[1] = list_coord.index(y2)
                county += 1
                if county > 1:
                    print(
                        "Unable to process: There can only be one longitude per coordinate line")
                    return False
    return pos_lat_long

# returns the label should there be one
# otherwise returns an empty string


def find_label(line_coord, lat_direction, long_direction, just_num_coord):
    if line_coord[-1] not in lat_direction and line_coord[-1] not in long_direction and line_coord[-1] not in just_num_coord and line_coord[-1] != "°" and line_coord[-1] != "'":
        return line_coord[-1]
    else:
        return ""

# verifies that the latitude numbers and longitude numbers are not
# unreasonable


def verify_lat_long_nums(lat_long_index, line_coord, latNum, longNum):
    positive_lat_long = ["N", "north", "North",
                         "NORTH" "E", "east", "East", "EAST"]
    negative_lat_long = ["S", "south", "South",
                         "SOUTH", "W", "west", "West", "WEST"]

    if lat_long_index[0] != None:
        if line_coord[lat_long_index[0]] in positive_lat_long:
            if latNum < 0:
                print(
                    "Unable to process: A positive latitude cannot proceed a negative latitude number: ", latNum)
                return False
        if line_coord[lat_long_index[0]] in negative_lat_long:
            if latNum > 0:
                latNum *= -1
    if lat_long_index[1] != None:
        if line_coord[lat_long_index[1]] in positive_lat_long:
            if longNum < 0:
                print(
                    "Unable to process: A positive longitude cannot proceed a negative longitude number: ", longNum)
                return False
        if line_coord[lat_long_index[1]] in negative_lat_long:
            if longNum > 0:
                longNum *= -1

    return [latNum, longNum]

# finds the index of the units should the user have
# specified the units of the coordinates


def check_unit_index(list_coord, just_num_coord):
    min_unit_decl = ["m", "minutes", "'"]
    degree_unit_decl = ["degree", "degrees", "°"]
    seconds_unit_decl = ["seconds", "s", "\""]

    if len(just_num_coord) == 4:
        unit_list = [None, None, None, None]
    elif len(just_num_coord) == 6:
        unit_list = [None, None, None, None, None, None]
    countx = 0
    county = 0
    countz = 0
    for x1 in min_unit_decl:
        for i, x2 in enumerate(list_coord):
            if x1 == x2:
                countx += 1
                if countx == 1:
                    unit_list[0] = i
                elif countx == 2:
                    unit_list[1] = i
            if countx == 0:
                unit_list[0] = None
                unit_list[1] = None
    if countx == 4:
        unit_list = [None, None, None, None]
    elif countx == 6:
        unit_list = [None, None, None, None, None, None]

    for y1 in degree_unit_decl:
        for j, y2 in enumerate(list_coord):
            if y1 == y2:
                county += 1
                if county > 2:
                    print("Unable to process: degrees can only be specified twice")
                    return False
                elif county == 1:
                    unit_list[2] = j
                elif county == 2:
                    unit_list[3] = j
            if county == 0:
                unit_list[2] = None
                unit_list[3] = None

    if len(just_num_coord) == 6:
        for z1 in seconds_unit_decl:
            for k, z2 in enumerate(list_coord):
                if z1 == z2:
                    countz += 1
                    if countz > 2:
                        print(
                            "Unable to process: minutes can only be specified twice")
                        return False
                    elif countz == 1:
                        unit_list[4] = i
                    elif countz == 2:
                        unit_list[5] = i
                if countz == 0:
                    unit_list[4] = None
                    unit_list[5] = None
    if countx == 3 or countx == 5:
        print("Unable to process: Bad direction")
        return False
    return unit_list

# returns the latitude and longitude in the
# correct order needed for the .json file


def lat_long_nums(just_num_coord, pos_lat_long, line_coord):
    i = 0
    for x in just_num_coord:
        just_num_coord[i] = float(x)
        i += 1
    if pos_lat_long[0] != None:
        if line_coord[-2] == line_coord[pos_lat_long[0]] or line_coord[-1] == line_coord[pos_lat_long[0]]:
            latNum = just_num_coord[1]
            longNum = just_num_coord[0]
        else:
            latNum = just_num_coord[0]
            longNum = just_num_coord[1]
    if pos_lat_long[1] != None:
        if line_coord[-2] == line_coord[pos_lat_long[1]] or line_coord[-1] == line_coord[pos_lat_long[1]]:
            latNum = just_num_coord[0]
            longNum = just_num_coord[1]
        else:
            latNum = just_num_coord[1]
            longNum = just_num_coord[0]
    else:
        latNum = just_num_coord[0]
        longNum = just_num_coord[1]

    if latNum < -90 or latNum > 90:
        print("Unable to process: Latitude number should be between -90 and 90.\nYou've entered: ", latNum)
        return False
    if longNum < -180 or longNum > 180:
        print("Unable to process: Longitude number should be between -180 and 180.\nYou've entered: ", longNum)
        return False
    return [latNum, longNum]

# cases for provided specs

# if there are 2 nums


def decimalDegrees(just_num_coord, line_coord, lat_direction, long_direction, pos_lat_long):
    label = find_label(line_coord, lat_direction,
                       long_direction, just_num_coord)
    if lat_long_nums(just_num_coord, pos_lat_long, line_coord) != False:
        latNum = lat_long_nums(just_num_coord, pos_lat_long, line_coord)[0]
        longNum = lat_long_nums(just_num_coord, pos_lat_long, line_coord)[1]
    else:
        return False
    if verify_lat_long_nums(pos_lat_long, line_coord, latNum, longNum) != False:
        latNum = verify_lat_long_nums(
            pos_lat_long, line_coord, latNum, longNum)[0]
        longNum = verify_lat_long_nums(
            pos_lat_long, line_coord, latNum, longNum)[1]
    else:
        return False

    return [latNum, longNum, label]

# if there are 4 nums


def degreeMin(just_num_coord, line_coord, lat_direction, long_direction, pos_lat_long):
    label = find_label(line_coord, lat_direction,
                       long_direction, just_num_coord)

    unit_index = check_unit_index(line_coord, just_num_coord)
    count_none = 0
    for x in unit_index:
        if x == None:
            count_none += 1

    if count_none == 4:
        degree_num1 = just_num_coord[0]
        min_num1 = just_num_coord[1]
        degree_num2 = just_num_coord[2]
        min_num2 = just_num_coord[3]

    else:
        i = 0
        j = 0
        for ind in unit_index:
            for num in just_num_coord:
                if ind != None:
                    this_num = line_coord[unit_index[i]-1]
                    if this_num == num:
                        num_ind = j + 1
                        if i == 0 or i == 1:
                            if num_ind % 2 == 1:
                                degree_num1 = just_num_coord[1]
                                min_num1 = just_num_coord[0]
                                degree_num2 = just_num_coord[3]
                                min_num2 = just_num_coord[2]
                            elif num_ind % 2 == 0:
                                degree_num1 = just_num_coord[0]
                                min_num1 = just_num_coord[1]
                                degree_num2 = just_num_coord[2]
                                min_num2 = just_num_coord[3]
                        elif i == 2 or i == 3:
                            if num_ind % 2 == 1:
                                degree_num1 = just_num_coord[0]
                                min_num1 = just_num_coord[1]
                                degree_num2 = just_num_coord[2]
                                min_num2 = just_num_coord[3]
                            elif num_ind % 2 == 0:
                                degree_num1 = just_num_coord[1]
                                min_num1 = just_num_coord[0]
                                degree_num2 = just_num_coord[3]
                                min_num2 = just_num_coord[2]
                    else:
                        j += 1

            i += 1
    leftdd = float(degree_num1) + (float(min_num1)*(1/60))
    rightdd = float(degree_num2) + (float(min_num2)*(1/60))

    new_num_only_coord = [leftdd, rightdd]
    if lat_long_nums(new_num_only_coord, pos_lat_long, line_coord) != False:
        latNum = lat_long_nums(new_num_only_coord, pos_lat_long, line_coord)[0]
        longNum = lat_long_nums(
            new_num_only_coord, pos_lat_long, line_coord)[1]
    else:
        return False

    if verify_lat_long_nums(pos_lat_long, line_coord, latNum, longNum) != False:
        latNum = verify_lat_long_nums(
            pos_lat_long, line_coord, latNum, longNum)[0]
        longNum = verify_lat_long_nums(
            pos_lat_long, line_coord, latNum, longNum)[1]
    else:
        return False

    return [latNum, longNum, label]

# if there are 6 nums


def degreeMinSec(just_num_coord, line_coord, lat_direction, long_direction, pos_lat_long):
    label = find_label(line_coord, lat_direction,
                       long_direction, just_num_coord)

    degree_num1 = just_num_coord[0]
    min_num1 = just_num_coord[1]
    sec_num1 = just_num_coord[2]
    degree_num2 = just_num_coord[3]
    min_num2 = just_num_coord[4]
    sec_num2 = just_num_coord[5]

    leftdd = float(degree_num1) + (float(min_num1)
                                   * (1/60)) + (float(sec_num1)*(1/3600))
    rightdd = float(degree_num2) + (float(min_num2)
                                    * (1/60)) + (float(sec_num2)*(1/3600))

    new_num_only_coord = [leftdd, rightdd]
    if lat_long_nums(new_num_only_coord, pos_lat_long, line_coord) != False:
        latNum = lat_long_nums(new_num_only_coord, pos_lat_long, line_coord)[0]
        longNum = lat_long_nums(
            new_num_only_coord, pos_lat_long, line_coord)[1]
    else:
        return False

    if verify_lat_long_nums(pos_lat_long, line_coord, latNum, longNum) != False:
        latNum = verify_lat_long_nums(
            pos_lat_long, line_coord, latNum, longNum)[0]
        longNum = verify_lat_long_nums(
            pos_lat_long, line_coord, latNum, longNum)[1]
    else:
        return False

    return [latNum, longNum, label]

# function called at the end of the for loop in main
# to open and write to the .json file


def writeJson(coords):
    start = "{\n\"type\": \"FeatureCollection\",\n\"features\": [\n"
    end = "\n]\n}"
    file = open("GeoJSON.json", "w")
    file.write(start + coords[0:len(coords)-1] + end)


def __main():
    lat_direction = ["north", "North", "NORTH",
                     "N", "south", "South", "SOUTH", "S"]
    long_direction = ["east", "EAST", "East",
                      "E", "west", "WEST", "West", "W"]
    decimalDegrees_coords = ""
    degreeMin_coords = ""
    degreeMinSec_coords = ""
    coords = ""
    print("\nHello User!")
    print("If you are manually entering coordinates please type \"done\" once you are finished entering all your coordinates.")
    print("Otherwise, type \"quit\" to quit the program without changes to your .json file\n")
    for line in sys.stdin:
        user_coords = line.rstrip()
        if user_coords == "quit":
            quit()
        if user_coords == "done":
            break
        just_num_coord = num_only_coord(user_coords)
        if len(just_num_coord) != 2 and len(just_num_coord) != 4 and len(just_num_coord) != 6:
            print("Unable to process: ", line)
            continue
        line_coord = whole_line_coord(user_coords, len(just_num_coord))
        pos_lat_long = verify_lat_long(
            line_coord, lat_direction, long_direction)
        if pos_lat_long != False:
            if len(just_num_coord) == 2:
                decimalDegrees_coords = decimalDegrees(just_num_coord, line_coord,
                                                       lat_direction, long_direction, pos_lat_long)
                if decimalDegrees_coords != False:
                    latNum = decimalDegrees_coords[0]
                    longNum = decimalDegrees_coords[1]
                    label = decimalDegrees_coords[2]
            if len(just_num_coord) == 4:
                degreeMin_coords = degreeMin(just_num_coord, line_coord,
                                             lat_direction, long_direction, pos_lat_long)
                if degreeMin_coords != False:
                    latNum = degreeMin_coords[0]
                    longNum = degreeMin_coords[1]
                    label = degreeMin_coords[2]
            if len(just_num_coord) == 6:
                degreeMinSec_coords = degreeMinSec(just_num_coord, line_coord,
                                                   lat_direction, long_direction, pos_lat_long)
                if degreeMinSec_coords != False:
                    latNum = degreeMinSec_coords[0]
                    longNum = degreeMinSec_coords[1]
                    label = degreeMinSec_coords[2]
            if decimalDegrees_coords != False and degreeMin_coords != False and degreeMinSec_coords != False:
                latNum = round(latNum, 6)
                longNum = round(longNum, 6)
                coords = coords + ("{\n\"type\": \"Feature\",\n\"properties\": {\n\"name\": \"" + label +
                                   "\"\n},\n\"geometry\": {\n\"type\": \"Point\",\n\"coordinates\": [" + str(longNum) + ", " + str(latNum) + "]\n}\n},")
    writeJson(coords)


__main()
