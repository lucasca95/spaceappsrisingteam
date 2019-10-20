from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method=='GET'):
        #Dar index.html
        return render_template('index.html')
    else:
        f_pantalla=request.form['f_pantalla']
        #Si venimos del index ir a pantalla 1
        if(f_pantalla == 'index'):
            return render_template('pantalla1.html')
        if(f_pantalla == 'pantalla1')>
            return render_template('pantalla2.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5555)