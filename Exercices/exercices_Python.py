# -----------------------------------------------------------------#
# Exercices
import itertools
import json
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
        print(f"Your user lastName is : {username}")
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
    separator = "-" * 25

    def __init__(self, lastName: str, firstName: str, balance: int):
        self.id = next(Account._idCounter)
        self.lastName = lastName
        self.firstName = firstName
        self.balance = balance
        Account.accounts.append(self)

    @staticmethod
    def createAccount():
        pass

    @staticmethod
    def deleteAccount():
        pass

    @staticmethod
    def payement(pullout: bool, targetAccountId=0, amount=0):
        pass

    @staticmethod
    def transfert():
        pass

    @staticmethod
    def viewAllJsonAccounts() -> json:
        pass

    @staticmethod
    def viewAllAccounts():
        pass

    @staticmethod
    def checkAccountId(Id: int):
        pass

    def __str__(self) -> str:
        return f'id: {self.id} \nlastName: {self.lastName} \nfirstName: {self.firstName} \nbalance: {self.balance} \n'


class CheckingAccount(Account):

    def __init__(self, lastName: str, firstName: str, balance: int):
        super().__init__(lastName, firstName, balance)

    @staticmethod
    def createAccount():
        lastName: str = input("Veuillez rentrez le nom : ")
        firstName: str = input("Veuillez rentrez le prénom : ")
        balance = "0"
        balance = input(f"Veuillez rentrez le solde du compte de {lastName} {firstName} : ")
        while not balance.isdigit():
            print(f"Veuillez ne rentrer que des chiffres pour le solde du compte !\n{CheckingAccount.separator}")
            balance = input(f"Veuillez rentrez le solde du compte de {lastName} {firstName} : ")
        print(f"{CheckingAccount.separator}\nLe compte courant de {lastName} {firstName} a été créé avec un solde de {balance} €")
        return CheckingAccount(lastName, firstName, int(balance))

    @staticmethod
    def deleteAccount():
        targetAccountId: int = int(input("Quel compte souhaitez vous supprimer (id) ? "))
        targetAccount = CheckingAccount.checkAccountId(targetAccountId)
        print(f"Le compte de {targetAccount.lastName} {targetAccount.firstName} a été supprimé")
        CheckingAccount.accounts.remove(targetAccount)

    @staticmethod
    def payement(pullout: bool, targetAccountId=0, amount=0):
        action1 = "vers" if not pullout else "depuis"
        action2 = "versement" if not pullout else "prélèvement"
        if not targetAccountId and not amount:
            targetAccountId: int = int(input(f"{action1} quel compte souhaitez vous effectuer un {action2} (id): "))
            amount = input(f"De quel montant est votre {action2} : ")
        amount = -int(amount) if pullout else int(amount)
        if not CheckingAccount.checkAccountId(targetAccountId):
            print(f"{CheckingAccount.separator}Le compte {action1} lequel vous essayer d'effectuer ce {action2} n'existe pas")
            pass
        else:
            target = CheckingAccount.checkAccountId(int(targetAccountId))
            action = "dépôt" if (amount > 0) else "retrait"
            if target.balance > 0:
                target.balance += amount
                if target.balance < 0:
                    print(
                        f"\nLe compte de {target.lastName} {target.firstName} n'a pas les fond suffisants, le compte "
                        f"va être à découvert de {target.balance} €")
                print(
                        f"{CheckingAccount.separator}\nVous avez effectué un {action} de {amount} € sur le compte de"
                        f"{target.lastName} {target.firstName}")
            else:
                print(
                    f"{CheckingAccount.separator}\nLe compte de {target.lastName} {target.firstName} est débiteur de"
                    f"{target.balance} €, vous ne pouvez pas faire de {action}")

    @staticmethod
    def transfert():
        originAccountId: int = int(input("Depuis quel compte souhaitez vous effectuer un virement (id): "))
        originAccount: CheckingAccount = CheckingAccount.checkAccountId(originAccountId)
        if not originAccount:
            print(f"Le compte depuis lequel vous essayer d'effectuer ce virement n'existe pas")
            pass
        else:
            targetAccountId: int = int(input("Vers quel compte souhaitez vous effectuer un virement (id): "))
            targetAccount: CheckingAccount = CheckingAccount.checkAccountId(targetAccountId)
            if not targetAccount:
                print(f"Le compte vers lequel vous essayer d'effectuer ce virement n'existe pas")
                pass
            else:
                amount = int(input("De quel montant est votre virement : "))
                originAccount.payement(True, originAccountId, amount)
                targetAccount.payement(False, targetAccountId, amount)

    @staticmethod
    def viewAllJsonAccounts() -> json:
        jsonResult = []
        for account in CheckingAccount.accounts:
            accountDict = {'id': account.id, 'lastName': account.lastName, 'firstName': account.firstName,
                           'balance': account.balance}
            jsonAccount = json.dumps(accountDict)
            jsonResult.append(jsonAccount)
        print(CheckingAccount.separator)
        print(jsonResult)
        print(CheckingAccount.separator)

    @staticmethod
    def viewAllAccounts():
        result = ""
        if not CheckingAccount.accounts:
            print("Il n'y a pas de compte créé")
        else:
            for account in CheckingAccount.accounts:
                result += f"id: {account.id}\nlastName: {account.lastName}\nfirstName: {account.firstName}\nbalance:"
                f"{account.balance} €\n{CheckingAccount.separator} \n"
            print(result)

    @staticmethod
    def checkAccountId(Id: int):
        accounts = CheckingAccount.accounts
        for account in accounts:
            if account.id == Id:
                return account

    def __str__(self) -> str:
        return super().__str__()


def myBank():
    print(
        f"{CheckingAccount.separator}\n{CheckingAccount.separator}\nBienvenue sur Ma Banque\n{CheckingAccount.separator}"
        f"\n{CheckingAccount.separator}")
    menu = "Choisissez parmi les 5 options suivantes \n" \
           "1: Afficher tout les comptes \n" \
           "2: Créer un compte  \n" \
           "3: Supprimer un compte \n" \
           "4: Effectuer un versement sur un compte \n" \
           "5: Effectuer un prélèvement depuis un compte \n" \
           "6: Effectuer un virement entre 2 comptes \n" \
           "7: Quitter \n" \
           "Votre choix -> "

    menu_choice = ["1", "2", "3", "4", "5", "6", "7"]
    while True:
        user_choice = ""
        while user_choice not in menu_choice:
            user_choice = input(menu)
            if user_choice not in menu_choice:
                print("\n Veuillez choisir une option valide")
                print(CheckingAccount.separator)
            else:
                print(CheckingAccount.separator)
                match user_choice:
                    case "1":
                        CheckingAccount.viewAllAccounts()
                    case "2":
                        CheckingAccount.createAccount()
                    case "3":
                        CheckingAccount.deleteAccount()
                    case "4":
                        CheckingAccount.payement(False)
                    case "5":
                        CheckingAccount.payement(True)
                    case "6":
                        CheckingAccount.transfert()
                    case "7":
                        print(f"A bientôt !\n{CheckingAccount.separator}")
                        sys.exit()
        print(CheckingAccount.separator)


myBank()


# MonCompte = CheckingAccount("Thomas", "Berta", 1000)
# MonCompte2 = CheckingAccount("Alex", "Tom", 1500)
# CheckingAccount.viewAllJsonAccounts()
# CheckingAccount.viewAllAccounts()
# MonCompte.payement(200)
# MonCompte2.pullOut(100)
# MonCompte.transfert(MonCompte2, 2000)


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
myBank()
