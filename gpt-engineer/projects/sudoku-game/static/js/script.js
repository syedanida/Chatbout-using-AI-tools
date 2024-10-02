document.addEventListener('DOMContentLoaded', () => {
    const newPuzzleButton = document.getElementById('new-puzzle');
    const solvePuzzleButton = document.getElementById('solve-puzzle');
    const validateMoveButton = document.getElementById('validate-move');

    newPuzzleButton.addEventListener('click', () => {
        fetch('/new_puzzle')
            .then(response => response.json())
            .then(data => {
                updateBoard(data.puzzle);
            });
    });

    solvePuzzleButton.addEventListener('click', () => {
        const puzzle = getPuzzle();
        fetch('/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ puzzle })
        })
        .then(response => response.json())
        .then(data => {
            updateBoard(data.solution);
        });
    });

    validateMoveButton.addEventListener('click', () => {
        const puzzle = getPuzzle();
        const row = parseInt(prompt('Enter row (0-8):'));
        const col = parseInt(prompt('Enter column (0-8):'));
        const value = parseInt(prompt('Enter value (1-9):'));

        fetch('/validate_move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ puzzle, row, col, value })
        })
        .then(response => response.json())
        .then(data => {
            if (data.valid) {
                alert('Valid move!');
            } else {
                alert('Invalid move!');
            }
        });
    });

    function getPuzzle() {
        const puzzle = [];
        const rows = document.querySelectorAll('#sudoku-board tr');
        rows.forEach(row => {
            const cells = row.querySelectorAll('td input');
            const rowData = [];
            cells.forEach(cell => {
                rowData.push(cell.value ? parseInt(cell.value) : 0);
            });
            puzzle.push(rowData);
        });
        return puzzle;
    }

    function updateBoard(puzzle) {
        const rows = document.querySelectorAll('#sudoku-board tr');
        rows.forEach((row, i) => {
            const cells = row.querySelectorAll('td input');
            cells.forEach((cell, j) => {
                cell.value = puzzle[i][j] ? puzzle[i][j] : '';
                cell.readOnly = puzzle[i][j] !== 0;
            });
        });
    }
});