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
    # curl -X GET  http://127.0.0.1:5000/getTransactions

	res = ""
	for i in sortTransactionsParDate(liste_transaction):
		res += str(i[1]) + "\n"
	return res

@app.route("/addTransaction", methods=['POST'])
def add():
    # curl -X POST -d "P1=Lucas" -d "P2=Benjamin" -d "s=10" http://127.0.0.1:5000/addTransaction

    solde = int(request.form.get("s"))
    P1 = getPersonne(request.form.get("P1"))
    P2 = getPersonne(request.form.get("P2"))
    h = hashlib.sha256((P1.name + P2.name + str(solde)).encode('utf-8')).hexdigest()
    
    transaction = (P1.name, P2.name, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), solde, h)
    liste_transaction[len(liste_transaction)] = transaction

    P1.solde = int(P1.solde) - solde
    P2.solde = int(P2.solde) + solde

    P1.transactions[len(P1.transactions)] = transaction
    P2.transactions[len(P2.transactions)] = transaction

    return getTransactions()

@app.route("/chargerFichier", methods=['POST'])
def chargerFichierCSV():
    # curl -X POST -d "fichierPersonne=data.csv" -d "fichierTransaction=transactions.csv"  -d "delimiter=;" http://127.0.0.1:5000/chargerFichier

    resPersonne = chargerFichierPersonne(request.form.get("fichierPersonne"), request.form.get("delimiter"))
    resTransaction = chargerFichierTransaction(request.form.get("fichierTransaction"), request.form.get("delimiter"))

    return resPersonne + resTransaction

def chargerFichierPersonne(fichierPersonne, _delimiter):
        with open(fichierPersonne, "r") as csvfile:
                i = 0
                spamreader = csv.reader(csvfile, delimiter = _delimiter)
                for row in spamreader:
                        liste_personne.append(Personne(row[0],row[1]))
                        i += 1
        return "Nombre de personne chargée : " + str(i) + "\n"

def chargerFichierTransaction(fichierTransaction, _delimiter):
        with open(fichierTransaction, "r") as csvfile:
                i = 0
                spamreader = csv.reader(csvfile, delimiter = _delimiter)

                for row in spamreader:
                        rowP1 = row[0]
                        rowP2 = row[1]
                        splitDate = row[2].split(",")
                        date = datetime.datetime(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]), int(splitDate[3]), int(splitDate[4]), int(splitDate[5]), int(splitDate[6])).strftime("%m/%d/%Y, %H:%M:%S")
                        s = int(row[3])
                        h = hashlib.sha256((rowP1 + rowP2 + str(s)).encode('utf-8')).hexdigest()

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
    # curl -X GET -d "nom=Benjamin"  http://127.0.0.1:5000/getPersonne

    return str(getPersonne(request.form.get("nom")))

@app.route("/getSoldePersonne", methods=['GET'])
def getSoldePersonne():
    # curl -X GET -d "nom=Benjamin"  http://127.0.0.1:5000/getSoldePersonne
    
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

