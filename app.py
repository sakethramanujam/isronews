from flask import Flask, render_template, jsonify
from isro import news, archives

app = Flask(__name__)

@app.route("/")
def index():
    articles = news()
    return render_template("index.html",articles=articles)

@app.route("/news",methods=['GET'])
def articles():
	news_articles = news()
	archive_articles = archives()
	response = {'news':news_articles, 'archives':archive_articles}
	return jsonify(response)

if __name__=="__main__":
    app.run(debug=True)
