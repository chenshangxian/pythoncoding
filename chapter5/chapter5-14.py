def kinetic_energy(mass, velocity):
    KE = 0.5 * mass * velocity**2
    return KE
def main():
    mass = float(input("Please enter the object's mass in kilograms: "))
    velocity = float(input("Please enter the object's velocity in meters per second: "))
    KE = kinetic_energy(mass, velocity)
    print(f"The object's kinetic energy is: {KE:.2f} Joules.")
main()
