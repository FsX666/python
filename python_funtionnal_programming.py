"""programmation fonctionnelle"""

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five, 10))

#output:
20
______________________________________________________________________________________________________

"""lambdas (fonction qui s'execute à la volée)"""

def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#s'ecrit:
print((lambda x: x**2 + 5*x + 4) (-4))
______________________________________________________________________________________________________
#exemple calcul de pourcentage
price = int(input())
perc = int(input())

res = (lambda x,y:x*y/100)(price, perc)

print(res)
______________________________________________________________________________________________________

"""map (s'applique sur des listes ou des itérables)"""

def add_five(x):
        return x+5
    
nums = [11,22,33,44,55]
result = list(map(add_five, nums))        ou   result = list(map(lambda x: x+5, nums))
print(result)

#output:
[16, 27, 38, 49, 60]
______________________________________________________________________________________________________

"""filter (s'applique sur des listes ou des itérables)"""

nums = [11,22,33,44,55]
res= list(filter(lambda x: x%2==0, nums))
print(res)

#output:
[22, 44]
______________________________________________________________________________________________________

"""generateurs
Les générateurs sont un type d'itérable, comme les listes ou les tuples.
Contrairement aux listes, elles ne permettent pas l'indexation avec des indices arbitraires, mais elles peuvent toujours être parcourues avec des boucles for.
Ils peuvent être créés à l'aide de fonctions et de l'instruction yield."""

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
    
#output:
5
4
3
2
1
______________________________________________________________________________________________________

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

#output:
[0, 2, 4, 6, 8, 10]
______________________________________________________________________________________________________

"""decorateurs
Les décorateurs permettent de modifier des fonctions à l'aide d'autres fonctions.
C'est idéal lorsque vous avez besoin d'étendre les fonctionnalités de fonctions que vous ne souhaitez pas modifier.
"""

def decor(func):
    def wrap():
        print("===============")
        func()
        print("===============")
    
    return wrap

def print_hello():                              ou      @decor
    print("hello world!")                               def print_hello():
                                                            print("hello world!")
decorated = decor(print_hello)
decorated()                                             print_hello()

#output:
===============
hello world!
===============
______________________________________________________________________________________________________

"""recursivité
La récursivité est un concept très important en programmation fonctionnelle.
La partie fondamentale de la récursivité est l'auto-référence - les fonctions s'appelant elles-mêmes. Il est utilisé pour résoudre des problèmes qui peuvent être décomposés en sous-problèmes plus faciles du même type.

Un exemple classique de fonction implémentée de manière récursive est la fonction factorielle, qui trouve le produit de tous les entiers positifs en dessous d'un nombre spécifié.
Par exemple, 5 ! (5 factoriel) est 5 * 4 * 3 * 2 * 1 (120). Pour implémenter cela de manière récursive, notez que 5! = 5 * 4 !, 4 ! = 4 * 3 !, 3 ! = 3 * 2 !, et ainsi de suite. Généralement, n! = n * (n-1)!.
De plus, 1 ! = 1. C'est ce qu'on appelle le cas de base, car il peut être calculé sans effectuer d'autres factorielles.
Vous trouverez ci-dessous une implémentation récursive de la fonction factorielle.
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
        
print(factorial(5))

#output:
120
______________________________________________________________________________________________________

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))

#output:
True
False
______________________________________________________________________________________________________

""" *args """

def function(named_arg, *args):
    print(named_arg)
    print(args)
    
function(1,2,3,4,5)

#output:
1
(2, 3, 4, 5)
______________________________________________________________________________________________________

""" *kwargs """

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
    print(args)

my_func(2, 3, 4, 5, 6, a=7, b=8)

#output:
{'a': 7, 'b': 8}
(4, 5, 6)