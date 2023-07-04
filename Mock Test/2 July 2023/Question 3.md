### 3. Explain what is execution context in detail with diagram
-----

**Answer**
> **Execution Context** is an environment in which JavaScript's code is executed. It stores all the necessary information for that code to be executed smoothly.
> In the JavaScript's runtime engine, there is a Call Stack will which execute each of these execution contexts of JavaScript code one by one on a FIFO basis. The call stack is the place where execution contexts get stacked on top of each other, to keep track of where we are in the execution.
> For each JavaScript code file, there can be exactly only one Global Execution Context, which is created for code that is not inside any function.
> For each function in JavaScript, a separate execution context is created for it to be run inside call stack.
> Inside an Execution context has the following things:
> - Variable environment
> - Scope chain
> - The `this` keyword