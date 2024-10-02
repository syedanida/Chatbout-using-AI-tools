document.getElementById('validate-btn').addEventListener('click', validateMove);
document.getElementById('solve-btn').addEventListener('click', solvePuzzle);
document.getElementById('new-btn').addEventListener('click', newPuzzle);

function getBoard() {
    const board = [];
    document.querySelectorAll('.sudoku-row').forEach(row => {
        const rowData = [];
        row.querySelectorAll('.sudoku-cell').forEach(cell => {
            rowData.push(cell.value ? parseInt(cell.value) : 0);
        });
        board.push(rowData);
    });
    return board;
}

function validateMove() {
    const board = getBoard();
    const row = parseInt(prompt('Enter row (0-8):'));
    const col = parseInt(prompt('Enter column (0-8):'));
    const value = parseInt(prompt('Enter value (1-9):'));

    fetch('/validate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ board, row, col, value }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.valid ? 'Valid move!' : 'Invalid move!');
    });
}

function solvePuzzle() {
    const board = getBoard();
    fetch('/solve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ board }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.solved) {
            updateBoard(data.solved);
        } else {
            alert('No solution found!');
        }
    });
}

function newPuzzle() {
    fetch('/new')
    .then(response => response.json())
    .then(data => {
        updateBoard(data.board);
    });
}

function updateBoard(board) {
    const cells = document.querySelectorAll('.sudoku-cell');
    let index = 0;
    board.forEach(row => {
        row.forEach(cell => {
            cells[index].value = cell !== 0 ? cell : '';
            index++;
        });
    });
}