# Assignment 5 - Core Modules

**Question 1:** What’s difference between Synchronous and Asynchronous?
**Answer:**
> Synchronous code is executed line by line in the compiler. while the Asynchronous code is the part of code which can run parallel-ly alongside other codes in the system compiler. It does not block the main thread of the code and lets it execute as intended while the asynchronous code which may need to be called multiple times in the time, can be called asynchronously in the background.

**Question 2:** What are Web Apis ?
**Answer:**
> Each and every browser provides a set of Web APIs (application programming interface) which provides a lot of features and methods to perform complex operations, provide a set of data and features which we usually don't want to write code for and helps us in improving and enhancing the quality and features of our web application.
>
> The fetch function is an example of the Web API which allows the native machine to interact with the internet and request the data we need.
> DOM (Document object model) is a Web APi which allows us to manipulate the website's components easily without ever refreshing the page.
> The geo-location and local-storage api helps access the user related information such as the devices's system info, location and what data is stored on their local machine's local storage cache for that website.
> These are all in-built Web apis built into the browser system the user has (for eg Chrome or Edge) to support complex operations, and to help accessing data.

**Question 3:** Explain SetTimeOut and setInterval ?
**Answer:**
> `setTimeout` is a timing event function, which takes a callback as it's first parameter, and a number as its second parameter. This function delays the execution of callback by the amount of milliseconds passed in the second parameter. Once the delay is over, the event loop of javascript will attempt to run the callback in the main thread.
> `setInterval` is a timing event function, which is similar to `setTimeout`, except it repeats the callback after every given time-interval in milliseconds

**Question 4:** how can you handle Async code in JavaScript ?
**Answer:**
> We can handle asynchronous code by dealing with it's results in a Promise based way. Because asynchronous code will execute and only return a value in future and not immediately, it may or may not return the desired results. To handle this uncertainty, pass 2 callbacks to handle the successful result and exception result respectively.
>
> Another way to handle asynchronous code is to directly `await` it and wait for it's result to finish on the spot. There is 1 limitation which is that this can only be done inside another asynchronous function only.

**Question 5:** What are Callbacks &  Callback Hell ?
**Answer:**
> A JavaScript callback is a function which will be executed in the future after a certain operation or another function has finished it's execution. Callbacks are most commonly used to run supplementary code after some particular code has been successfully executed, for example to clean up or wrap up something like database connection.
> Callbacks can be defined on the spot when passing as a function in JavaScript.
> Promises and Higher order functions has callbacks which are always called in the future one or multiple times. For example Promises has 2 mandatory callbacks that we must define / override to write our own custom behavior and code. It also makes it easier to read the maintain the code. As we can simply chain callbacks.
> 
> Callback hell is nothing but the pattern of code where there is nested callbacks (or callbacks within callbacks). This is usually a bad way to write code and should not be done. The nested callbacks depends on their parent callbacks to be executed. Again it's a bad practice whatsoever.

**Question 6:** What are Promises & Explain Some Three Methods of Promise
**Answer:**
> A Promise is an object that is used as a placeholder for the future result of an asynchronous operation. `Fetch` function is an example of a promise. Promise was introduced in ES6 2015
> How promise works:
> Promise has 2 states, in the beginning the Promise is pending, during this time the asynchronous task is still doing its work in the background.
> Once the asynchronous task is finished executing, the promise has now SETTLED.
> There are 2 different types of settled promises, a Fulfilled promises and a Rejected promises.
> A fulfilled promise has successfully resolved and returned a value for us.
> A rejected promise means that there has been an error that occurred during the asynchronous task, and it returns us an error object with all the details specified.
> Chaining promises is a good alternative to nesting callbacks, which helps us escape callback hell.

**Question 7:** What’s async & await Keyword in JavaScript
**Answer:**
> The async and await keywords enable asynchronous, promise-based behavior to be written in a cleaner style, avoiding the need to explicitly configure promise chains.
> `async` keyword allows us to write promises-based code as if it was synchronous and it checks that we are not breaking the execution thread. It operates asynchronously via the event loop.
> `await` keyword is used to wait for the promise. It could be used within the async block only.
> Essentially, `async/await` is just simply syntactic sugar over the `.then()` method in Promises. It's much useful in case of chaining `then()` as it prevents us from doing that and gives a much more simpler way of asynchronously doing the operations.

**Question 8:** Explain Purpose of Try and Catch Block & Why do we need it?
**Answer:**
> Try-catch is the exception handling mechanism of JavaScript which allows developers to handle runtime exceptions in their JavaScript code. The `try` statement block wraps the code which will be executed but has chance to fail and throw an error. The `catch` statement block is where exception is caught and wraps the code which will be executed if an exception happens. The block also has access to the error. So we can access the error object and inspect what kind of error it was and other necessary values if need to be accessed.
> We need try-catch to handle code which is not fail-safe and may return exceptions based on it's nature. The purpose is to handle the exceptions and direct the code to do the operations necessary to do based on the exceptions.
> Example:
```js
try {
    fetch('https://www.thiswebsitedoesnotexist/')
} catch (error) {
    console.log('Fetching from website failed! What should we do now?')
}
```

**Question 9:** Explain fetch
**Answer:**
> Fetch is an Web API feature provide by Web browsers to JavaScript. Fetch is a functional method that allows you to request and fetch data from the internet or a server. Fetch is an all in one method that allows the user to modify and construct the query url with necessary parameters.
> Example is as follows:
```js
fetch("http://api.mathjs.org/v4/?expr=2*(7-3)")
.then(resp => resp.json())
.then(data => console.log(data)) // Output: 8
```

**Question 10:** How do you define an asynchronous function in JavaScript using async/await?
**Answer:**
> This is how we call an asynchronous function in JavaScript and call it.
```js
async function multiply(a, b) {
    if (b === 0) {
        throw new Error('Zero Division Error: cannot divide first number with a  0')
    }
    return a * b
}
multiply(3,4)
// Output: *Promise {<fulfilled>: 12}*
multiply(3,4).then(o => console.log(o))
// Output: 12

multiply(3,0)
.then(o => console.log(o))
.catch(e => console.log('cannot do that!'))
// Output: cannot do that!
```

