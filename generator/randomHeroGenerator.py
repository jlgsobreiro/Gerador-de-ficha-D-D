import random
import rstr

classe = ["Barbarian",
              "Bard",
              "Cleric",
              "Druid",
              "Fighter",
              "Monk",
              "Mystic",
              "Paladin",
              "Ranger",
              "Rogue",
              "Sorcerer",
              "Warlock",
              "Wizard"]

raca = ["Dragonborn",
            "Dwarf",
            "Eladrin",
            "Elf",
            "Gnome",
            "Half-elf",
            "Half-orc",
            "Halfling",
            "Human",
            "Tiefling"]

def classeLista():
    return classe

def racaLista():
    return raca

def randomHero():
    nome = rstr.xeger("[A-Z](((([aeiou]{0,1})|([bcdfghjklmnpqrstvwyxz]{1,2}))|(([aeiou]{1,2})|([bcdfghjklmnpqrstvwyxz]{0,1})))|([aeiou][bcdfghjklmnpqrstvwyxz])){3,6}")
    level = random.uniform(1,20)
    level = int(round(level))



    randClasse = random.uniform(0,len(classe)-1)
    randClasse = int(round(randClasse))


    randRaca = random.uniform(0,len(raca)-1)
    randRaca = int(round(randRaca))


    post = {"Nome" : nome,
            "Level" : level,
            "Classe" : classe[randClasse],
            "Raça" : raca[randRaca]}

    return (post)





