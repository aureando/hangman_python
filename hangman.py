import random

def choisir_mot():
  """Choisit un mot aléatoire parmi une liste"""
  mots = ["chat", "chien", "oiseau", "poisson"]
  return random.choice(mots)

def jouer():
  mot_a_trouver = choisir_mot()
  mot_affiche = "_" * len(mot_a_trouver)
  essais_restants = 6

  while essais_restants > 0:
    print("Mot à trouver :", mot_affiche)
    lettre = input("Saisissez une lettre : ")

    if lettre in mot_a_trouver:
      nouveau_mot_affiche = ""
      for i in range(len(mot_a_trouver)):
        if lettre == mot_a_trouver[i]:
          nouveau_mot_affiche += lettre
        else:
          nouveau_mot_affiche += mot_affiche[i]
      mot_affiche = nouveau_mot_affiche
      print("Bonne réponse!")
    else:
      print("La lettre n'est pas dans le mot.")
      essais_restants -= 1

    if "_" not in mot_affiche:
      print("Félicitations, vous avez gagné!")
      break

  if essais_restants == 0:
    print("Désolé, vous avez perdu. Le mot était :", mot_a_trouver)

jouer()