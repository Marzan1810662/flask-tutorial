from flask import Flask, request,make_response,render_template,redirect, url_for

app =Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myValue = 'Marzan'
    myResult = 10 + 20
    myList = [10,20,30,40,50]
    return render_template('index.html', myValue = myValue, myResult = myResult, myList = myList)

@app.route('/other')
def other():
    value = 'Hello World!'
    return render_template('other.html',value = value)

# creating our own template filter
@app.template_filter('reverse_string')
def reverse(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times= 2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(s)])

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

# @app.route('/')
# def index():
#     return "<h1>Hello World</h1>"

@app.route('/index2', methods = ['GET', 'POST'])
def index2():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'marzan' and password == 'abc':
            return 'success'
        else: return 'failure'


@app.route('/hello', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'You have made a get request', 200
    elif request.method == 'POST':
        return 'You have a POST request'
    else: return "If methods are fixed you will probably never see this BUT Hello There"

@app.route('/response-crafting')
def response_crafting():
    response = make_response('the is the response')
    response.status_code = 00
    response.headers['content-type'] = 'plain/text'
    return response

# Dynamic URLs
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1+number2}'
    
# URL Parameters
# to handle url parameters I need to import the request object from flask
@app.route('/handle_url_params')
def handle_params():
    # return str(request.args)
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args['name']
        return f'{greeting}, {name}'
    else:
        return "Some parameters are missing"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000, debug = True)