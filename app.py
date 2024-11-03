from flask import Flask, request,make_response,render_template

app =Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myValue = 'Marzan'
    myResult = 10 + 20
    myList = [10,20,30,40,50]
    return render_template('index.html', myValue = myValue, myResult = myResult, myList = myList)

@app.route('/other')
def other():
    return render_template('other.html')

# @app.route('/')
# def index():
#     return "<h1>Hello World</h1>"


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