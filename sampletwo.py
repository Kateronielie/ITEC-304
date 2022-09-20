from flask import Flask, request

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    
    state = request.args.get('state')
    nationality = request.args['nationality']
    language = request.args.get('language')
    
    return '''<h1 style="color: #b32d56;">The State is : {}</h1>
              <h1 style="color: #b32d56;">The Nationality is: {}</h1>
              <h1 style="color: #b32d56;">The Language is : {}</h1>'''.format(state, nationality, language)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
