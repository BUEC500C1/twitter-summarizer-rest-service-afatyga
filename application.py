import sys
from flask import Flask, render_template, request, send_file
import os
import zipfile

application = Flask(__name__)

@application.route('/') #creates the flask html route
def root():
    return render_template('main.html')
@application.route('/', methods=['POST']) #creates the flask html route
def post():
    text1 = request.form['user1']
    text2 = request.form['user2'] 
    text3 = request.form['user3']
    text4 = request.form['user4'] 

    args2 = "rm *.png"
    os.system(args2)
    args3 = "rm Vids/*"
    os.system(args3)

    args6 = "python3 hw3queue.py "+ str(text1) + " " + str(text2) + " " + str(text3) + " " + str(text4)
    os.system(args6)
    zipFolder = zipfile.ZipFile('vids.zip','w', zipfile.ZIP_DEFLATED)
    for root, directs, files in os.walk('Vids/'):
        for f in files:
            zipFolder.write('Vids/' + str(f))
    zipFolder.close()
    return send_file('vids.zip', mimetype ='zip', attachment_filename = 'vids.zip', as_attachment=True)

#    return render_template('videos.html')



if __name__ == '__main__':

    application.run(host = '0.0.0.0', port = 8080)