from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def analyze_sentiment():
    user_input = ''
    sentiment_result = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiment_result = "Positive"
        elif sentiment < 0:
            sentiment_result = "Negative"
        else:
            sentiment_result = "Neutral"
    return render_template('index.html', user_input=user_input, sentiment_result=sentiment_result)

if __name__ == '__main__':
    app.run(debug=True)