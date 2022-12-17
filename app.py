#!.locenv/bin/python
from src.funtasks import Fibonacci
from src.rqtasker import rqclient
import random
from flask import Flask, jsonify, request
import subprocess

rqc = rqclient()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify("Hello, World!")

@app.route("/fibocalc", methods=["POST"])
def fibocalc():
    cargo = request.get_json()
    num = int(cargo["n"])
    jobn = rqc.filler.enqueue(
        Fibonacci, kwargs={"n": num},
        job_timeout=60*30)
    return jsonify({"id": jobn.id})

@app.route("/randomfibocalc", methods=["GET"])
def randomfibocalc():
    num = random.randint(13,44)
    jobn = rqc.filler.enqueue(
        Fibonacci, kwargs={"n": num},
        job_timeout=60*30)
    return jsonify({"id": jobn.id, "num_input": num})

@app.route("/checktaskid/<task_id>", methods=["GET"])
def checktaskid(task_id):
    res = rqc.checktaskresult(task_id)
    if res.result is None:
        return jsonify({"status": "PENDING", "result": None})
    else:
        return jsonify({"status": "FINISHED", "result": res.result})

if __name__=="__main__":
    subprocess.Popen("./worker.py")
    app.run(debug=True)