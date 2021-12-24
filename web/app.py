import config

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def index(ip_addr = None):
    return render_template('index.html', ip_addr_send = config.IP_ADDR + 'send', ip_addr_get = config.IP_ADDR + 'get')


@app.route('/send', methods=['POST'])
def send():
    value = request.form['value']

    with open('data.txt', 'w') as file:
        file.write(value)

    return jsonify(result = "success")


@app.route('/get', methods=['POST'])
def get():
    value = ''

    with open('data.txt', 'r') as file:
        for line in file:
            value = line

    return jsonify(result = value)


if __name__ == '__main__':
    app.run(debug=True)