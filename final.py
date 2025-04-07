from flask import Flask

app = Flask(__name__)

@app.route('/')
def add_numbers():
    num1 = 450
    num2 = 740
    result = num1 + num2
    return f"The sum of {num1} and {num2} is {result}."

if __name__ == '__main__':
    app.run(debug=True)
