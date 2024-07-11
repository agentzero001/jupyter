function speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
}

let whiteRabbit = {type: "white", speak};

let hungryRabbit = {type: "hungry", speak};

// whiteRabbit.speak("Oh my fur and whisters");

// hungryRabbit.speak("Got any carrots")

// speak.call(whiteRabbit, "Hurry");

let finder = {
    find(array) {
        return array.some(v => v == this.value)

    },
    value: 5
};

//console.log(finder.find([4, 5]));

// let empty = {};
// console.log(empty.toString());

let protoRabbit = {speak}
let blackRabbit = Object.create(protoRabbit);
blackRabbit.type = 'black';

//blackRabbit.speak('I am fear and darkness');

function Rabbit(type, color) {
    return {type: type, color: color, speak}
}
let rabbit1 = Rabbit('hungry', 'black')


function makeRabbit(type) {
    let rabbit = Object.create(protoRabbit);
    rabbit.type = type;
    return rabbit;
}


class Rabbit2 {
    constructor(type) {
        this.type = type;
    }
    speak2(line) {
        console.log(`The ${this.type} rabbit says '${line}'`);
    }
}

let rabbit2 = new Rabbit2('white')

rabbit2.speak2('Oh my fur and whiskers')


function ArchaicRabbit(type) {
    this.type = type;
}

ArchaicRabbit.prototype.speak3 = function(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
};

let oldSchoolRabbit = new ArchaicRabbit('old school')

// It is important to understand the distinction between the way a prototype is
// accociated with a constructor (through its prototype property) and the way
// objects have a prototype (which can be found with Object.getPrototypeOf).
// The actual prototype of a constructor is Function.prototype since constructors 
// are functions. The constructor functions's prototype property holds the prototype
// used for instances created through it.

console.log(Object.getPrototypeOf(Rabbit2) == Function.prototype)
console.log(Object.getPrototypeOf(rabbit2) == Rabbit2.prototype)


class Particle {
    speed = 0;
    constructor(position) {
        this.position = position;
    }
}

let particle = new Particle((1,2))


let object = new class { getWord() {return 'hello';}};


//private property
class SecretiveObject {
    #getSecret() {
        return 'I ate all the plums';
    }
    interrogate() {
        let shallISayIt = this.#getSecret();
        return shallISayIt
    }
}


class RandomSource {
    #max;
    constructor(max) {
        this.#max = max;
    }
    getNumber() {
        return Math.floor(Math.random() * this.#max);
    }
}

//Overriding derived properties

Rabbit2.prototype.teeth = 'small'

rabbit2.teeth = 'long, sharp and bloody'
