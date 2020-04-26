import datetime
import logging
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from google.cloud import storage
from pip._internal.cli.status_codes import SUCCESS
from _ast import If
ALLOWED_EXTENSIONS = {'xml'}
app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])  
def upload():
     if request.method == 'POST':
        
         uploaded_file = request.files.get('file')
         if allowed_file(uploaded_file.filename):
             
          gcs = storage.Client(project="golden-joy-270306")
          bucket = gcs.get_bucket("cc-a2-0426")
          blob = bucket.blob(uploaded_file.filename)
        #   blob.upload_from_string(
        #   uploaded_file.read(),
        #   content_type=uploaded_file.content_type
        #   )
          blob.upload_from_file(uploaded_file)
         
         else:
          return render_template('index.html',messg=" File EXTENSIONS is not Allowed!!")
   
       
     return render_template('index.html',messg="UPLOAD SUCCESSFUL")


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500



@app.route('/')
def hello():
    return render_template('index.html',messg="Hello!,you can upload now!")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
















if __name__ == '__main__':

    app.run(host='127.0.0.1', port=6061, debug=True)

