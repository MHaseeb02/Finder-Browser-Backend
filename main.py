from flask import jsonify,make_response,Flask,request
from stack import stack as stk
from que import Queue as qe
from tinydb import TinyDB

app = Flask(__name__)
stack = stk()
que = qe()
db = TinyDB("data.json")
dbe = TinyDB("data2.json")

@app.route("/add_history")
def add_hist():
    global stack
    request_data = request.args
    url = request_data["url"]
    print(url)
    stack.push(url)
    for i in db.all():    
        db.update({"url":stack.pop()})
    return "."
    
@app.route("/")
def main():
    stackout = stk()
    # json_obj.add({"history" :stack.mystack})
    data = list(reversed(stack.mystack))
    return make_response(jsonify({"history":data}))

@app.route("/add_favouties")
def add_fav():
    global que
    request_data = request.args
    url = request_data["url"]
    print(url)
    que.push(url)
    dbe.update({"url":que.myque})
    return "."

@app.route("/get_favouties")
def main_2():
    data = que.myque
    return make_response(jsonify({"favourites":data}))

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")