"""
Data Structures

Quand utiliser un dictionnaire :
- Lorsque vous avez besoin d'une association logique entre une paire clé:valeur.
- Lorsque vous avez besoin d'une recherche rapide de vos données, basée sur une clé personnalisée.
- Lorsque vos données sont constamment modifiées. N'oubliez pas que les dictionnaires sont modifiables.

Quand utiliser les autres types :
- Utilisez des listes si vous avez une collection de données qui n'a pas besoin d'un accès aléatoire. Essayez de choisir des listes lorsque vous avez besoin d'une collection simple, itérable et fréquemment modifiée.
- Utilisez un set si vous avez besoin d'unicité pour les éléments.
- Utilisez des tuples lorsque vos données ne peuvent/ne doivent pas changer.
Souvent, un tuple est utilisé en combinaison avec un dictionnaire, par exemple, un tuple peut représenter une clé, car il est immuable.

les listes et les dictionnaires sont mutables, ce qui n'est pas le cas des tuples et les sets
"""

""" gestion des chaines de caracteres """

print("-"*80+"\r")
print("\t \t \t \t \t hello ! \r") #avec retour a la ligne, sans saut de ligne
print("-"*80+"\n") #avec retour a la ligne avec saut de ligne
print("end")

#output:
--------------------------------------------------------------------------------
                                    hello ! 
--------------------------------------------------------------------------------

end
______________________________________________________________________________________________________

#une string peut etre indexée comme une liste
str = "Hello world!"
print(str[6])

#output:
w
______________________________________________________________________________________________________

"""gestion des listes"""

x = ['hi','hello','welcome']
print(x[2])

#output:
welcome
______________________________________________________________________________________________________

n = [2,4,6,8]
for x in n[1:3]:
    print(x)
 
#output:   
4
6
______________________________________________________________________________________________________

things = [”text", 0, [1, 2, 8], 4.56]
print(things[2][2])

#output:
8
______________________________________________________________________________________________________

""" réassignation de liste"""

nums = [5, 8, 2]
nums[1] = 42

print(nums)

#output:
[5, 42, 2]
______________________________________________________________________________________________________

""" ajout d'elements dans une liste """

nums = [1, 2, 3]
print(nums + [4, 5, 6])

#output:
[1, 2, 3, 4, 5, 6]
______________________________________________________________________________________________________

""" affichage des élements d'une liste """

words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

#output:
hello!
world!
spam!
eggs!
______________________________________________________________________________________________________

"""generation d'une liste avec des nombre de 0 à 9"""

numbers = range(10)
for x in numbers:
    print(x)

#output:
0
1
2
3
4
5
6
7
8
9

numbers = list(range(10))
print(numbers)

#output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
______________________________________________________________________________________________________

"""generation d'une liste avec des nombre de 3 à 7"""

numbers = list(range(3,8))
print(numbers)

#output:
[3, 4, 5, 6, 7]
______________________________________________________________________________________________________

"""generation d'une liste avec des nombre de 5 à 19 avec un pas de 2"""

numbers = list(range(5,20,2))
print(numbers)

#output:
[5, 7, 9, 11, 13, 15, 17, 19]
______________________________________________________________________________________________________

""" slices sur une liste """

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])   #affichage du 3eme element au 6eme element de la liste
print(squares[3:8])   #affichage du 4eme au 8eme element de la liste
print(squares[0:1])   #affiche le 1er element
print(squares[:5])    #affiche les 5ers elements
print(squares[5:])    #affiche les elements de la liste a partir du 6eme element
print(squares[::2])   #affiche tous les nombres paires
print(squares[2:8:3]) #affiche 1 element sur 3 de la liste entre le 3eme element et le 8eme
print(squares[1:-1])  #affiche a partir du 2eme element de la liste en supprimant le dernier element
print(squares[::-1])  #affiche la liste du dernier element au premier

#output:
[4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]
[0, 1, 4, 9, 16]
[25, 36, 49, 64, 81]
[0, 4, 16, 36, 64]
[4, 25]
[1, 4, 9, 16, 25, 36, 49, 64]
______________________________________________________________________________________________________

"""gestion des dictionaires"""
ages = {
    "Dave": 24,
    "Mary": 42,
    "John": 58
}
print(ages["Mary"])
print("Dave" in ages)
print("Fred" not in ages)
print(ages.get("Dave"))
print(ages.get("Fred",25))  # surcharge de la valeur recuperée

#output:
42
True
True
24
25
______________________________________________________________________________________________________

"""gestion des tuples - plus rapides que les listes mais immuables"""

words = ("spam", "eggs", "sausages")
print(word[0])

#output:
spam
______________________________________________________________________________________________________

numbers = (1,2,3)
a, b, c = numbers
print(a)
print(b)
print(c)
______________________________________________________________________________________________________

a,b = b,a #swap de variable

x,y = (1,2)
x,y = y,x
print(y)

#output:
1
______________________________________________________________________________________________________

a, b, *c, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)

#output:
1
2
[3, 4, 5, 6, 7, 8]
9
______________________________________________________________________________________________________

a, b, c, d, *e, f, g = range(20)
print(len(e))

#output:
14
______________________________________________________________________________________________________

""" gestion des sets - similaire aux listes ou dico - non ordonnés / pas d'index - plus rapides a parcourir - pas d'elements en double """

num_set = {1,2,3,4,5}
print(3 in num_set)
num_set.add(6)
num_set.remove(3)
print(num_set)
print(len(num_set))

#output:
True
{1, 2, 4, 5, 6}
5
______________________________________________________________________________________________________

"""Les sets peuvent être combinés à l'aide d'opérations mathématiques.
L'opérateur syndical | combine deux sets pour en former un nouveau contenant des éléments dans l'un ou l'autre.
L'opérateur d'intersection & obtient les éléments uniquement dans les deux.
L'opérateur de différence - obtient les éléments du premier set mais pas du second.
L'opérateur de différence symétrique ^ obtient des éléments dans l'un ou l'autre des sets, mais pas dans les deux."""

first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}
print(first|second)
print(first&second)
print(first-second)
print(second-first)
print(first^second)

#outpout:
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{4, 5, 6}
{1, 2, 3}
{8, 9, 7}
{1, 2, 3, 7, 8, 9}
______________________________________________________________________________________________________

""" gestion des listes de compréhension """

cubes = [i**3 for i in range(5)]
print(cubes)

#output:
[0, 1, 8, 27, 64]
______________________________________________________________________________________________________

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

#output:
[0, 4, 16, 36, 64]
______________________________________________________________________________________________________

