message = input("tell me something: ")
print(message)


name = input("please inout ur name: ")
print(f"\nHello, {name}!")

name = input("\nWhat is your name? ")
response = input("which mountain would you like to climb someday? ")

responses[name] = response

repeat = input("would you like to let other person respond?(y/n)")
if repeat == "no" :
    polling_active = False

    print("\n--poll results--")
    for name, response in response.item():
        print(f"{name} would like tp climb{response}.")
        
    please