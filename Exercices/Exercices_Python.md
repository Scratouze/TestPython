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
On prendra comme conditions : 
- Si la température est strictement négative alors l'eau est à l'état solide.
- Si la température est entre 0 et 100 inclus, l'eau est à l'état liquide.
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
#### 12 . Créer un programme myBank qui permet de manipuler (dans le terminal) des comptes courants  qui hérite d'un objet compte et de ses méthodes.

Au lancement, un menu permettra à l'utilisateur d'utiliser différentes méthodes (voir exercice 10) et d'en afficher le résultat dans le terminal (pas de stockage en BDD) :
```
- Attributs :
    - idAccount (unique et auto-incrémenté)
    - lastName
    - firstName
    - balance
- Méthodes :
    1 - Voir tout les comptes
    2 - Créer un compte
    3 - Supprimer un compte
    4 - Effectuer un versement sur un compte
    5 - Effectuer un prélèvement sur un compte
    6 - Effectuer un virement entre 2 comptes 
    7 - Quitter le programme
```
Créer également 2 méthodes non appelées dans le menu qui permettront :
- Afficher un compte sous la forme :  
  id:  
  name:    
  firstname:  
  balance:  
- Renvoyer un tableau de Json de l'ensemble des comptes

***
***
