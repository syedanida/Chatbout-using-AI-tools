from flask import Flask, render_template, request, jsonify
from sudoku_generator import generate_puzzle, validate_move, solve_puzzle

app = Flask(__name__)

@app.route('/')
def index():
    puzzle = generate_puzzle()
    return render_template('index.html', puzzle=puzzle)

@app.route('/validate_move', methods=['POST'])
def validate():
    data = request.json
    row = data['row']
    col = data['col']
    value = data['value']
    puzzle = data['puzzle']
    is_valid = validate_move(puzzle, row, col, value)
    return jsonify({'valid': is_valid})

@app.route('/solve', methods=['POST'])
def solve():
    puzzle = request.json['puzzle']
    solution = solve_puzzle(puzzle)
    return jsonify({'solution': solution})

@app.route('/new_puzzle', methods=['GET'])
def new_puzzle():
    puzzle = generate_puzzle()
    return jsonify({'puzzle': puzzle})

if __name__ == '__main__':
    app.run(debug=True)