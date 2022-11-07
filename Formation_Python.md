# Python

***
***
#### 1. Créer 5 variables python représentantes les différents types possibles en python. 
***
#### 2. Définir des fonctions avec arguments qui renvois les différents résultats demandés et afficher les résultats.
```
- Multiplication de 2 nombres
- Division de 2 entiers 
- Modulo de 2 entiers
- Concatenation de 3 chaines de caractères
```
***
#### 3. Ecrire une fonction qui prend en entrée une température t et qui renvoie l'état de l'eau à cette température et afficher le résultat. 
```
C'est à dire "SOLIDE", "LIQUIDE" ou "GAZEUX". On prendra comme conditions les suivantes : 
- Si la température est strictement négative alors l'eau est à l'état solide.
- Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
- Si la température est strictement supérieure à 100.
Entrée : Une température t.
Sortie : L'état de l'eau à cette température parmi les trois possibilités : 
"SOLIDE", "LIQUIDE" ou "GAZEUX"
```
***
#### 4. Ecrire une fonction qui renvoi la somme des entiers de 1 à 673 et afficher le résultat.
***
#### 5. Ecrire une fonction qui prend en entrée une liste et renvoit en sortie si cette liste contient 0 ou non.
```
Pour cela, il faut renvoyer les chaines de caractères "0 trouvé" ou "0 non trouvé".
Entrée : Une liste de nombres nommée liste.
Sortie : "0 trouvé" ou "0 non trouvé" selon les cas.
```
***
#### 6. Ecrire une fonction qui retourne une liste contenant tout les entiers jusqu'à un nombre défini et afficher le résultat.
***
#### 7. Ecrire une fonction qui retourne une liste contenant les chaines de caractères de plus de 3 caractères et contenant un "h" de la liste ci-dessous et afficher le résultat.
```
liste = ["Python", "Java", "PHP", "HTML", "Pandas", "Symfony", "High level language]
```
***
#### 8. Ecrire une fonction qui affiche le nombre de voyelles dans un texte et renvoi un dictionnaire avec leurs positions dans ce texte et afficher le résultat.
***
#### 9. Ecrire une fonction qui retourne un dictionnaire contenant l'intégralité de 2 dictionnaires passés en arguments en additionant les valeurs où la clef est identique.
```
Exemple :
dict_1 = {"un": 2, "deux": 3, "trois": 1, "cinq": 4}
dict_2 = {"deux": 1, "quatre": 3, "cinq": 2, "six":1}

Resultat attendu : 
{'un': 2, 'deux': 4, 'trois': 1, 'cinq': 6, 'quatre': 3, 'six': 1}
```  
***
#### 10. Créer une fonction qui, en ligne de commande, qui permet à l'utilisateur d'utiliser une liste et lui proposer différentes solutions :
```
- Ajouter un élément à la liste
- Retirer un élément à la liste
- Afficher la liste
- Vider la liste
- Quitter le programme
```
***
#### 11. Créer une fonction qui, en ligne de commande, demande à l'utilisateur de créer un identifiant et un mot de passe avec les conditions suivantes :
```
- Identifiant : 
    Entre 3 et 20 caractères
    Contenant au moins 1 lettre
- Mot de passe : 
    Au moins  : 8 caractères    
                1 lettre minuscule
                1 lettre majuscule
                1 caractère spécial : #?!@$%^&*-            
```
Une fois que tout est validés, afficher à l'utilisateur son identifiant et son mot de passe.
Tant que tout les critères ne sont pas remplis, l'utilisateur doit réeffectuer sa saisie.
***
***
## Exemples de correction
***
#### 1.
````
example_string = "Bienvenue chez Scalian!"
example_char = 'a'
example_int = 5
example_float = 10.0
example_boolean = True

print(type(example_string))
print(type(example_char))
print(type(example_int))
print(type(example_float))
print(type(example_boolean))
````
***
#### 2.
````
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulo(a, b):
    return a % b

def concat(a: str, b: str, c: str) -> str:
    return a + b + c

print(multiply(2, 5))
print(divide(9, 3))
print(modulo(12, 5))
print(concat("Bienvenue ", "chez ", "Scalian"))
````
***
#### 3.
````
def water_state(a: int) -> str:
    if a < 0:
        return "SOLIDE"
    elif a <= 100:
        return "LIQUIDE"
    else:
        return "GAZEUX"
        
print(water_state(-12))        
````
***
#### 4.
````
def sum_int(a: int) -> int:
    somme = 0
    for i in range(a):
        somme += i
    return somme  
    
    print(sum_int(12))
````
***
#### 5.
````
def zero_present(liste: list) -> str:
    try:
        return "0 trouvé à la position " + str(liste.index(0))
    except ValueError:
        return "0 non trouvé"

print(zero_present([2, 8, 7, 4, 9, 0]))
````
***
#### 6.
````
def max_integer(a: int) -> list:
    somme = 0
    i = 0
    ints = []
    while somme < a:
        ints.append(i)
        i += 1
        somme += i
    return ints
    
print(max_integer(1253))    
````
***
#### 7.
````
def h_existe(a: list) -> list:
    result = []
    for word in a:
        if (len(word) > 3) and "h" in str.lower(word):
            result.append(word)
    return result
    
print(h_existe(["Python", "Java", "PHP", "HTML", "Pandas", "Symfony", "High level language"]))
````
***
#### 8.
````
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

print(vowel_index("Lorem ipsum dolor sit ametconsectetur adipiscin"))
````
***
#### 9.
````
def result_dict(dict_1: dict, dict_2: dict) -> dict:
    result = {}
    for i in (dict_1.keys()):
        result.update({i: dict_1[i]})
    for i in (dict_2.keys()):
        if i not in dict_1.keys():
            result.update({i: dict_2[i]})
        else:
            result.update({i: dict_1[i] + dict_2[i]})
    return result

print(result_dict({"un": 2, "deux": 3, "trois": 1, "cinq": 4}, {"deux": 1, "quatre": 3, "cinq": 2, "six":1}))
````
***
#### 10. 
````
import sys
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
                       
my_list()
````
***
#### 11.
````
def password_check(pwd):
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
    
identifiers()
````

