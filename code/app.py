from flask import Flask, render_template 

app = Flask(__name__)

####################################################

#Твой код

@app.route('/')
@app.route('/home')
def download():
	return render_template('index.html')

####################################################

if __name__ == "__main__":
  app.run(debug=True)