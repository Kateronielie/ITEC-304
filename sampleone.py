from flask import Flask, request

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    
    nationality = request.args.get('nationality')
    return '<h1 style="color: #b32d56;">The nationality is : {}</h1>'.format(nationality)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
