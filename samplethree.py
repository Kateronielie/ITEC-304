from flask import Flask, request

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    
    state = request.args.get('state')
    nationality = request.args['nationality']
    language = request.args.get('language')
    
    return '''<h1 style="color: #b32d56;">The State is : {}</h1>
              <br>
              <h1 style="color: #b32d56;">The Nationality is: {}</h1>
              <br>
              <h1 style="color: #b32d56;">The Language is : {}</h1>'''.format(state, nationality, language)

@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        state = request.form.get('state')
        nationality = request.form['nationality']
        return'<h1>The state is {}. The nationality is {}. </h1>'.format(state, nationality)

    return'''<form method="POST">
    State <input type="text" name="state" style="color: #b32d56;">
    <br>
    Nationality <input type="text" name="nationality" style="color: #b32d56;">
    <br>
    <input type="submit" style="color: #b32d56;">
    </form>'''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
