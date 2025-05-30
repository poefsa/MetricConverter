#Simple Converter For Metric Systems

from colorama import init, Fore
init(Fore)

print(Fore.LIGHTBLACK_EX + "  __  __      _        _         _____                          _            ")
print(Fore.LIGHTBLACK_EX + " |  \/  |    | |      (_)       / ____|                        | |           ")
print(Fore.LIGHTBLACK_EX + " | \  / | ___| |_ _ __ _  ___  | |     ___  _ ____   _____ _ __| |_ ___ _ __ ")
print(Fore.LIGHTBLACK_EX + " | |\/| |/ _ \ __| '__| |/ __| | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|")
print(Fore.LIGHTBLACK_EX + " | |  | |  __/ |_| |  | | (__  | |___| (_) | | | \ V /  __/ |  | ||  __/ |   ")
print(Fore.LIGHTBLACK_EX + " |_|  |_|\___|\__|_|  |_|\___|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   ")


print("")

print("[1] Ft -> In")
print("[2] In -> Cm")

userOption = int(input("Please Enter An Option: "))

if userOption == 1:
    userFt = int(input("Please Enter Feet: "))
    print(f"From Feet to Inches, your value is: {userFt * 12}")
elif userOption == 2:
    userIn = int(input("Please Enter Inches: "))
    print(f"From Inches to Centimeters, your value is: {userIn * 2.54}")
else:
    print("You did not enter a valid option!")