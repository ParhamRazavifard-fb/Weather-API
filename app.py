def get_weather(city):
    print(f"you want the weather of {city} city")

def main_loop():
    command = input("enter city name: ").split()

    if not command:
        print("you havent entered one of these below:\n1_the command\n2_the city")
        main_loop()

    city_name = command[0]
    choice = command[1]

    if choice.lower() == "qt" or a.lower() == "quit":
        print("thanks for using our app")
        return
    
    if choice.lower() == "gw" and len(command) >= 2:
        city = " ".join(command[1:])
        get_weather(city)

    else:
        print("your command is wrong")
        main_loop()

main_loop()