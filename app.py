from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>Decribe yourself</h2>
            <form action="/greet">
                Your name <input type='text' name='username' style="color: #b32d56;"> is <br>
                Your characteristic <input type='text' name='char' style="color: #b32d56;" ><br>
                <br>
                <input type='submit' value='Continue' style="color: #b32d56;" >
            </form>
            </body></html>"""

@app.route('/intro')
def intro():
    username = request.args.get('username')
    char = request.args['char']
  
    return """
        <html><body>
            <h2 style="color: #b32d56;">Hello, {0} is {1}! •ᴗ• </h2>
            
        </html></body>""".format(username,  char)


