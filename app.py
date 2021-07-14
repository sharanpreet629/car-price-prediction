#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('regression_model.pkl', 'rb'))



#User defined Functions
@app.route("/", methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predictions', methods=['POST'])
def predict():
    carName = request.form['car']
    caryear = int(request.form['year'])
    carprice = float(request.form['price'])
    carkm = int(request.form['km'])
    carowners = int(request.form['Owners'])
    transmission= request.form["transmission"]
    Stype = request.form['Stype']
    ftype = request.form['type']

    if transmission=='Manual':
        transmission=1
    else:
        transmission=0

    if ftype=="CNG":
        Diesel=0
        Petrol=0
    elif ftype=="Petrol":
        Diesel=0
        Petrol=1
    else:
        Diesel=1
        Petrol=0

    if Stype=='Dealer':
        Stype=1
    else:
        Stype=0

    predictions = loadedModel.predict([[carprice,carkm,carowners,caryear,Diesel,Petrol,Stype,transmission]])[0]
    price = round(predictions,2)

    return render_template('index.html', Predict = price)


#Main function
if __name__== "__main__":
    app.run(debug=True)