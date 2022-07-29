"""
Différentes exceptions sont soulevées pour différentes raisons.
Exceptions courantes :
ImportError : une importation échoue ;
IndexError : une liste est indexée avec un numéro hors plage ;
NameError : une variable inconnue est utilisée ;
SyntaxError : le code ne peut pas être analysé correctement ;
TypeError : une fonction est appelée sur une valeur d'un type inapproprié ;
ValueError : une fonction est appelée sur une valeur du type correct, mais avec une valeur inappropriée.
Python a plusieurs autres exceptions intégrées, telles que ZeroDivisionError et OSError. Les bibliothèques tierces définissent également souvent leurs propres exceptions.
"""

""" gestion des exceptions """

try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occured due to zero division")
    
#output:
An error occured due to zero division
______________________________________________________________________________________________________

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("An error occured due to zero division")
except (ValueError, TypeError):
    print("Error occured")

#output:
Error occured   # sans rajouter l'exception sur TypeError => TypeError: unsupported operand type(s) for +: 'int' and 'str'
______________________________________________________________________________________________________

""" 
finally

Après une instruction try/except, un bloc finally peut suivre. Il s'exécutera après le bloc try/except, peu importe si une exception s'est produite ou non.
Le bloc finally est utile, par exemple, lorsque vous travaillez avec des fichiers et des ressources : il peut être utilisé pour s'assurer que les fichiers ou les ressources sont fermés ou libérés, qu'une exception se produise ou non.
"""

try:
    print("hello")
    print(1 / 0)
except ZeroDivisionError:
    print("An error occured due to zero division")
finally:
    print("this code will run no matter what")
    
#output:
hello
An error occured due to zero division
this code will run no matter what
______________________________________________________________________________________________________

"""
L'instruction else peut également être utilisée avec les instructions try/except.
Dans ce cas, le code qu'il contient n'est exécuté que si aucune erreur ne se produit dans l'instruction try.
"""

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)
try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

#output:
1
3
4
______________________________________________________________________________________________________

""" Lever des exceptions
Vous pouvez lever (ou déclencher) des exceptions lorsqu'une condition se produit.
Par exemple, lorsque vous prenez une entrée utilisateur qui doit être dans un format spécifique, vous pouvez lever une exception lorsqu'elle ne répond pas aux exigences.
Ceci est fait en utilisant l'instruction raise.
"""

num = 102
if num > 100:
    raise ValueError("number greater than 100")

#output:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError
______________________________________________________________________________________________________

try:
    name = input()
    if len(name) <4:
        raise ValueError ("Invalid Name")   

except ValueError:
    print("Invalid Name")

else:
    print("Account Created")
    
"""
Sample Input:
abc
"""

#output:
Invalid Name
______________________________________________________________________________________________________
