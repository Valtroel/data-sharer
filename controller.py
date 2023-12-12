import json
from flask import Flask, jsonify, make_response, request
import people_repository as pr
import logging as log

app = Flask(__name__)

log.basicConfig(
    encoding='utf8',
    level=log.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    handlers=[log.FileHandler('logs/logs.log')]
)


@app.route('/get-data', methods=['GET'])
def get_data():
    people = pr.find_people_by_n_zachet_data()
    json_response = json.dumps([ob.__dict__ for ob in people], default=str)
    response = make_response(json_response)
    response.content_type = "application/json"
    response.content_encoding = "utf-8"
    return response


@app.route('/get-student-data', methods=['GET'])
def get_student_data():
    file_path = request.args.get("filePath")
    log.debug(f"[controller(/get-student-data)] Recieved query file path:{file_path}")
    people = pr.find_people_by_n_zachet_data([file_path])
    json_response = json.dumps([ob.__dict__ for ob in people], default=str)
    response = make_response(json_response)
    response.content_type = "application/json"
    response.content_encoding = "utf-8"
    return response


@app.route("/n-spec-values", methods=['GET'])
def get_n_spec_values():
    n_spec_values = pr.find_all_n_specializ()
    json_response = json.dumps(n_spec_values)
    response = make_response(json_response)
    response.content_type = "application/json"
    response.content_encoding = "utf-8"
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
