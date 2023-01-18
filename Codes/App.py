from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return 'Hello Rattanon!'

@app.route('/Id')
def Id():
    return '654272111'

@app.route('/name')
def name():
    return 'Rattanon Krittiyawan'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

if _name_ == '_main_':
    app.run(debug=True)