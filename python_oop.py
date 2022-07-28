"""programmation orientée objets"""

""" classes """


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
    
    def bark(self):
        print("Miaou!")


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)
felix.bark()
_____________________________________________________________________________________________________

""" l'héritage """
"""
L'héritage fournit un moyen de partager des fonctionnalités entre les classes.
Imaginez plusieurs classes, chat, chien, lapin et ainsi de suite. Bien qu'ils puissent différer à certains égards (seul Chien peut avoir la méthode aboiement), ils sont susceptibles d'être similaires dans d'autres (tous ayant les attributs couleur et nom).
Cette similitude peut être exprimée en les faisant tous hériter d'une superclasse Animal, qui contient la fonctionnalité partagée.
Pour hériter d'une classe d'une autre classe, placez le nom de la superclasse entre parenthèses après le nom de la classe.
"""

class Animal:  #superclasse
    def __init__(self, name, color): 
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):  #sous-classe
    def bark(self):
        print("woof!")

fido = Dog("Fido", "brown")
print(fido.name)
print(fido.color)
fido.bark()

#output:
Fido
brown
woof!
______________________________________________________________________________________________________

""" surcharge de classe"""

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grrr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Maxx","grey")
husky.bark()

#output:
Woof
______________________________________________________________________________________________________

""" 
La fonction super est une fonction utile liée à l'héritage qui fait référence à la classe parent. 
Il peut être utilisé pour trouver la méthode avec un certain nom dans la superclasse d'un objet.
"""

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()   # super().spam() appelle la méthode spam de la superclasse

B().spam()

#output:
2
1
______________________________________________________________________________________________________

""" 
Les méthodes magiques sont des méthodes spéciales qui ont des traits de soulignement doubles (dunders) au début et à la fin de leurs noms.
Elles sont utilisés pour créer des fonctionnalités qui ne peuvent pas être représentées comme une méthode normale.
L'une de leurs utilisations courantes est la surcharge d'opérateurs.
Cela signifie définir des opérateurs pour des classes personnalisées qui permettent d'utiliser des opérateurs tels que + et * sur celles-ci.
Un exemple de méthode magique est __add__ pour +.
"""

class Vector2D:
    def __init__(self, x ,y):
        self.x = x 
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3 ,9)
result = first + second
print(result.x)
print(result.y)

#output:
8
16

"""
La méthode __add__ permet de définir un comportement personnalisé pour l'opérateur + dans notre classe.
Comme vous pouvez le voir, il ajoute les attributs correspondants des objets et renvoie un nouvel objet, contenant le résultat.
Une fois défini, nous pouvons ajouter deux objets de la classe ensemble.
"""

"""
exemple de methodes magiques

__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

L'expression x + y est traduite en x.__add__(y).
Cependant, si x n'a pas implémenté __add__, et que x et y sont de types différents, alors y.__radd__(x) est appelé.
Il existe des méthodes r équivalentes pour toutes les méthodes magiques mentionnées ci-dessus.

__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

Si __ne__ n'est pas implémenté, il renvoie l'opposé de __eq__.
Il n'y a pas d'autres relations entre les autres opérateurs.

__len__ pour len()
__getitem__ pour l'indexation
__setitem__ pour l'affectation aux valeurs indexées
__delitem__ pour supprimer les valeurs indexées
__iter__ pour l'itération sur les objets (par exemple, dans les boucles for)
__contains__ pour dans

autres méthodes:
__call__ pour appeler des objets en tant que fonctions
__int__ pour convertir des objets en types intégrés
__str__ pour convertir des objets en types intégrés
__repr__ pour la représentation sous forme de chaîne de l'instance

"""

class SpecialString:
    def __init__(self, cont):
        self.cont = cont
        
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

#output:
spam
============
Hello world!

#autre exemple

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index]

    def __len__(self):
        return len(self.cont)

vague_list = VagueList(["A","B","C","D","E"])
print(len(vague_list))
print(vague_list[2])

#output:
5
C
______________________________________________________________________________________________________

