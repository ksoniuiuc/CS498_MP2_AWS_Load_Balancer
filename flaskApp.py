import sys
from flask import Flask, request
app = Flask(__name__)

seed_value = 0

@app.route('/', methods=['POST','GET'])
def home():
    global seed_value
    if request.method == 'POST':
        input = request.json
        print(f'Input JSON: {input}')
        seed_value = input.get('num')
        print(f'Seed Value: {seed_value}')
        return str(seed_value)
    
    return str(seed_value)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')