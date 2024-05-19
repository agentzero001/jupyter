var n = 50, m = 100, row, data = [], board = [], interval_ID;

button = document.createElement('button')
button.textContent = 'Start'
button.id = 'button1'

button2 = document.createElement('button')
button2.textContent = 'clear'

button3 = document.createElement('button')
button3.textContent = 'get pattern1'

button4 = document.createElement('button')
button4.textContent = 'random pattern'


set_state = function(i, j) {
    return function() {
        data[i][j] = true;
        setRow();
    }
}
    

function setRow() {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            board[i][j].style.background = (data[i][j] ? 'gray' : 'black')
        }
    }
}


function update() {
    let i, j, k, l, neighbours;

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            neighbours = 0;
            for (k = i - 1; k <= i + 1; k++) {
                for (l = j - 1; l <= j + 1; l++) {
                    if (k != i || l != j) {
                        if (board[k] && board[k][l] && board[k][l].style.background.indexOf('gray') != -1) 
                            neighbours++;
                    }
                }
            }        
            if (neighbours == 3)
                data[i][j] = true;
            else if (neighbours != 2)
                data[i][j] = false;
        }    
    }
}


function run() {
    if (button.textContent === 'Start') {
        button.textContent = 'Stop';
        interval_ID = setInterval(function() { setRow(), update() }, 200);
    }
    else {
        button.textContent = 'Start';
        clearInterval(interval_ID);
        
    }   
}


function clear() {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            data[i][j] = false; 
        }
    }
    setRow();
}

function get_pattern1() {
    mid_m = Math.floor(m / 2), mid_n =  Math.floor(n / 2)

    data[mid_n][mid_m] = true;
    data[mid_n + 1][mid_m] = true;
    data[mid_n - 1][mid_m] = true;
    data[mid_n - 1][mid_m + 1] = true;
    data[mid_n][mid_m - 1] = true;
    setRow()
}


function get_random_pattern() {

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (Math.random() < .3) 
                data[i][j] = true;
        }
    }

    setRow();

    // var list_i = [];
    // var list_j = [];
    // const getRandomIndexes = (n) =>  Math.floor(Math.random() * n - 1)

    // for (let i = 0; i <= Math.floor(m/2); i++) {
    //     list_i[i] = getRandomIndexes(n)
    //     list_j[i] = getRandomIndexes(m)
    // }

    
    // for (let z = 0; z < list_i.length; z++)
    //     data[list_i[z]][list_j[z]] = true;
}


function init () {
    char = document.createTextNode('click the cells to set initial state or get one from the buttons');

    document.body.appendChild(char)
    document.body.appendChild(button)
    document.body.appendChild(button2)
    document.body.appendChild(button3)
    document.body.appendChild(button4)

    tbody = document.getElementById('board');  
    for (let i = 0; i < n; i++) {
        row = tbody.appendChild(document.createElement('tr'));
        board[i] = [];
        data[i] = [];
        for (j = 0; j < m; j++) {
            board[i][j] = row.appendChild(document.createElement('td'));
            data[i][j] = false;
            board[i][j].addEventListener('click', set_state(i, j)) 
        }
    }

    button.addEventListener('click', run)
    button2.addEventListener('click', clear)
    button3.addEventListener('click', get_pattern1)
    button4.addEventListener('click', get_random_pattern)

}
