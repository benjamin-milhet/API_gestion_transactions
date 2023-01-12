
from flask import Flask, request




app = Flask(__name__)
@app.route("/")
def hello_world():
	return "Hello,world!"


mon_dictionnaire={0:"voiture",1:"moto",2:"velo"}
@app.get("/dico")
def get_list():
	res =""
	for i in mon_dictionnaire.items():
		res+=i[1]+"\n"
	return res
#curl http://127.0.0.1:5000/dico

@app.post("/add")
def add():
	mon_dictionnaire[len(mon_dictionnaire)] = request.form["name"]		

	return  str(mon_dictionnaire)
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
