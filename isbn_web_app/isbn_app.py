# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:50:28 2021

@author: micha
"""

from flask import Flask, render_template



print(__name__)
app = Flask(__name__)

@app.route("/") # Start Page
def start_page():
    return"<p>Hello World! Hope you are good, Sir!!!</p>"
 
    
 
@app.route("/info") # Information Page
def show_info():
    return "<p>Some information</p>"
 
@app.route("/isbn/<isbn>")    
def isbn_display(isbn):
    return render_template("isbn_display.html")