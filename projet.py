from flask import Flask, request
import datetime
from personne import *
import sys
import csv
import hashlib

app = Flask(__name__)

liste_transaction = {}
liste_personne = []

@app.route("/")
def hello_world():
	return "Hello, world!"

@app.route("/getTransactions", methods=['GET'])
def getTransactions():
    """
        Renvoie la liste des transactions

        :return: liste des transactions
    """
    # curl -X GET  http://127.0.0.1:5000/getTransactions

    res = ""
    for i in sortTransactionsParDate(liste_transaction):
        res += str(i[1]) + "\n"
    return res + verifierTransaction()

@app.route("/addTransaction", methods=['POST'])
def add():
    """
        Ajoute une transaction

        :param P1: nom de la personne qui donne
        :param P2: nom de la personne qui reçoit
        :param s: solde de la transaction
        
        :return: liste des transactions
    """
    # curl -X POST -d "P1=Lucas" -d "P2=Benjamin" -d "s=10" http://127.0.0.1:5000/addTransaction

    solde = int(request.form.get("s"))
    P1 = getPersonne(request.form.get("P1"))
    P2 = getPersonne(request.form.get("P2"))
    date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    h = hashlib.sha256((P1.name + P2.name + str(solde) + date).encode('utf-8')).hexdigest()
    
    transaction = (P1.name, P2.name, date, solde, h)
    liste_transaction[len(liste_transaction)] = transaction

    P1.solde = int(P1.solde) - solde
    P2.solde = int(P2.solde) + solde

    P1.transactions[len(P1.transactions)] = transaction
    P2.transactions[len(P2.transactions)] = transaction

    return getTransactions()

@app.route("/chargerFichier", methods=['POST'])
def chargerFichierCSV():
    """
        Charge les fichiers csv

        :param fichierPersonne: nom du fichier csv des personnes
        :param fichierTransaction: nom du fichier csv des transactions
        :param delimiter: délimiteur des fichiers csv

        :return: Le nombre de personne et de transaction chargée
    """
    # curl -X POST -d "fichierPersonne=data.csv" -d "fichierTransaction=transactions.csv"  -d "delimiter=;" http://127.0.0.1:5000/chargerFichier

    resPersonne = chargerFichierPersonne(request.form.get("fichierPersonne"), request.form.get("delimiter"))
    resTransaction = chargerFichierTransaction(request.form.get("fichierTransaction"), request.form.get("delimiter"))

    return resPersonne + resTransaction

def chargerFichierPersonne(fichierPersonne, _delimiter):
    """
        Charge le fichier csv des personnes

        :param fichierPersonne: nom du fichier csv des personnes
        :param delimiter: délimiteur des fichiers csv

        :return: Le nombre de personne chargée
    """
    with open(fichierPersonne, "r") as csvfile:
        i = 0
        spamreader = csv.reader(csvfile, delimiter = _delimiter)
        for row in spamreader:
            liste_personne.append(Personne(row[0],row[1]))
            i += 1
    return "Nombre de personne chargée : " + str(i) + "\n"

def chargerFichierTransaction(fichierTransaction, _delimiter):
    """
        Charge le fichier csv des transactions

        :param fichierTransaction: nom du fichier csv des transactions

        :return: Le nombre de transaction chargée
    """
    with open(fichierTransaction, "r") as csvfile:
            i = 0
            spamreader = csv.reader(csvfile, delimiter = _delimiter)

            for row in spamreader:
                rowP1 = row[0]
                rowP2 = row[1]
                splitDate = row[2].split(",")
                date = datetime.datetime(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]), int(splitDate[3]), int(splitDate[4]), int(splitDate[5]), int(splitDate[6])).strftime("%m/%d/%Y, %H:%M:%S")
                s = int(row[3])
                h = hashlib.sha256((rowP1 + rowP2 + str(s) + date).encode('utf-8')).hexdigest()

                transaction = (rowP1, rowP2, date, s, h)
                liste_transaction[len(liste_transaction)] = transaction
			
                P1 = getPersonne(rowP1)
                P2 = getPersonne(rowP2)

                P1.solde = int(P1.solde) - s 
                P2.solde = int(P2.solde) + s
			
                P1.transactions[len(P1.transactions)] = transaction
                P2.transactions[len(P2.transactions)] = transaction

                i += 1
			
    return "Nombre de transaction chargée : " + str(i) + "\n"

@app.route("/getPersonne", methods=['GET'])
def getDataPersonne():
    """
        Récupère les données d'une personne

        :param nom: nom de la personne

        :return: les données de la personne (nom, solde, transactions)
    """
    # curl -X GET -d "nom=Benjamin"  http://127.0.0.1:5000/getPersonne

    return str(getPersonne(request.form.get("nom")))

@app.route("/getSoldePersonne", methods=['GET'])
def getSoldePersonne():
    """
        Récupère le solde d'une personne

        :param nom: nom de la personne

        :return: le solde de la personne
    """
    # curl -X GET -d "nom=Benjamin"  http://127.0.0.1:5000/getSoldePersonne

    return str(getPersonne(request.form.get("nom")).solde)

@app.route("/verifierTransaction", methods=['GET'])
def verifierTransaction():
    """
        Vérifie les transactions

        :return: les transactions non valides
    """
    # curl -X GET http://127.0.0.1:5000/verifierTransaction

    res = ""

    for i in liste_transaction:
        transaction = liste_transaction[i]

        P1 = getPersonne(transaction[0])
        P2 = getPersonne(transaction[1])

        date = transaction[2]

        h = hashlib.sha256((P1.name + P2.name + str(transaction[3]) + date).encode('utf-8')).hexdigest()

        if h != transaction[4]:
            res += str(transaction) + " : " + "Transaction non valide !" + "\n"

        if res == "":
            res = "Aucune transaction non valide ! \n"
    return res

def sortTransactionsParDate(transactions):
    """
        Trie les transactions par date

        :param transactions: les transactions

        :return: les transactions triées par date
    """
    return sorted(transactions.items(), key=lambda x: x[1][2])

def getPersonne(nom):
    """
        Récupère une personne

        :param nom: nom de la personne

        :return: la personne
    """
    for personne in liste_personne:
        if personne.name == nom:
            return personne
    return None

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)

