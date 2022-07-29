""" gestion des fichiers """

"""
Ouverture de fichiers / fermeture de fichiers

Avant qu'un fichier puisse être modifié, il doit être ouvert à l'aide de la fonction d'ouverture.
Vous pouvez spécifier le mode utilisé pour ouvrir un fichier en appliquant un second argument à la fonction open.
Envoyer "r" signifie ouvrir en mode lecture, qui est la valeur par défaut.
L'envoi de "w" signifie le mode écriture, pour réécrire le contenu d'un fichier.
L'envoi de "a" signifie le mode d'ajout, pour ajouter un nouveau contenu à la fin du fichier.

L'ajout de "b" à un mode l'ouvre en mode binaire, qui est utilisé pour les fichiers non textuels (tels que les fichiers image et son).
"""

# read mode
open("filename.txt", "r")
open("filename.txt")

# write mode
open("filename.txt", "w")

# binary write mode
open("filename.txt", "wb")

# write mode + file close
file = open("filename.txt", "w")
file.close()
______________________________________________________________________________________________________

"""
Lecture de fichiers


Le contenu d'un fichier qui a été ouvert en mode texte peut être lu à l'aide de la méthode read.
Nous avons créé un fichier books.txt sur le serveur qui inclut les titres des livres. Lisons le fichier et produisons le contenu :
"""

file = open("books.txt")
cont = file.read()
print(cont)      # cela imprimera tout le contenu du fichier
file.close()

#output:
Game Of Thrones
Harry Potter
bridget Jones
______________________________________________________________________________________________________

"""
Pour lire uniquement une certaine quantité d'un fichier, vous pouvez fournir le nombre d'octets à lire comme argument à la fonction read.
Chaque caractère ASCII est de 1 octet.
Cela lira les 5 premiers caractères du fichier, puis les 7 suivants.
L'appel de la méthode read() sans argument renverra le reste du contenu du fichier.
"""

file = open("books.txt")
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()

#output:
Game 
Of Thro
nes
Harry Potter
bridget Jones
______________________________________________________________________________________________________

"""
Pour récupérer chaque ligne d'un fichier, vous pouvez utiliser la méthode readlines() pour renvoyer une liste dans laquelle chaque élément est une ligne du fichier.
"""

file = open("books.txt")

for line in file.readlines():      # file.readlines() est une liste
    print(line)

file.close()

file = open("books.txt")

cont = file.readlines()
print("the line 1 contains: {}".format(cont[1]))

file.close()

#output:
Game Of Thrones

Harry Potter

bridget Jones

the line 1 contains: Harry Potter



#Si vous n'avez pas besoin de la liste pour chaque ligne, vous pouvez simplement parcourir la variable file 
file = open("books.txt")

for line in file:
    print(line)
    
file.close()

#output:
Game Of Thrones

Harry Potter

bridget Jones

#Dans la sortie, les lignes sont séparées par des lignes vides, car la fonction d'impression ajoute automatiquement une nouvelle ligne à la fin de sa sortie.
______________________________________________________________________________________________________

""" Ecrire dans des fichiers """

# ecrire un nouveau fichier/ecraser le contenu d'un fichier existant
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()


# ecrire dans un fichier existant
file = open("books.txt", "a")

file.write("\nThe Da Vinci Code")
file.close()

# recuperer le nombre de bytes ecrits (Pour écrire autre chose qu'une chaîne, il doit d'abord être converti en chaîne.)
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
______________________________________________________________________________________________________

""" 
travailler avec des fichiers (1)
Il est recommandé d'éviter de gaspiller des ressources en s'assurant que les fichiers sont toujours fermés après avoir été utilisés. Une façon de faire est d'utiliser try et finally
"""

try:
    f = open("books.txt")
    cont = f.read()
    print(cont)
finally:
    f.close()
______________________________________________________________________________________________________

""" 
travailler avec des fichiers (2)
Une autre façon de procéder consiste à utiliser des instructions with. Cela crée une variable temporaire (souvent appelée f), qui n'est accessible que dans le bloc indenté de l'instruction with.
"""

try:
    with open("books.txt") as f:
        print(f.read())
except:
    print("Error")
______________________________________________________________________________________________________

""" Title Encoder """

file = open("books.txt", "r")

for line in file.readlines():
    encoded_words=""
    title = line.replace("\n","").split(' ')
    print("Original title: {}".format(title))
    for each_word in title:
        encoded_title += each_word[:1]
    print("Encoded title: {}".format(encoded_title))

file.close()

#output:
Original title: ['Game', 'Of', 'Thrones']
Encoded title: GOT
Original title: ['Harry', 'Potter']
Encoded title: HP
Original title: ['bridget', 'Jones']
Encoded title: bJ