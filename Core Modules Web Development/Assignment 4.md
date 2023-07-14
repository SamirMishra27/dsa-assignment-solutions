# Assignment 4 - Core Modules

**Question 1:** Explain Hoisting in JavaScript
**Answer:**
> Hoisting in JavaScript is the process of hoisting the mutable variable declarations to the top of the javascript file. Before some JavaScript code is executed in the browser, the browser will first scan for all let, var and const declarations and put them at the very top of the javascript executable code. For var declarations, the variables are hoisted and then assigned ‘undefined’ before actual initialization. Meanwhile the let and const declarations are not assigned a default value but remain in a temporal dead zone till they are finally initialized their actual value.

**Question 2:** Explain Temporal Dead Zone?
**Answer:**
> Temporal dead zone is that 'brief' period of time in JavaScript's code execution when all variables which were assigned with `let` and `const` declarations remain in an 'unaccessible state'. If we try to access these variables during this period it will throw a Reference error exception, as if the variable was never declared.

**Question 3:** Difference between var & let?
**Answer:**
> data types declared with `var` keyword are function scoped in JavaScript, which means that once it is declared with `var`, it can be accessed anywhere in the environment. However `let` & `const` declarations are Block scoped. They are only accessible in the environment variable in which they are created and in their child scopes.
> Additionally, var declarations are hoisted in JS, so they will be bought up at the top of the scope and assigned a default value i.e, `undefined`, but same is not the case with `let` and `const` as they are hoisted technically but not initialized with a value.
> `var` declarations and `let` declarations are mutable, it can be changed in the runtime. `const` declarations are immutable and are supposed to remain constants during it's execution lifetime.

**Question 4:** What are the major features introduced in ECMAScript 6?
**Answer:**
> The following key features were introduced in ECMAScript 6 / 2015 version of JavaScript. It's also considered the 2nd major version of JavaScript.
> - The `let` and `const` keywords (two new ways to safely declare a variable)
> - Anonymous (Arrow Functions)
> - The array spread operator (...) and function's rest operator.
> - `for (elem of iterable)` for/of looping technique.
> - Two new datatype objects - `Map` object and `Set` object.
> - Classes
> - Promises
> - Default parameters for functions.
> - New methods for Arrays and Strings.
> - New Math, Global and Number methods.
> - JavaScript modules and module standardization.

**Question 5:** What is the difference between let and const ?
**Answer:**
> `let` declaration is mutable, it can be changed in the runtime. `const` declarations are immutable and are supposed to remain constants during it's execution lifetime.

**Question 6:** What is template literals in ES6 and how do you use them?
**Answer:**
> Template literals is a string interpolation method to directly insert variables and values inside a string without doing concatenation. It makes reading and constructing a String literal in JavaScript more easier.
> Example: ```const message = `hello world! my name is ${name}` ```
> Example: ``` `Today's temperature in ${city.name} is around ${temperature} celsius` ```
> To insert a variable directly inside a string, make write ${} and put the values inside the curly brackets. Ternary operations are also supported.

**Question 7:** What’s difference between map & forEach?
**Answer:**
> Difference between .map() and .forEach():
> - `map()` is an array method that loops over all the elements on an array, applies a callback function that was passed to it and returns the returned values in a new array.
> - `forEach()` only applies the callback function that was passed to it to each and every element of the array and returns nothing.

**Question 8:** How can you destructure objects and arrays in ES6?
**Answer:**
> Example:
```js
const batsman = {
    runs: 24,
    balls: 20,
    wickets: 4,
    hattrick: true
}
const { runs, balls, wickets, hattrick } = batsman
```
> You need to specify the exact attribute name in which the value is being stored. You can also change the variable name and assign it to a different one using this syntax. (Assign within destructuring)
> ``` const { batsmanRuns = runs } = batsman ```

> Arrays destructuring example:
```js
const [a, b] = [10, 20]
const [state, setState] = useState()
const [a, b] = [1, 2, 3, 4, 5] // a = 1, b = 2
const [a, b, c, d, e, f, g, h] = [1, 2, 3, 4, 5] // a = 1, b = 2, c = 3, d = 4, e = 5, f = undefined, g = undefined, h = undefined
```
> Arrays destructuring works pretty much the same as object destructuring.
> If fewer than variables are assigned then it only unpacks the first xy amount of values from the array

**Question 9:** How can you define default parameter values in ES6 functions?
**Answer:**
```js
function getCurrentState(player, second_innings = false) {
    if (second_innings)
        return `${player.runs} (${player.balls}) runs.`
    else
        return `${player.wickets} - ${player.runsGiven} (${player.oversBowled}) spell.`
}
getCurrentState(player) // 35 (23) runs.
getCurrentState(player, second_innings = true) // 6 - 34 (7.0) spell.
```

**Question 10:** What is the purpose of the spread operator (...) in ES6?
**Answer:**
> The spread (...) operator is to smoothly destructure the elements of an array and return all of their values. It can be used to easily construct new arrays from existing arrays or to extend an array.
> Example:
```js
const a = [1, 2, 3, 4, 5, 6]
const b = [7, 8, 9, 10]
const c = [...a, ...b]
```
> Putting ... before the array name will return an unpacked version of the datatype to be consumed. It does not returns another iterable. To be clear.
