# OpenAgent

For a theoretical description, see [Abstract Neural Systems](https://github.com/CarsonScott/abstract-neural-systems). This project is not a one-for-one replica of the system described in the paper, however they share many of the same concepts regarding embedded systems and autonomy.

***
## A Formal Language for Nested Automata

### Notation

The Dot notation (DO/OF/TO) is a phrase structure based on the mathematical notation of functions, where the dot phrase for f(x)y is written as: 

#### .f[x]:y

Letter symbols represent stored variables and functions. Functions require an additional piece of information that describes the inputs, where brackets with contained argument variables are placed right after the function.

### Grammar
The use of brackets is restricted, such that any instance is considered invalid unless it does immediately follows a function and has both open and close brackets, in that order. The period symbol indicates a “begin” statement, where the current statement is replaced with a blank statement. The colon indicates a “store” expression, where the calculated left value becomes the new value of the right variable.
