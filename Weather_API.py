
def weather_api_pannel(city) :
    
    print("Welcom to Weather API app !")
    try :
        choice = int(input("What action you wanna do ? \n1.Get_city_weather \n2.Favorit_list \n3.Exit_app . ( valid: number of acts )"))
    except :
        print("not valid . try again :")
        choice = int(input("What action you wanna do ? \n1.Get_city_weather \n2.Favorit_list \n3.Exit_app . ( valid: number of acts )"))
    
    if choice == 1 :
        def get_weather():
            print(f"{city} city information : ")
            pass

    elif choice == 2 :
        def favorit_list() :
            
            favorits_list = []
            try :
                func_choice = int(input("What action you wanna do in your favorit list ? \n1.add_city \n2.delete_city \n3.edit_options \n4.favorit_list \n5.find_city ( valid : number of acts)"))
            except :
                print("not valid . try again .")
                func_choice = int(input("What action you wanna do in your favorit list ? \n1.add_city \n2.delete_city \n3.edit_options \n4.favorit_list \n5.find_city"))
                
            if func_choice == 1 :
                def add_city() :
                    ac_choice = input("Enter the name of city you want to add to favorite list : ")
                    favorits_list.append(ac_choice)
                
            elif func_choice == 2 :
                def delete_city() :
                    dc_choice = input("Enter the name of city you want to delete from favorite list : ")
                    if dc_choice in favorits_list :
                        favorits_list.remove(dc_choice)
                    else :
                        print("this city isnt in your favorite list ! ")
                
            elif func_choice == 3 :
                def edit_city() :
                    fc_choice = input("Enter the name of city you want to edit from favorite list : ")
                    if fc_choice in favorits_list :
                        fc_edit = input("whats the new name of this city ? : ")
                        favorits_list.remove(fc_choice)
                        favorits_list.append(fc_edit)
                    else : 
                        print("this city isnt in your favorite list ! ")
                    pass
                
            elif func_choice == 4 :
                def favorit_list() :
                    pass
                
            elif func_choice == 5 :
                def find_city() :
                    pass
                

    elif choice == 3 :
        def main_loop():
            command = input("enter city name: ").split()

            if not command:
                print("you havent entered one of these below:\n1_the command\n2_the city")
                # main_loop()

            action = command[0].lower()

            if action == "qt" or action == "quit":
                return("Thanks for using our app ")
            
            if action == "gw" or action == "get-weather" and len(command) >= 2:
                city = " ".join(command[1:])
                # get_weather(.city)

            else:
                print("your command is wrong")
                # main_loop()\

    elif choice == 4 :
        return("Thanks for using our app ")
                

# main_loop()