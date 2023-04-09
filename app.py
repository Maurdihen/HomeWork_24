import os

from flask import Flask, request, abort, jsonify, Response
from utils import some_functions
from typing import Optional, Union, List

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    cmd1: Optional[str] = request.args.get("cmd1")
    val1: Optional[str] = request.args.get('val1')
    cmd2: Optional[str] = request.args.get('cmd2')
    val2: Optional[str] = request.args.get('val2')
    file_name: Optional[str] = request.args.get('file_name')
    if not cmd1 and val1 and file_name:
        abort(400, "Недостаточно команд для корректной работы программы")
    file_path: str = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400, "File not found")
    with open(file_path, "r") as file:
        print(file)
        result: Union[list, str] = some_functions(cmd1, val1, file)
        if cmd2 and val2:
            result = some_functions(cmd2, val2, result)
    return jsonify(result)


if __name__ == "__main__":
    app.run()