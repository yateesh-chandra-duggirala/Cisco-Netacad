/** Exercise 2: 
  * Use the debugger to understand why the final result logged is equal to zero 
  * when on each iteration of for, a loop value of the variable result increases. 
  * Use Watch to track the changes in the selected variables.*/

let counter = 0; 
let maxValue = 10; 
let result = 1; 
 
debugger; 
for (counter = 0; counter < maxValue; counter++) { 
    console.log(result); 
    result *= maxValue - counter - 1; 
} 
 
console.log("Final result: ", result);

/**
 * 1. Open Developer Tools: Open your browser's developer tools or debugging environment.
 * 2. Set Breakpoint: Navigate to the line with debugger; and set a breakpoint there. 
 *      This will pause the code execution when it reaches that point.
 * 3. Run the Code: Execute the code. It will pause at the breakpoint, and you'll be able to inspect variables 
 *      and track their changes.
 * 4. Inspect Initial Values: At the breakpoint, inspect the initial values of the variables:
        counter: Should be 0.
        maxValue: Should be 10.
        result: Should be 1.
 * 5. Start Loop Execution: Resume execution by clicking the "Play" button or the "Continue" 
        option in the debugging toolbar. The code will now enter the loop.
 * 6. Watch Variables: While the code is paused inside the loop, use the debugging tools to add watches for the variables counter and result. 
        This will allow you to track their values as the loop progresses.
 * 7. Step Through the Loop: Use the debugging controls (step into, step over, etc.) 
        to step through each iteration of the loop. Pay attention to how result changes with each iteration.
 * 8. Observe Result Changes: As you step through the loop, observe how the value of result changes. 
        You'll notice that it starts increasing initially but then decreases and eventually becomes zero.
 * 9. Analyze Multiplication: Pay close attention to the expression where result is updated (result *= maxValue - counter - 1;). 
        Analyze how the values of maxValue, counter, and the expression (maxValue - counter - 1) affect the value of result.
 * 10. Final Result: Once the loop completes, observe the final value of result. It will be zero.
 */