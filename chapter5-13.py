def falling_distance(time_seconds):
    g = 9.8 
    distance = 0.5 * g * time_seconds**2
    return distance

def main():
    for t in range(1, 11):
        distance= falling_distance(t)
        print("At",t,"seconds,""the object has fallen",distance,"meters.")
main()






