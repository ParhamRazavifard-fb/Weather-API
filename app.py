def get_weather(city):
    print(f"you want the weather of {city} city")

def main_loop():
    command = input("enter city name: ").split()

    if not command:
        print("you havent entered one of these below:\n1_the command\n2_the city")
        main_loop()

    a = command[0]

    if a == "qt":
        print("thanks for using our app")
        return
    
    if a == "gw" and len(command) >= 2:
        city = " ".join(command[1:])
        get_weather(city)

    else:
        print("your command is wrong")
        main_loop()

main_loop()