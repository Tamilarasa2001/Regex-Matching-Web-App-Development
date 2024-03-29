from flask import Flask, render_template, request

import re # importing the regular expression module

#creating an instance of flask application
app = Flask(__name__)

#define route for home page
@app.route('/')
def index():
    return render_template('index.html')

# define route to handle form submission for regex matching
@app.route('/match', methods=['POST'])
def match():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']

    # performimg regex matching
    matches = re.findall(regex_pattern, test_string, re.IGNORECASE)
    
    # to count the number of matches found
    num_matches = len(matches)
    matched_words = matches

    return render_template('matches.html',test_string=test_string, regex_pattern=regex_pattern, num_matches=num_matches, matched_words=matches)

# to run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)