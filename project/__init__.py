from flask import Flask,jsonify

app = Flask(__name__)
# set config
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'success',
        'message': 'Pong'
    })


    