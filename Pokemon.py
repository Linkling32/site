from random import *

class Pokemon:
    def __init__(self,nom,types,points_de_vie,attaque,defense,attaque_speciale,defense_speciale,vitesse,capacites):
        self.no = nom
        self.ty = types
        self.pv = points_de_vie
        self.at = attaque
        self.de = defense
        self.ats = attaque_speciale
        self.des = defense_speciale
        self.vi = vitesse
        self.ca = capacites


class Pokemon_en_combat:
    def __init__(self,nom,types,points_de_vie,attaque,defense,attaque_speciale,defense_speciale,vitesse,capacites):
        self.no = nom
        self.ty = types
        self.pv = points_de_vie
        self.at = attaque
        self.de = defense
        self.ats = attaque_speciale
        self.des = defense_speciale
        self.vi = vitesse
        self.ca = capacites


class Capacite:
    def __init__(self,nom,type,puissance,precision,categorie,PP,effet,peut_echouer):
        self.no = nom
        self.ty = type
        self.pu = puissance
        self.pr = precision
        self.ca = categorie
        self.pp = PP
        self.ef = effet
        self.pe = peut_echouer


Normal = "Normal"
Plante = "Plante"
Feu = "Feu"
Eau = "Eau"
Poison = "Poison"
Electrique = "Electrique"
Insecte = "Insecte"
Combat = "Combat"
Acier = "Acier"
Sol = "Sol"
Roche = "Roche"
Vol = "Vol"
Glace = "Glace"
Psy = "Psy"
Fee = "Fee"
Spectre = "Spectre"
Tenebres = "Tenebres"
Dragon = "Dragon"

Physique = "Physique"
Special = "Special"
Statut = "Statut"

Brulure = "Brulure"
Empoisonnement = "Empoisonnement"
Paralysie = "Paralysie"
Gele = "Gele"
Protection = "Protection"
Vampirisme = "Vampirisme"
Contrecoup = "Contrecoup"
Piege = "Piege"
Critique = "Critique"
BonusAtk = "BonusAtk"
BonusDef = "BonusDef"
BonusAtkSpe = "BonusAtkSpe"
BonusDefSpe = "BonusDefSpe"
BonusVit = "BonusVit"
BonusPre = "BonusPre"
MalusAtk = "MalusAtk"
MalusDef = "MalusDef"
MalusAtkSpe = "MalusAtkSpe"
MalusDefSpe = "MalusDefSpe"
MalusVit = "MalusVit"
MalusPre = "MalusPre"
Non = "Non"


Tempete_florale = Capacite("Tempete florale",Plante,90,100,Physique,15,"","")
Croissance = Capacite("Croissance",Normal,0,100,Statut,20,(BonusAtk,1,BonusAtkSpe,1),Non)
Vampigraine = Capacite("Vampigraine",Plante,0,90,Statut,10,(Vampirisme,-1,0.125),"")
Belier = Capacite("Belier",Normal,90,85,Physique,20,Contrecoup,"")
Lame_d_air = Capacite("Lame d'air",Vol,75,95,Special,15,"","")
Lance_flammes = Capacite("Lance flammes",Feu,90,100,Special,15,(Brulure,10),"")
Draco_souffle = Capacite("Draco souffle",Dragon,60,100,Special,20,(Paralysie,30),"")
Tranche = Capacite("Tranche",Normal,70,100,Physique,20,(Critique,125),"")
Hydrocanon = Capacite("Hydrocanon",Eau,110,80,Special,5,"","")
Lumicanon = Capacite("Lumicanon",Acier,80,100,Special,10,"","")
Exuviation = Capacite("Exuviation",Normal,0,100,Statut,15,(BonusAtk,2,BonusAtkSpe,2,BonusVit,2,MalusDef,1,MalusDefSpe,1),Non)
Abri = Capacite("Abri",Normal,0,100,Statut,10,Protection,Non)


