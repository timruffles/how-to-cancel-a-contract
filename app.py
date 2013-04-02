import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
  host = request.host.split(":")[1]
  if host == "how-to-cancel-a-contract.co.uk":
    return index_generic()
  else:
    return index_three()

@app.route('/done',methods=['GET'])
def done():
  return render_template("done.html")

def index_generic():
  return render_template("generic.html",title="How to cancel a contract")

def index_three():
  return render_template("three.html",title="How to cancel a contract")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get("DEBUG"):
      app.debug = True
    app.run(host='0.0.0.0', port=port)
