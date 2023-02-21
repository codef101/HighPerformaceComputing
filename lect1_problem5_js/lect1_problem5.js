const math = require('mathjs')

console.log("==================================================================== " )
console.log("                           Slide 12                                  " )
console.log("==================================================================== " )

var arr1 = Array.from({length: 10000}, () => Math.floor(Math.random() * 100));;
var arr2 = Array.from({length: 10000}, () => Math.floor(Math.random() * 100));;
let sum = 0;

var startTime = performance.now()
for (let i=0; i<arr1.length; i++) {
    sum += arr1[i] * arr2[i];
}
var endTime = performance.now()
var for_loop_time = endTime - startTime;
console.log("For Loop Sum: " + sum)


startTime = performance.now()
sum = math.dot(arr1, arr2)
var endTime = performance.now()
var dot_product_time = endTime - startTime;
console.log("Dot Product Sum: " + sum)

console.log("For Loop Time: " + for_loop_time)
console.log("Dot Product Time: " + dot_product_time)
console.log("Speed Up: " + (for_loop_time/dot_product_time))

console.log("==================================================================== " )
console.log("                           Slide 13                                  " )
console.log("==================================================================== " )


let n = 10000;
narr = Array.from({length: n}, () => Math.floor(Math.random() * 4));
var a = [narr, narr];
var x = narr;
let i, j, k;

var startTime = performance.now()
for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
        x[i][j] = 0;
        for (k = 0; k < n; k++)
            x[i][j] += a[i][k] * x[k][j];
    }
}
endTime = performance.now()

for_loop_time = endTime - startTime;
console.log("For Loop Cross Mul: " + x)

startTime = performance.now()
x = math.multiply(a, x) 
endTime = performance.now()
dot_product_time = endTime - startTime;

console.log("Math Library Cross Mul: " + x)

console.log("For Loop Time: " + for_loop_time)
console.log("Cross Mul Loop Time: " + dot_product_time)
console.log("Speed Up: " + (for_loop_time/dot_product_time))