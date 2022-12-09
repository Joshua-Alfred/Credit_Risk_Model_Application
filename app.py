from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    interestRate = float_features[-1]
    float_features.pop()
    features=[np.array(float_features)]
    predictions=model.predict(features)

    

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    predictions=model.predict([np.array(list(data.values()))])

    return jsonify(predictions[0])


if __name__=="__main__":
	app.run(debug=True)