# -----------------------------------------------------------------#
# Exercices
import itertools
import json
import random
import sys


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def modulo(a, b):
    return a % b


def concat(a: str, b: str, c: str) -> str:
    return a + b + c


def water_state(a: int) -> str:
    if a < 0:
        return "SOLIDE"
    elif a <= 100:
        return "LIQUIDE"
    else:
        return "GAZEUX"


def sum_int(a: int) -> int:
    somme = 0
    for i in range(a):
        somme += i
    return somme


def zero_present(liste: list) -> str:
    try:
        return "0 trouvé à la position " + str(liste.index(0))
    except ValueError:
        return "0 non trouvé"


def maximum_integer(a: int) -> list:
    somme = 0
    i = 0
    ints = []
    while somme < a:
        ints.append(i)
        i += 1
        somme += i
    return ints


def h_existe(a: list) -> list:
    result = []
    for word in a:
        if (len(word) > 3) and "h" in str.lower(word):
            result.append(word)
    return result


def vowel_index(a: str) -> dict:
    result = {}
    vowel = 0
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(a)):
        if a[i] in vowel_list:
            vowel += 1
            result.update({i: a[i]})
    print("Nombre de voyelles : " + str(vowel))
    return result


def add_dict(dict_1: dict, dict_2: dict) -> dict:
    result = {}
    for i in (dict_1.keys()):
        result.update({i: dict_1[i]})
    for i in (dict_2.keys()):
        if i not in dict_1.keys():
            result.update({i: dict_2[i]})
        else:
            result.update({i: dict_1[i] + dict_2[i]})
    return result


# -----------------------------------------------------------------#

def my_list():
    list_test = []
    menu = "Choisissez parmi les 5 options suivantes \n" \
           "1: Ajouter un élément \n" \
           "2: Retirer un élément \n" \
           "3: Afficher la liste \n" \
           "4: Vider la liste \n" \
           "5: Quitter \n" \
           "Votre choix -> "

    menu_choice = ["1", "2", "3", "4", "5"]
    separator = "-" * 50
    while True:
        user_choice = ""
        while user_choice not in menu_choice:
            user_choice = input(menu)
            if user_choice not in menu_choice:
                print("\n Veuillez choisir une option valide")
                print(separator)
            else:
                match user_choice:
                    case "1":
                        add = input("Quel élément voulez vous rajouter : ")
                        list_test.append(add)
                        print(f"L'élément '{add}' a bien été ajouter")
                        print(separator)
                    case "2":
                        rmv = input("Quel élément voulez vous retirer ? ")
                        if rmv not in list_test:
                            print(f"L'élément '{rmv}' n'est pas contenu dans la liste")
                            print(separator)
                        else:
                            list_test.remove(rmv)
                            print(f"L'élément '{rmv}' retiré")
                            print(separator)
                    case "3":
                        if list_test:
                            print("Voici le contenu de la liste : ")
                            for i, item in enumerate(list_test, 1):
                                print(f"{i}. {item}")
                        else:
                            print("Votre liste est vide ..")
                            print(separator)
                    case "4":
                        list_test.clear()
                        print(separator)
                    case "5":
                        print("A bientôt !")
                        print(separator)
                        sys.exit()
        print(separator)


# -----------------------------------------------------------------#
# Mot de passe

def password_check(pwd) -> bool:
    SpecialChar = ['$', '@', '#', '%', '+', '-', '*', '!', '?']
    result = True
    if not any(char.isdigit() for char in pwd):
        result = False
    if not any(char.isupper() for char in pwd):
        result = False
    if not any(char.islower() for char in pwd):
        result = False
    if not any(char in SpecialChar for char in pwd):
        result = False
    if result:
        return result


