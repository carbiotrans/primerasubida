"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask,render_template,url_for
from FlaskWebProject1 import app
import os
import webbrowser
import dash
import dash_core_components as dcc
import dash_html_components as html
import json
import pygal
import time
import pymysql



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# prueba de uso de mysql
@app.route('/mysql_test2')
def mysql_test():
       conexion = pymysql.connect("80.34.8.193", "NOSOTROS", "NO1133tros", "qeo557")
       cursor = conexion.cursor()
       sql = "SELECT * from facturas order by fecha desc limit 10"
       cursor.execute(sql)
       results = cursor.fetchall()
       #field_names = [i[0] for i in cursor.description]
       #get_data = [xx for xx in cursor]
       return render_template('mysql_test2.html',results=results)
       conexion.close
#fin de prueba de mysql
@app.route("/bar")

# -------------------------------------------
# Charting route which displays the bar chart
# -------------------------------------------
@app.route("/bar")
def bar():
    with open('FlaskWebProject1/templates/bar.json','r') as bar_file:
        data = json.load(bar_file)
    chart = pygal.Bar()
    mark_list = [x['mark'] for x in data]
    chart.add('Annual Mark List',mark_list)
    chart.x_labels = [x['year'] for x in data]
    chart.render_to_file('FlaskWebProject1/static/images/bar_chart.svg')
    img_url = 'FlaskWebProject1/static/images/bar_chart.svg?cache=' + str(time.time())
    return render_template('app_chart.html',image_url = img_url)
# fin de charting
