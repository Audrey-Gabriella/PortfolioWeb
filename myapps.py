from flask import Flask, render_template, request
from datetime import datetime


webapp = Flask(__name__)

@webapp.route('/') #Route Default 

def index():
	message = render_template("index.html")
	return message

@webapp.route('/audrey')
def audrey():
	return "<h2>Welcome back!!</h2>"

@webapp.route('/page')
def page():
	main_page = render_template("budi.html")
	return main_page

@webapp.route("/headline")
def headline_page():
	headline = "Audrey Gabriella"
	page = render_template("headline.html", headline=headline)
	return page

@webapp.route("/isitmybirthday")
def my_page():
	today = datetime.now()
	status = (today.month == 1 and today.day == 20)
	if status:
		ans = "YES"
	else:
		ans = "NO"
	page = render_template("myday.html", ans=ans)
	return page

@webapp.route("/isitnewyear")
def new_year():
	today = datetime.now()
	newYear = (today.month == 1 and today.day == 1)
	page = render_template("hny.html", newYear=newYear)
	return page

@webapp.route("/menu")
def food():
	meals =['sate', 'sayur asin', 'soto', 'pempek', 'model']
	page = render_template("eat.html", meals=meals)
	return page

@webapp.route('/<string:name>')
def greetings(name):
	msg = render_template("greetings.html", name=name)
	return msg

@webapp.route('/moreinfo')
def info():
	page = render_template("info.html")
	return page

"""
@webapp.route('/layout')
def blog():
	come = render_template("layout.html")
	return come
"""
@webapp.route('/form')
def form():
	return render_template("form.html")
	

@webapp.route('/result', methods = ['GET','POST'])
def result():
	if request.method == 'GET':
		go = render_template('warning.html')
		return go
	else:
		name = request.form.get('name')
		page = render_template("result.html", name=name)
		return page

@webapp.route('/html')
def html():
	page = render_template('khtml/01_hello.html')
	return page

@webapp.route('/css')
def css():
	page = render_template('khtml/02_css.html')
	return page

@webapp.route('/about')
def about():
	page = render_template('about.html')
	return page

@webapp.route('/division')
def division():
	page = render_template('division.html')
	return page

@webapp.route('/lcss')
def lcss():
	page = render_template('css/css-14-grid.html')
	return page

@webapp.route('/portofolio')
def potray():
	page = render_template('portofolio/potray.html')
	return page

