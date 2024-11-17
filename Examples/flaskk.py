'''
from flask import Flask, request
app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    try:
        number1 = float(args.get("number1"))
        number2 = float(args.get("number2"))
        total_sum = number1+number2
        return str(total_sum)
    except (TypeError, ValueError):
        return "Invalid input: Please provide valid numbers for number1 and number2"

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000, debug=True)
'''
from flask import Flask, request

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    total_sum = number1+number2

    response = {
        "number1" : number1,
        "number2" : number2,
        "total_sum" : total_sum
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)