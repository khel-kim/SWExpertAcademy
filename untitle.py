import collections
blood_types_str = "A B A O AB AB O A B O B AB"
blood_types = blood_types_str.split()
print(collections.Counter(blood_types))
