## Generators :
- A Python generator is a piece of specialized code able to produce a series of values and to control the iteration processes.
- This is the reason why generators are also called as Iterators.
- Consider the following piece of code :
    ```
    for i in range(5):
        print(i)
    ```
  Here, The range() is a generator and again an iterator

- The difference is A function returns one, well-defined value - It may be the result of a more or less complex evaluation of, something like a polynomial, and is invoked once - only once.
- A generator returns a series of values and in general is invoked more than once.
- In example, the range() generator is invoked six times, providing five subsequent values from zero to four and finally signaling that the series is complete.
- The Iterator protocol is a way in which an object should behave to confirm to the rules imposed by the context of the for and in statements. 
- An object conforming to the iterator protocol is called an iterator.

- An iterator must provide 2 methods :
    a. __iter__() which should return the object itself and which is invoked once
    b. __next__() which is intended to return the next value of the desired series - It will be invoked by the for / in statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception.
- The process goes like this :
    a. The iterator object is instantiated first.
    b. Python invokes the __iter__() method to get access to the actual iterator
    c. The __next__() method will be invoking n+1 times. The result woould run for n invocations by terminating the iteration at n+1 th time.

## yield statement :
- The iterator protocol is not particularly difficult to understand and use, but it is also indisputable that the protocol is rather inconvenient.
- The Main disadvantage is the need to save the state of the iteration between subsequent __iter__  invocations.
- For example, the Fib iterator is forced to precisely store the place in which the last invocation has been stopped. This makes the code larger and less comprehensible.
- Hence, Python offers a much more effective, convenient and elegant way of writing iterators.
- This concept is fundamentally based on a very specific and powerful mechanism provided by the yield keyword.
- yield and return statement have one essential difference.

- For loop has no chance to finish the first execution as the return will break it irrevocably.
- Invoking the function will not change anything - the for loop will start from scratch and will be broken immediately.
- We can say that such a function is not able to save and restore its state between subsequent invocations.
- This also means that a function like this cannot be used as a generator.
- Meanwhile we can add yied, instead of return.
- This little amendment turns the function into a generator, and executing the yield statement has some very interesting effects.
- First of all, it provides the value of the expression specific after the yield keyword, just like return but does not lose the state of the function. 
- All the variables' values are frozen and wait for the next invocation, when the execution is resumed
- There is one important limitation; such a function should not be invoked explicitly as - in fact - it is not a function anymore; It is a generator object.
- The invocation will return the object's identifier, not the series we expect from the generator.
- Due to the same reasons, the previous function may only be invoked explicitly and must not be used as a generator.

a. List Comprehensions : Generators may also be used within the list comprehensions.
b. list() function : The list() function can transform a series of subsequent generator invocations into real list.
c. in operator : Moreover the context created by the in operator allows you to generate an operator.

## Conditional Expression :
- This is a way of selecting one of two different values based on the result of a boolean expression. 
- Just Something `exp1 if condition else exp2`
- This is not a conditional expression, This is not even instruction.. this is a operator.
- Two main words should come into mind while looking into code : Compactness and Elegance.
- Just only one change can turn any list comprehension into a generator.
- [] Closed brackets make a Comprehension and () Parentheses make a generator.
- We can work on the lists and generators without creating.
- However, List is automatically created but Generator is not automatically created.

## Lambda Function :
- The Lambda Function is used to simplify the code, to make it clearer and easier to understand.
- A lambda function is a function without name (Anonymous function).
- It is declared as :
    `lamdba parameters : expression`
- This clause returns the value of the expression when taking into account the current value of the current lambda argument.
- From lambda-function example, It is clear that :
    a. The first Lambda is an anonymous parameterless function that always returns 2. As we have assigned it to a variable named two, we can say that the function is not anonymous anymore and we can use that name to invoke it.
    b. The second one is a one parametered function that returns the value of its squared argument.
    c. The third lambda takes two parameters and returns the value of the first one raised to the power of the second one. The name of the variable which carries the lambda speaks for itself.
- This is how code is made shorter, clearer and more legible

## Lambdas and the map() function :
- map() function is declared as map(function, list).
- The second map() argument may be an entity that can be iterated  (eg. Tuple or just a generator)
- map() can accept more than two arguments.
- The map() function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent result.
- You can use the resulting iterator in a loop or convert it into a list using the list() function.

## Lambdas and filter() function :
- This function expects same type of arguments as of map() function
- It filters the second argument while being guided by directions flowing from the function specified as the first argument.

## Closures :
- A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore.
- Consider the example outer.py
- inner() may be invoked only from within outer().
- We can say that inner() is outer()'s private tool. No other part of the code can access it.
- The inner() function is parameterless, so we have to invoke it without arguments.
- Now It is fully possible to declare a closure equipped with an arbitrary number of parameters.
- Closure not only makes use of the frozen environment, but it also can modify its behavior by using values taken from the outside.
- This example shows one more interesting circumstance - you can create as many closures as you want using one and the same piece of code. This is done with a function named make_closure().