"""
Masquage des données
Un élément clé de la programmation orientée objet est l'encapsulation, qui implique le conditionnement de variables et de fonctions associées dans un seul objet facile à utiliser - une instance d'une classe.
Un concept connexe est le masquage des données, qui stipule que les détails d'implémentation d'une classe doivent être masqués et qu'une interface standard propre doit être présentée à ceux qui souhaitent utiliser la classe.
Dans d'autres langages de programmation, cela se fait généralement avec des méthodes et des attributs privés, qui bloquent l'accès externe à certaines méthodes et attributs d'une classe.
La philosophie Python est légèrement différente. Il est souvent dit que "nous sommes tous des adultes consentants ici", ce qui signifie que vous ne devez pas imposer de restrictions arbitraires à l'accès à certaines parties d'une classe. Par conséquent, il n'y a aucun moyen d'imposer qu'une méthode ou un attribut soit strictement privé.

Les méthodes et attributs faiblement privés ont un seul trait de soulignement au début.
Cela signale qu'ils sont privés et ne doivent pas être utilisés par du code externe. Cependant, il ne s'agit généralement que d'une convention et n'empêche pas le code externe d'y accéder.

Les méthodes et attributs fortement privés ont un double trait de soulignement au début de leur nom. Cela provoque la déformation de leurs noms, ce qui signifie qu'ils ne sont pas accessibles depuis l'extérieur de la classe.
Le but n'est pas de s'assurer qu'ils restent privés, mais d'éviter les bogues s'il existe des sous-classes qui ont des méthodes ou des attributs avec les mêmes noms.
Les méthodes mutilées par nom sont toujours accessibles de l'extérieur, mais sous un nom différent. La méthode __privatemethod de la classe Spam est accessible en externe avec _Spam__privatemethod.
"""

#exemple de masquage faiblement privé
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0,value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

#output:
Queue([1, 2, 3])
Queue([0, 1, 2, 3])
Queue([0, 1, 2])
[0, 1, 2]

#exemple de masquage fortement privé

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
#s.print_egg()  # AttributeError: 'Spam' object has no attribute 'print_egg'.
print(s._Spam__egg)
#print(s.__egg) # AttributeError: 'Spam' object has no attribute '__egg'

#output:
7
______________________________________________________________________________________________________

"""
Méthodes de classe:
Les méthodes des objets que nous avons examinés jusqu'ici sont appelées par une instance d'une classe, qui est ensuite transmise au paramètre self de la méthode.
Les méthodes de classe sont différentes -- elles sont appelées par une classe, qui est passée au paramètre cls de la méthode.
Une utilisation courante de celles-ci sont les méthodes de fabrique, qui instancient une instance d'une classe, en utilisant des paramètres différents de ceux habituellement passés au constructeur de la classe.
Les méthodes de classe sont marquées par un décorateur de méthode de classe.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

#output:
25
______________________________________________________________________________________________________

""" Methodes statiques sont similaires aux méthodes de classe, sauf qu'elles ne reçoivent aucun argument supplémentaire ; elles sont identiques aux fonctions normales appartenant à une classe.
Ils sont marqués avec le décorateur staticmethod."""

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            print("Ingredient {} KO".format(topping))
            raise ValueError("No pineapples!")
        else:
            print("Ingredient {} OK".format(topping))
            return True

ingredients = ["cheese","onions","spam","pineapple"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

#output:
Ingredient cheese OK
Ingredient onions OK
Ingredient spam OK
Ingredient pineapple KO
Traceback (most recent call last):
  File "/test.py", line 16, in <module>
    if all(Pizza.validate_topping(i) for i in ingredients):
  File "test.py", line 16, in <genexpr>
    if all(Pizza.validate_topping(i) for i in ingredients):
  File "test.py", line 10, in validate_topping
    raise ValueError("No pineapples!")
ValueError: No pineapples!
______________________________________________________________________________________________________

"""
Les propriétés permettent de personnaliser l'accès aux attributs d'instance.
Ils sont créés en plaçant le décorateur de propriété au-dessus d'une méthode, ce qui signifie que lorsque l'attribut d'instance portant le même nom que la méthode est accédé, la méthode sera appelée à la place.
Une utilisation courante d'une propriété consiste à rendre un attribut en lecture seule.
"""

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

#output:
False
Traceback (most recent call last):
  File "test.py", line 13, in <module>
    pizza.pineapple_allowed = True
AttributeError: can't set attribute 'pineapple_allowed'
______________________________________________________________________________________________________

"""
Les propriétés peuvent également être définies en définissant des fonctions setter/getter.
La fonction setter définit la valeur de la propriété correspondante.
Le getter obtient la valeur.
Pour définir un setter, vous devez utiliser un décorateur du même nom que la propriété, suivi d'un point et du mot-clé setter.
Il en va de même pour la définition des fonctions getter
"""

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "test!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

#output:
False
Enter the password: test!
True
______________________________________________________________________________________________________

"""shooting game"""

class Enemy():
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
  x = input()
  if x == 'exit':
    break
  elif x == 'laser':
    weapon = "laser"
    a.hit()
  elif x == "gun":
    weapon = "gun"
    m.hit()
    
    
"""
Sample Input:
laser
laser
gun
exit
"""

#output:
Monster has 2 lives
Alien has 4 lives
Alien has 3 lives
Alien has 2 lives
Alien has 1 lives
Alien killed
______________________________________________________________________________________________________