HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8
num_people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))
total_hot_dogs_needed = num_people * hot_dogs_per_person
hot_dog_packages_needed = (total_hot_dogs_needed + HOT_DOGS_PER_PACKAGE - 1) // HOT_DOGS_PER_PACKAGE
buns_packages_needed = (total_hot_dogs_needed + BUNS_PER_PACKAGE - 1) // BUNS_PER_PACKAGE
hot_dogs_leftover = (hot_dog_packages_needed * HOT_DOGS_PER_PACKAGE) - total_hot_dogs_needed
buns_leftover = (buns_packages_needed * BUNS_PER_PACKAGE) - total_hot_dogs_needed
print("Minimum number of packages of hot dogs required:", hot_dog_packages_needed)
print("Minimum number of packages of hot dog buns required:", buns_packages_needed)
print("Number of hot dogs left over:", hot_dogs_leftover)
print("Number of hot dog buns left over:", buns_leftover)