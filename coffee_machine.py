options = {"E" : "espresso" ,"L" : "latte","C" : "cappuccino"}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,

    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }

}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

choice = input("What would you like? (E - Esspresso/ L - Latte/ C - Cappuccino)").upper()


status = "OFF"
while choice!=status:
    if choice== "REPORT":
        print("Water" ,':', resources["water"],"ml")
        print("milk" ,':', resources["milk"],"ml")
        print("coffee" ,':', resources["coffee"],"grams")
    elif choice not in ["E","C","L"]:
        print("Sorry Option Not Avliable")
    else:
        if resources["water"] >=MENU[options[choice]]["ingredients"]["water"] and resources["coffee"]>=MENU[options[choice]]["ingredients"]["coffee"] and resources["milk"]>= MENU[options[choice]]["ingredients"]["milk"]:

            print(f"That would be {MENU[options[choice]]["cost"]}$")
            p=int(input("How many pennys? "))
            n=int(input("How many Nickels? "))
            d=int(input("How many Dimes? "))
            q=int(input("How many Quarter? "))

            price = p*0.01 + n*0.05 + d*0.1 + q*0.25
            if price< MENU[options[choice]]["cost"]:
                print ("Not enough money is paid")
            else:
                resources["water"]-= MENU[options[choice]]["ingredients"]["water"]
                resources["coffee"]-= MENU[options[choice]]["ingredients"]["coffee"]
                resources["milk"]-= MENU[options[choice]]["ingredients"]["milk"]

                if price > MENU[options[choice]]["cost"]:
                    print("Here's your",price - MENU[options[choice]]["cost"] , "$ change")
                print (f"Enjoy Your {options[choice]} !!!")

        else:
            print("Not Enough Resources")

        
            
    choice = input("What would you like? (E - Esspresso/ L - Latte/ C - Cappuccino)").upper()