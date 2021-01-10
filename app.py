import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
import pickle
app = Flask(__name__)
model = pickle.load(open('crop.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():

    #For rendering results on HTML GUI
    
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    if(prediction[0]==0):
        c="Adzuki Beans"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==1):
        c="Black gram"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==2):
        c="Chickpea"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==3):
        c="Coconut"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==4):
        c="Coffee"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==5):
        c="Cotton"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==6):
        c="Ground Nut"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==7):
        c="Jute"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==8):
        c="Kidney Beans"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==9):
        c="Lentil"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==10):
        c="Moth Beans"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==11):
        c="Mung Bean"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==12):
        c="Peas"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==13):
        c="Pigeon Peas"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==14):
        c="Rubber"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==15):
        c="Sugarcane"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==16):
        c="Tea"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==17):
        c="tobacco"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==18):
        c="apple"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==19):
        c="banana"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==20):
        c="grapes"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==21):
        c="maize"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==22):
        c="mango"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==23):
        c="millet"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==24):
        c="muskmelon"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==25):
        c="orange"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==26):
        c="papaya"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==27):
        c="pomogranate"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==28):
        c="rice"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==29):
        c="watermelon"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    elif(prediction[0]==30):
        c="wheat"
        return render_template('index.html', prediction_text='Crop field is {}'.format(c))
    
if __name__ == "__main__":
    app.run(debug = True)
    
