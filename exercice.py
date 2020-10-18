#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        for nb in range(0, 9):
            list.append(input('Veuillez entrer un nombre entier: '))

    return list == sorted(list)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        mot1 = input("Veuillez entrer un mot : ")
        mot2 = input("Veuillez entrer un deuxieme mot : ")
    if len(mot1) == len(mot2):
        for lettre in mot1:
            mot2.remove(lettre)
        if len(mot2) == 0:
            print("Anagramme")
        else:
            print("raté!")

    return False


def contains_doubles(items: list) -> bool:
    for element in items:
        if items.count(element) > 1:
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    moyenne = {}
    for étudiant, résultats in student_grades.items():
        somme = 0
        for note in résultats:
            somme += note
        moyenne[étudiant] = somme / len(résultats)

    moyenneLaPlusHaute = max(moyenne.values())
    for étudiant, moyenne in moyenne.items():
        if moyenne[étudiant] == moyenneLaPlusHaute:
            étudiantLePlusFort = étudiant

    return {étudiantLePlusFort: moyenneLaPlusHaute}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données
    nomRecette = input("Quel est le nom de la recette? ")
    recette = {}
    recette[nomRecette] = []
    ajouterIngrédient = True
    while ajouterIngrédient:
        recette[nomRecette].append(input("Veuillez entrer un ingrédient: "))
        ajouterIngrédient = input("Voulez vous ajouter un autre ingrédient? Entrer 'oui' ou 'non': ")
        ajouterIngrédient = ajouterIngrédient == 'oui'

    return recette


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nomRecetteVoulue = input("Veuillez choisir une recette: ")
    for recette, listeIngrédients in ingredients.items():
        if recette == nomRecetteVoulue:
            print(listeIngrédients)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
