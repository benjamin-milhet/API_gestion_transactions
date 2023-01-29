from flask import Flask, request
import datetime
from personne import *
import sys
import csv

app = Flask(__name__)

liste_transaction = {0: ("jean", "pierre", datetime.datetime.now(), 100)}
liste_personne = []

@app.route("/")
def hello_world():
	return "Hello, world!"

@app.route("/getTransactions", methods=['GET'])
def getTransactions():
	res = ""
	for i in sortTransactionsParDate(liste_transaction):
		res += str(i[1]) + "\n"
	return res

@app.route("/addTransaction", methods=['POST'])
def add():
    solde = int(request.form.get("s"))
    transaction = (request.form.get("P1"), request.form.get("P2"), datetime.datetime.now(), solde)
    liste_transaction[len(liste_transaction)] = transaction

    P1 = getPersonne(request.form.get("P1"))
    P2 = getPersonne(request.form.get("P2"))

    P1.solde = int(P1.solde) - solde
    P2.solde = int(P2.solde) + solde

    P1.transactions[len(P1.transactions)] = transaction
    P2.transactions[len(P2.transactions)] = transaction

    return getTransactions()

@app.route("/chargerFichier", methods=['POST'])
def chargerFichierCSV():
    resPersonne = chargerFichierPersonne(request.form.get("fichierPersonne"), request.form.get("delimiter"))
    resTransaction = chargerFichierTransaction(request.form.get("fichierTransaction"), request.form.get("delimiter"))

    return resPersonne + resTransaction

def chargerFichierPersonne(fichierPersonne, _delimiter):
        with open(fichierPersonne, "r") as csvfile:
                spamreader = csv.reader(csvfile, delimiter = _delimiter)
                for row in spamreader:
                        liste_personne.append(Personne(row[0],row[1]))
        return "Nombre de personne chargée : " + str(len(spamreader)) + "\n"

def chargerFichierTransaction(fichierTransaction, _delimiter):
        with open(fichierTransaction, "r") as csvfile:
                spamreader = csv.reader(csvfile, delimiter = _delimiter)

                for row in spamreader:
			rowP1 = row[0]
			rowP2 = row[1]
			date = row[2]
			s = int(row[3])
			transaction = (rowP1, rowP2, date, s)
                        liste_transaction[len(liste_transaction)] = transaction
			
			P1 = getPersonne(rowP1)
		        P2 = getPersonne(rowP2)

		        P1.solde = int(P1.solde) - s
		        P2.solde = int(P2.solde) + s

		        P1.transactions[len(P1.transactions)] = transaction
                        P2.transactions[len(P2.transactions)] = transaction
			
        return "Nombre de transaction chargée : " + str(len(spamreader)) + "\n"

@app.route("/getPersonne", methods=['GET'])
def getDataPersonne():
    return str(getPersonne(request.form.get("nom")))

@app.route("/getSoldePersonne", methods=['GET'])
def getSoldePersonne():
    return str(getPersonne(request.form.get("nom")).solde)

def sortTransactionsParDate(transactions):
    return sorted(transactions.items(), key=lambda x: x[1][2])

def getPersonne(nom):
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

