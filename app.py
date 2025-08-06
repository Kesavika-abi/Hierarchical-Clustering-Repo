from flask import Flask, render_template, request
import os
import pandas as pd
from model import perform_clustering
from utils import create_cluster_plot

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    file = request.files['file']
    clusters = int(request.form['clusters'])

    if not file:
        return "No file uploaded", 400

    df = pd.read_csv(file)
    clustered_df, labels = perform_clustering(df, clusters)
    plot_path = create_cluster_plot(clustered_df, labels)

    return render_template('result.html', tables=[clustered_df.to_html(classes='data', index=False)],
                           plot_url=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
