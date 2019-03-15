from flask import Flask, render_template,redirect,url_for
app = Flask(__name__)
import payment,hello_world,based_on_low_price,Add_cart_increment,list_link,based_on_name,signup

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/task')
def index_val():
	payment.payment()
	return redirect(url_for('index'))

@app.route('/hell')
def hello():
	hello_world.hello()
	return redirect(url_for('index'))

@app.route('/based_on_price')
def base_low_price():
	based_on_low_price.low_price()
	return redirect(url_for('index'))

@app.route('/add_cart_inc')
def add_cart():
	Add_cart_increment.add_cart_inc()
	return redirect(url_for('index'))

@app.route('/link')
def link():
	lis = list_link.link()
	return str(lis)

@app.route('/name')
def name():
	lis = based_on_name.name()
	return redirect(url_for('index'))

@app.route('/register')
def register():
	signup.register()
	return redirect(url_for('index'))



if __name__ == '__main__':
   app.run(debug = True,port='8001')