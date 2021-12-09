nombre_mots = 0
phrase = input("Écrivez une phrase")
liste_mots = phrase.split(" ")
nombre_mots = len(liste_mots)
nombre_min_lettres = 4
if nombre_mots > 0:
    for i in liste_mots.copy():
        if len(i) <= nombre_min_lettres:
            liste_mots.remove(i)
else:
    print("La liste est vide")
proportion = round(100*len(liste_mots)/nombre_mots,2)
print("Proportion de mots de plus de {} lettres : {} %".format(nombre_min_lettres,proportion))