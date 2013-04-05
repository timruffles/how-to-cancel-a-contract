import os
import sys
import logging
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
  host = request.host.split(":")[0]
  host = host.replace("www.","")
  if host == "how-to-cancel-a-contract.co.uk":
    return index_generic()
  elif host == "justbloodycancel.co.uk":
    return index_brand()
  else:
    return index_three_contract()

def debug_route(decorator,fn):
  if os.environ.get("DEBUG"):
       # Return the function unchanged, not decorated.
       return decorator(fn)
  return fn

@app.route('/done',methods=['GET'])
def done():
  return render_template("done.html",contract="generic",contentClass="generic",title="You're almost done!")

# for localhosting
def index_brand():
  title = "Just Bloody Cancel - cancel your contract online!"
  return render_template("brand.html",title=title,contentClass="generic")
debug_route(app.route('/brand', methods=['GET']),index_brand)

def index_generic():
  return render_template("generic.html",\
          title="How to cancel a contract",\
          contentClass="generic",\
          banner="Cancel A Contract")
debug_route(app.route('/how-to-cancel-a-contract', methods=['GET']),index_generic)


@app.route('/cancel-three-mobile-contract', methods=['GET'])
def index_three_contract():
  return index_three(title="Cancel your Three Mobile contract",\
        contentClass="three",\
        banner="How to cancel a three contract",\
        price="3.50")

def index_three(**kwargs):
  return render_template("three.html",**kwargs)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get("DEBUG"):
      app.debug = True

    stdout = logging.StreamHandler(sys.stdout)
    app.logger.addHandler(stdout)

    app.run(host='0.0.0.0', port=port)
