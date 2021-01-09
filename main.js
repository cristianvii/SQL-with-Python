/* Minnimum Javascript needed to learn react

Vanilla JS
- Recursion : aproach of solution, a recursive way to get solution
- Closures
- Loops
- Condtionals

- Package managers
- Yarn
- Webpack
- Babel

- Ajax(Http requests)
- Promises(concepts)

- Async/Awake(ES7)

const, lets, var

Scopes
 - Global 
- Lexical

ES6
- Classes
- Imports/Exports
- Arrow Functions
- Spread operator

Functional methods(See MDN - Mozilla Developer Network)
- .map
- .filter
- .reduce

Destructuring 
- example = import React { Component, Fragment } from 'react';

*/

/* RECURSION */

var add = function (n) {
    if(n<=0){
    return 0
    } else{
    return n + add(n-1);
}

console.log( add(3));

































