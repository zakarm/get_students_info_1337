import os

from colorama import Fore, Back, Style


def style():
    print(Fore.GREEN)
    print(" ██╗██████╗ ██████╗ ███████╗    ██╗███╗   ██╗███████╗ ██████╗")
    print("███║╚════██╗╚════██╗╚════██║    ██║████╗  ██║██╔════╝██╔═══██╗")
    print("╚██║ █████╔╝ █████╔╝   ██╔╝     ██║██╔██╗ ██║█████╗  ██║   ██║")
    print(" ██║ ╚═══██╗ ╚═══██╗  ██╔╝      ██║██║╚██╗██║██╔══╝  ██║   ██║")
    print(" ██║██████╔╝██████╔╝  ██║       ██║██║ ╚████║██║     ╚██████╔╝")
    print(" ╚═╝╚═════╝ ╚═════╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝")
    print(Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "                                                    by zmrabet\n"+ Style.RESET_ALL)


def error_case():
    with open("42data.txt", 'r') as file:
        content = file.read()
        if "uidNumber" not in content:
            os.system("clear")
            print(Fore.RED+"Wrong Login !"+Style.RESET_ALL);
            quit()


def get_data(word):
    with open("42data.txt", 'r') as file:
        content = file.readlines()
        for line in content:
            if line.find(word) != -1:
                print("__________________________________")
                print(line, end="")
                print("__________________________________")
                input()
                os.system("clear")


def menu():
    data = 0
    login = input(Fore.YELLOW+"Enter Login : "+Style.RESET_ALL)
    os.system("ldapsearch uid="+login+" > 42data.txt")
    os.system("clear")
    error_case()
    while data != '5':
        style()
        print(Fore.RED+" 1"+Style.RESET_ALL+" - Get Phone Number")
        print()
        print(Fore.RED+" 2"+Style.RESET_ALL+" - Get Mail")
        print()
        print(Fore.RED+" 3"+Style.RESET_ALL+" - Get Full Name")
        print()
        print(Fore.RED+" 4"+Style.RESET_ALL+" - Get Intra Profile")
        print()
        print(Fore.RED+" 5"+Style.RESET_ALL+" - Exit")
        print()
        data = input(Fore.YELLOW+"Choose One : "+Style.RESET_ALL)
        os.system("clear")
        if data == '1':
            get_data("mobile:")
        elif data == '2':
            get_data("alias:")
        elif data == '3':
            get_data("cn:")
        elif data == '4':
            print("__________________________________________")
            print("https://profile.intra.42.fr/users/"+login)
            print("__________________________________________")
            input()
            os.system("clear")
        elif data == '5':
            quit()


def main():
    style()
    menu()


if __name__ == "__main__":
    main()