def identifiers():
    username = input("Entrez un nom d'utilisateur : \n")
    separator = "-" * 50
    print(len(username))
    while len(username) <= 2 or len(username) >= 19 or username.isdigit():
        username = input("Entrez un nom d'utilisateur entre 3 et 20 caractères contenant au moins 1 lettre : \n")
    else:
        print(f"Your user name is : {username}")
        print(separator)
        pwd = input("Entrez un mot de passe (minimum 8 caractères) : \n")
    while len(pwd) == 0:
        pwd = input("Veuillez entrer un mot de passe : \n")
    else:
        while not password_check(pwd):
            pwd = input("Veuillez entrez un mot de passe contenant au moins un chiffre, une lettre minuscule"
                        ", une lettre majuscule ainsi qu'1 caractère spécial (\'$@#%+-*!?\') : \n")

    print(f"Vos identifiants de connexion sont  : \n{username} - {pwd}")
    print(separator)


# -----------------------------------------------------------------#
# Class


class Account(object):
    accounts = []
    _idCounter = itertools.count()

    def __init__(self, name: str, firstname: str, balance: int):
        self.id = next(Account._idCounter)
        self.name = name
        self.firstName = firstname
        self.balance = balance
        Account.accounts.append(self)

    def payement(self, amount: int):
        self.balance = self.balance + amount
        print(f"Vous avez effectué un dépôt de {amount} € sur le compte de {self.name} {self.firstName}")

    def pullOut(self, amount: int):
        if self.balance < 0:
            print(
                f"Votre compte est débiteur de {self.balance} €, vous ne pouvez pas faire de virement\n")
        elif (self.balance - amount) < 0:
            print(
                f"Votre compte n'a pas les fond suffisants, vous allez être à découvert de {self.balance - amount} €\n")
            self.balance = self.balance * 95 / 100
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - amount

    def transfert(self, count, amount: int):
        self.pullOut(amount)
        count.payement(amount)

    @staticmethod
    def createAccount():
        name: str = input("Veuillez rentrez le nom : ")
        firstname: str = input("Veuillez rentrez le prenom : ")
        balance = input(f"Veuillez rentrez le solde du compte de {name} {firstname} : ")
        return Account(name, firstname, int(balance))

    @staticmethod
    def viewAllAccounts() -> json:
        jsonResult = []
        for account in Account.accounts:
            accountDict = {'id': account.id, 'name': account.name, 'firstname': account.firstName,
                           'balance': account.balance}
            jsonAccount = json.dumps(accountDict)
            jsonResult.append(jsonAccount)
        print(jsonResult)

    def __str__(self) -> str:
        return f'id: {self.id} \nname: {self.name} \nfirstname: {self.firstName} \nbalance: {self.balance} \n'


class CheckingAccount(Account):

    def __init__(self, name, firstname, balance):
        super().__init__(name, firstname, balance)

    def payement(self, amount):
        super().payement(amount)

    def pullOut(self, amount):
        super().pullOut(amount)

    def transfert(self, count, amount):
        super().transfert(count, amount)

    @staticmethod
    def createAccount():
        return Account.createAccount()

    @staticmethod
    def viewAllAccounts():
        Account.viewAllAccounts()

    def __str__(self) -> str:
        return super().__str__()


# MonCompte = CheckingAccount("Thomas", "Berta", 1000)
# MonCompte2 = CheckingAccount("Alex", "Tom", 1500)
# CheckingAccount.viewAllAccounts()
# MonCompte.payement(200)
# MonCompte2.pullOut(100)
# MonCompte.transfert(MonCompte2, 2000)
CheckingAccount.createAccount()
CheckingAccount.createAccount()
CheckingAccount.createAccount()
CheckingAccount.viewAllAccounts()

# -----------------------------------------------------------------#

# print(multiply(2, 5))
# print(modulo(10, 3))
# print(divide(9, 3))
# print(modulo(12, 5))
# print(concat("Bienvenue ", "chez ", "Scalian"))
# print(water_state(-12))
# print(sum_int(12))
# print(zero_present([2, 8, 7, 4, 9]))
# print(maximum_integer(1253))
# print(vowel_index("Lorem ipsum dolor sit ametconsectetur adipiscin"))
# print(h_existe(["Python", "Java", "PHP", "HTML", "Pandas", "Symfony", "High level language"]))
# print(add_dict({"un": 2, "deux": 3, "trois": 1}, {"deux": 1, "quatre": 3, "cinq": 2, "six":1}))
# my_list()
# identifiers()
