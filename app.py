from flask import Flask,render_template,session,request
import json,csv
app=Flask(__name__)
app.secret_key="tentacolo_tantact"
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/watch')
def watch():
    filename=open("data/watch.json","r")
    products=json.load(filename)
    return render_template("watch.html",watches=products)

@app.route('/watch/<int:id>')
def watchetail(id):
      filename=open('data\watch.json',"r")
      products=json.load(filename)
      product=None
      
      for eachproduct in products:
           if eachproduct["id"]==id:
                product=eachproduct
                break
      return render_template("watchdetail.html",watch=product)

@app.route("/cart/<int:id>")
def add_and_show_car(id):
     cart=session.get("cart",[])
     cart.append(id)
     session["cart"]=cart
     filename=open('data\watch.json',"r")
     products=json.load(filename)
     cart_items=[]
     for cid in cart:
          for p in products:
               if p["id"] == cid:
                    cart_items.append(p)
     return render_template("cart.html",items=cart_items)

@app.route("/checkout",methods=["POST","GET"])
def tantocolotantac():
     filename=open("data\watch.json","r")
     products=json.load(filename)
     cart_ids=session.get("cart",[])
     cart_items=[]
     for i in cart_ids:
          for p in products:
               if p["id"]==i:
                    cart_items.append(p)
                    break
     print(cart_items)
     totalprice=0



     if request.method=="POST":
          customer=request.form.get("name")

          files=open("order.json","w")
          writer=json.load(files)

          for item in cart_items:
               writer.dump([
                    customer,
                    item["id"],
                    item["name"],
                    item["price"],
               ],files)
          session["cart"]=[]

          

          return render_template("thankyou.html",total=totalprice)
          
     






     for item in cart_items:
          totalprice=totalprice+item["price"]


     
     return render_template('checkout.html',total=totalprice)

@app.route("/thank")
def thank():
     return render_template("thankyou.html")


if __name__=="__main__":
    app.run(debug=True)