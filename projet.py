from flask import Flask, request
import datetime
from personne import*
import sys

app = Flask(__name__)



@app.route("/")
def hello_world():
	return "Hello,world!"




liste_transaction={0: ("jean", "pierre", datetime.date.today(),100)}
@app.get("/listetransaction")
def get_list():
	res =""
	for i in liste_transaction.items():
		res+= str(i[1])+"\n"
	return res


@app.post("/add")
def add():
	liste_transaction[len(liste_transaction)] = (request.form["P1"],request.form["P2"],request.form["date"],request.form["s"])

	return  get_list()


if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [OK]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported arguments are : check_syntax")
			exit(1)	
	app.run(debug=True)

'''
#curl http://127.0.0.1:5000/dico


#curl -X POST -d  "name=tricycle" http://127.0.0.1:5000/add
@app.post("/del")
def delete():
	del mon_dictionnaire[int(request.form["id"])]
	return str(mon_dictionnaire)
#curl -X POST -d  "id=2" http://127.0.0.1:5000/del

@app.post("/modif")
def modif():
	mon_dictionnaire[int(request.form["id"])] = request.form["name"]		
	return str(mon_dictionnaire)
# curl -X POST -d  "id=2" -d "name=truc" http://127.0.0.1:5000/modif
if __name__ == '__main__':
    app.run()
'''