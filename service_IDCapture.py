# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:03:46 2021

@author: Ardouz11
"""
#Import libraries and modules
import flask,os
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask import render_template,request, jsonify,send_file
import dtree_model_predict
import fuzzymatching 
import getTextFromImage
import getFace
def create_app():
  """Function that creates flask app """
  app = flask.Flask(__name__)
  Bootstrap(app)
  return app
app=create_app()
#enable debug mode
app.config["DEBUG"] = True
#add error handler
@app.errorhandler(404)
#Routing root / using get method
@app.route('/', methods=['GET'])
#render home page
def home():
    """Function that redirect to the home page"""
    return render_template("public/index.html"),404
#/gender after post method 
@app.route('/gender', methods=['POST'])
#return the gender of the input
def get_gender():
    """
    Function that predict the gender of an entered name
    """
    result_=dtree_model_predict.genderpredictor_tree(request.form.get('inputNameGender'))
    assert result_=="Male" or result_=="Female" , 'Return should be either male or female'
    response={"gender":result_}
    return jsonify(response)
#/search using post 
@app.route('/search', methods=['POST'])
#Return list of similatiries of the input
def get_listofsimilarities():
    """Function that returns list of similarities of an entered name with the default treshold"""
    #defensive coding
    list_similarities = fuzzymatching.find_similarities(request.form['inputNameSearch'])
    if len(list_similarities)>0:
        response_list={"list":list_similarities}
        return jsonify(response_list)
    else:
        return render_template("exception.html",name=request.form['inputNameSearch']),404
@app.route('/search_treshold', methods=['POST'])
#Return list of similarities with treshold
def get_listofsimilarities_treshold():
    """ The same as the precedent function ,
    it returns also the list of similarities with a treshold entered by the user"""
    list_similarities = fuzzymatching.find_similarities(request.form['inputNameSearchTreshold'],float(request.form['inputNameTreshold']))
    if len(list_similarities)>0:
        response_treshold={"list":list_similarities}
        return jsonify(response_treshold)
    else:
        return render_template("exception_treshold.html",name=request.form['inputNameSearchTreshold'],treshold=request.form['inputNameTreshold']),404
@app.route('/textExtraction', methods=['POST'])
def extract_data():
    """
    Function that extracts the data from a picture
    we save the picture uploaded to use it on the extraction 
    after we return json file that contains """
    file=request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join('SavedCards/', filename);
    file.save(filepath)
    text=getTextFromImage.get_text(filepath)
    response_data={"data":text}
    return jsonify(response_data)
@app.route('/faceExtraction', methods=['POST'])
def extract_face():
    """
    Function that recognizes the face in a picture
    we save the picture uploaded after this we return an 
    image of the face recognized
    """
    file=request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join('SavedCards/', filename);
    file.save(filepath)
    face=getFace.get_face(filepath)
    return send_file(face,mimetype='image/jpeg')
app.run(host='0.0.0.0',debug=True)