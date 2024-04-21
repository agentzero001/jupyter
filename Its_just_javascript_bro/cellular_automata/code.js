var n = 100, row, data = [], cells, interval_ID;

button = document.createElement('button')
button.textContent = 'Start'
button.id = 'button1'

button2 = document.createElement('button')
button2.textContent = 'clear'

set_state = function(i) {
    return function() {
        data[i] = true;
        setRow();
    }
}
    

function setRow() {
    for (let i = 0; i < n; i++)
    cells[i].style.background = (data[i] ? 'gray' : 'black')
}


function update() {
    var left, right;

    for (let i = 0; i < n; i++) {
        left = (cells [i-1] && cells[i-1].style.background.indexOf('gray') != -1);
        right = (cells [i+1] && cells[i+1].style.background.indexOf('gray') != -1);
        data[i] = ((left && !right) || (!left && right));
    }
}

function run() {
    if (button.textContent === 'Start') { //gotta be extra-sure these are equal at runtime
        button.textContent = 'Stop';
        interval_ID = setInterval(function() { setRow(), update() }, 200);
    }
    else {
        button.textContent = 'Start';
        clearInterval(interval_ID);
        
    }   
}


function clear() {
    for (let i = 0; i < n; i++)
        data[i] = false; 
        setRow();
    }
     

function init () {
    char = document.createTextNode('click the cells to set initial state');

    document.body.appendChild(char)
    document.body.appendChild(button)
    document.body.appendChild(button2)

    row = document.getElementById('cells') 
    cells = row.getElementsByTagName('td') 
    for (let i = 0; i < n; i++) {
        row.appendChild(document.createElement('td'))
        cells[i].addEventListener('click', set_state(i));
    }

    button.addEventListener('click', run)
    button2.addEventListener('click', clear)
}