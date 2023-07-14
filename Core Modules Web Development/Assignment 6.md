# Assignment 6 - Core Modules

**Question 1:** What’s Constructor And Its Purpose?
**Answer:**
> The `constructor()` method is an in-built method of JavaScript class objects that initializes the object with additional attributes and values and it's modification.
> Every time a JavaScript object is initiated, this `constructor` method is ran first. When we are making blue prints of objects, we can override this method to take additional parameters and arguments so that we can access it withing the constructor method and assign it as values to the object's attributes.
> Example:
```js
class Player {
    constructor (user, channel) {
        this.user = user
        this.channel = channel
        this.name = user.name
        this.id = user.id
        // Player stats
        this.runs = 0
        this.balls = 0
        this.wickets = 0
        this.hattricks = 0
    }
}

```
> As you can see, instead of initializing these attributes outside the object, the constructor method takes care of it's implementation within the class only. So we do not need to worry about it.

**Question 2:** Explain This Keyword and Its Purpose?
**Answer:**
> `this` keyword is a special keyword that gives access to it's current environment's prototype. In simpler words for example, in the case of an object, the `this` keyword will give you a reference to the object so that you can access it's attributes, methods and values.
> The purpose of this keyword is to access the data and attributes from within an object or environment when we are writing some code within it.

**Question 3:** What’s Call Apply Bind Method & Difference Between them
**Answer:**
> - `function.call()` will call the function with the provided ‘this’ context. It will replace the default ‘this’ object of that function. Further arguments are passed separated by comma (,)
> - `function.apply()` is exactly the same as .call() except it takes an ‘Array of arguments’ instead of arguments being passed individually.
> - `function.bind()` serves the exact purpose as call() does but does not call the function immediately, instead it returns the copy of the function with the new replaced ‘this’ context. Then that variable can be later called to execute the function with new this context.


**Question 4:** Explain OOPS ? (Object oriented programming)
**Answer:**
> The Object Oriented Programming is a programming paradigm & practice in which developers write and organize their code inside 'Objects'. Objects are like items which have different qualities and their own methods and implementations. The Purpose of OOPS is to write efficient and purposeful code, so that we do not repeat our code in multiple places.
> Additionally, one of the great key features of this paradigm is that it hides implementations and encapsulates the internal logical code within it so that outsiders code cannot access it unless explicitly specified.

**Question 5:** Whats Abstraction and Its Purpose?
**Answer:**
> Abstraction is a practice in which we break down the code into more generic & 'abstract' parts. The generic part of code can be used and inherited multiple times by other code and so it need to be written every time. If there is a need to change or override those values we can always do so in the code that inherited it.
> Purpose of abstraction is to allow reuse of code and also this allows multiple classes and objects to access same code, attributes and methods from multiple places, preventing unnecessary workaround to be done.
> Example:
```js
class PlayerABC {   // ABC => Abstract base class
    name;
    id;
    winner;
}

class Batsman extends PlayerABC {
    runs
    balls
    century
}

class Bowler extends PlayerABC {
    wickets;
    runs_given;
    balls_given;
    hattricks;
}
```

**Question 6:** Whats Polymorphism and Purpose of it?
**Answer:**
> Polymorphism is a concept in programming languages. Polymorphism means *Many forms*. Poly means many and morphism means transforming into different forms.
> In the simplest of language, Polymorphism in JavaScript refers to the practice when we inherit a class and override one of it's defined methods to have it's own implementation. It's one of the key features of OOPS as it aims to write less and more efficient code.
> Example:
```js
class Game {
    startGame() {
        'Starting a game!'
    }
}

class Ludo extends Game {
    startGame() {
        'Starting a ludo game! Getting all 4 players on board.'
    }
}
```
> As you can see we rewrote it's defined method so that it can have it's own custom implementation. If we still want the parent class' method to execute, while doing our own implementation. We can use `super()` method to call the parent method's code, then we can write the custom code based on the purpose of the class.

**Question 7:** Whats Inheritance and Purpose of it?
**Answer:**
> Inheritance is inheriting all the properties and attributes of a parent class to its child class.
> Example:
```js
class A {
    name = 'A'
    age = 20
}

class B extends A {
    hobbies = 'Programming'
    language = 'JavaScript'
}

testA = A()
testB = B()
console.log(
    testA.name,
    testA.age,
    testA.hobbies,
    testA.language
)
// A 20 undefined undefined
console.log(
    testB.name,
    testB.age,
    testB.hobbies,
    testB.language
)
// A 20 Programming JavaScript
```

**Question 8:** Whats Encapsulation and Purpose of it ?
**Answer:**
> Encapsulation is the process fo hiding code implementation and their values behind a class or a function. It 'encapsulates' the code and variables so that others cannot have unwanted access to it. The purpose of doing encapsulation is to prevent modification and access to certain variables and values directly and instead provide methods to access and modify them so that we can restrict the scope and nature of modification to strict types.
> Although JavaScript objects do allow some level of encapsulating values, they are not 100% secure.
> Functional programming in JavaScript provides safe way to encapsulate and modify private methods.
```js
function Game() {
    let _started = true
    let _score = 0

    function addScore(s) {
        _score += s
    }
    function endGame() {
        _started = false
    }
    function started() { return _started }
    function score() { return _score }
    return {started, score, addScore, endGame}
}

let {started, score, addScore, endGame} = Game()
// game = Game()

console.log(started)
console.log(score)
// true and 0

addScore()
endGame(50)
console.log(started)
console.log(score)
// false and 50

Game()._score
Game()._started
// Both return undefined
```

**Question 9:** Explain Class in JavaScript?
**Answer:**


**Question 10:** What’s Super Keyword & What it does?
**Answer:**

