import json
from json import dumps
import datetime

from flask import Flask, jsonify
import people_repository as pr

app = Flask(__name__)


def dumps(obj, default=lambda obj: obj.__dict__):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    return json.dumps(obj, default=default)


@app.route('/get_data', methods=['GET'])
def get_data():
    return dumps(pr.find_people_by_n_zachet_data())


if __name__ == '__main__':
    app.run(debug=True, port=5000)
