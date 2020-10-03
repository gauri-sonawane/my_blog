from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/test')
def test():
    return render_template('test_button.html')

if __name__ == '__main__':
    app.run(debug=True, port=8084)