Florizarre = Pokemon("Florizarre",("Plante","Poison"),80,82,83,100,100,80,(Tempete_florale,Croissance,Vampigraine,Belier))
Dracaufeu = Pokemon("Dracaufeu",("Feu","Vol"),78,84,78,109,85,100,(Lame_d_air,Lance_flammes,Draco_souffle,Tranche))
Tortank = Pokemon("Tortank","Eau",79,83,100,85,108,78,(Hydrocanon,Lumicanon,Exuviation,Abri))


Liste_pokemon = {"Florizarre":Florizarre,"Dracaufeu":Dracaufeu,"Tortank":Tortank}

Table_modifications_générale = (0.25,0.29,0.33,0.4,0.5,0.67,1,1.5,2,2.5,3,3.5,4)
Table_modifications_reste = (0.33,0.38,0.43,0.5,0.6,0.75,1,1.33,1.67,2,2.33,2.67,3)


def combat():
    Pokemon_temp = None
    Numero_joueur = 1
    for i in range(2):
        while not isinstance(Pokemon_temp,Pokemon):
            Pokemon_temp = input("Pokemon du joueur " + str(Numero_joueur) + ": ")
            if Pokemon_temp in Liste_pokemon:
                Pokemon_temp = Liste_pokemon[Pokemon_temp]
            else:
                print("Il n'existe pas, n'a pas été implémenté ou a été mal écrit")
        if Numero_joueur == 1:
            Pokemon1 = Pokemon_en_combat(Pokemon_temp.no,Pokemon_temp.ty,Pokemon_temp.pv,Pokemon_temp.at,Pokemon_temp.de,Pokemon_temp.ats,Pokemon_temp.des,Pokemon_temp.vi,Pokemon_temp.ca)
        else:
            Pokemon2 = Pokemon_en_combat(Pokemon_temp.no,Pokemon_temp.ty,Pokemon_temp.pv,Pokemon_temp.at,Pokemon_temp.de,Pokemon_temp.ats,Pokemon_temp.des,Pokemon_temp.vi,Pokemon_temp.ca)
        Pokemon_temp = None
        Numero_joueur = 2
    print("")


    if randint(0,1) == 0:
        Pokemon_attaquant = Pokemon1
        Pokemon_defenseur = Pokemon2
    else:
        Pokemon_attaquant = Pokemon2
        Pokemon_defenseur = Pokemon1


    while Pokemon1.pv > 0 and Pokemon2.pv > 0:
        for i in range(4):
            print(Pokemon_attaquant.ca[i].no + " [" + str(i+1) + "]")
        print("")
        Capacite_choisie = None
        Termine = True
        while Termine:
            print(Pokemon_defenseur.pv)
            Capacite_choisie = int(input("Choisissez la capacité: "))
            if 1 <= Capacite_choisie <= 4:
                if Pokemon_attaquant.ca[Capacite_choisie-1].ca == Statut:
                    print("Nope")
                else:
                    Coefficient_multiplicateur = 1
                    Taux_critique = 417
                    if Pokemon_attaquant.ca[Capacite_choisie-1].ca == Physique:
                        Statistique_attaque = Pokemon_attaquant.at
                        Statistique_defense = Pokemon_defenseur.de
                    else:
                        Statistique_attaque = Pokemon_attaquant.ats
                        Statistique_defense = Pokemon_defenseur.des
                    if Pokemon_attaquant.ca[Capacite_choisie-1].ty in Pokemon_attaquant.ty:
                        Coefficient_multiplicateur *= 1.5
                    for i in Pokemon_attaquant.ca[Capacite_choisie-1].ef:
                        if i == Critique:
                            Taux_critique = Pokemon_attaquant.ca[Capacite_choisie-1].ef[i+1]
                    if randint(1,1000) < Taux_critique:
                        Coefficient_multiplicateur *= 1.5
                    Pokemon_defenseur.pv -= (22*Statistique_attaque*Pokemon_attaquant.ca[Capacite_choisie-1].pu/Statistique_defense/50+2)*Coefficient_multiplicateur
                print(Pokemon_defenseur.pv)
                Termine = False
                        

            else:
                print("Veuillez écrire un entier de 1 à 4")

combat()