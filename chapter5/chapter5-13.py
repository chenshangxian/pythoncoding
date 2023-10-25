# File: <Falling Distance>
# Description: <It can return the distance, in meters, that the object has fallen during that time interval.>
# Assignment Name and Number:13. Falling Distance
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
def falling_distance(time_seconds):
    g = 9.8 
    distance = 0.5 * g * time_seconds**2
    return distance

def main():
    for t in range(1, 11):
        distance= falling_distance(t)
        print("At",t,"seconds,""the object has fallen",distance,"meters.")
main()






