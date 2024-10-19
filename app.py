from flask import Flask, render_template, request
import pickle
import pandas as pd

model = pickle.load(open('model code/model.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    diagnosis = request.form['diagnosis']
    radius = request.form['radius']
    texture = request.form['texture']
    perimeter = request.form['perimeter']
    area = request.form['area']
    smoothness = request.form['smoothness']
    compactness = request.form['compactness']
    concavity = request.form['concavity']
    concave_points = request.form['concave_points']
    symmetry = request.form['symmetry']
    fractal_dimension = request.form['fractal_dimension']
     
    data = pd.DataFrame(
        {
            'diagnosis': [diagnosis],
            'radius': [radius],
            'texture': [texture],
            'perimeter': [perimeter],
            'area': [area],
            'smoothness': [smoothness],
            'compactness': [compactness],
            'concavity': [concavity],
            'concave points': [concave_points],
            'symmetry': [symmetry],
            'fractal_dimension': [fractal_dimension],
        }
    )
    
    predict = model.predict(data)
    
    if predict[0] == 'M':
        final_prediction = 'The prediction indicates a malignant tumor (M). It is important to consult a healthcare professional for further evaluation and possible treatment options. Early intervention can significantly improve outcomes.'

    else:
        final_prediction = "The prediction indicates a benign tumor (B). This is a reassuring result, but it is still important to follow up with your healthcare provider for regular monitoring and to discuss any concerns you may have."
    
    return render_template('index.html', prediction=final_prediction)


if __name__ == '__main__':
    app.run(debug=False)

