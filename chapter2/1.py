def display_information(name, address, city, state, zip_code, telephone, major):
    print("Personal information：")
    print("--------------------")
    print(f"Name: {name}")
    print(f"address: {address}")
    print(f"city: {city}")
    print(f"state: {state}")
    print(f"zip_code: {zip_code}")
    print(f"telephonr: {telephone}")
    print(f"major: {major}")

def main():
    name = input("name: ")
    address = input("address: ")
    city = input("city: ")
    state = input("state: ")
    zip_code = input("zip_code: ")
    telephone = input("telephone: ")
    major = input("major: ")
    
    display_information(name, address, city, state, zip_code, telephone, major)

main()