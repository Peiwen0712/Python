print("Hello Wolrd")

alien_0 = { "colour" : "green", "points" : "5"}
print(alien_0)
del alien_0["points"]
print(alien_0)

favorite_language = {
    "jane" : "a" ,
    "Jack" : "b" ,
    "june" : "a" ,

}
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite langiage is {language.title()}")

for name in favorite_language.keys():
    print(name)

for language in favorite_language.values():
    print(language.title())

for language in set(favorite_language.values()):
    print(language)

for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking this pool")

apple_0 = {"colour" : "red", "point" : "5"}
apple_1 = {"colour" : "yellow", "point" : "10"}
apple_2 = {"colour" : "blue", "point" : "15"}

all_apples = [apple_0, apple_1, apple_2]
for a in all_apples:
    print(a)

    pizza = {
        "crust" : "thick",
        "toppings" : ['a', 'b', 'c'],
    }
    print(f"you ordered a {pizza['crust'].title()}-crust pizza"
        "with the flowing toppings:")

    for toppings in pizza['toppings']:
        print(f"\t{toppings.title()}")

#
#    users = {
#        "peiwenchi" :{
#            "first" : "peiwen"
#            "last" : "chi"
#            "loscation" : "bath"
#        }
#    }
#    for username, user_info in users.items():
#        print(f"\n") 