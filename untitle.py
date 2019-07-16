blood_types_str = "A B A O AB AB O A B O B AB"
blood_types = blood_types_str.split()
print(blood_types)

dict = {}
for blood in blood_types:
    if blood in dict.keys():
        dict[blood] += 1
    else:
        dict[blood] = 1
print(dict)