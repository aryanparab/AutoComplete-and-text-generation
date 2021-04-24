from flask import Flask , request, render_template 
from  imports import textgen 
import requests

app = Flask(__name__)

@app.route('/',methods=['GET', "POST"])
def main():
	context = ""
	text = ''
	number = 0
	if request.method == 'POST':
		text = request.form['text']
		number = int(request.form['number'])
		context = textgen.generate_text_seq(text,number)

	return render_template('home.html',context = [context,text , number])

if __name__ == '__main__':
	app.run(debug=True)