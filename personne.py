
import csv 
class Personne:

    name = ""
    solde = 0
    def __init__(self, _name, _solde):
        self.name = _name
        self.solde = _solde

    def __str__(self):
        return "name: "+self.name+" solde: "+str(self.solde)
    
def listePersonne():
    liste_personne = []
   
    with open('data.csv' , "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            liste_personne.append(Personne(row[0],row[1]))
    return liste_personne

def printListePersonne(liste_personne):
    for p in liste_personne:
        print(p)
