import json

from flask import Flask, jsonify, make_response
import people_repository as pr

app = Flask(__name__)


@app.route('/get-data', methods=['GET'])
def get_data():
    people = pr.find_people_by_n_zachet_data()
    json_response = json.dumps([ob.__dict__ for ob in people])
    response = make_response(json_response)
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
