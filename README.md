# OpenAgent

## A Formal Language for Nested Automata

### Notation

Dot (DO-OF-TO) notation is a phrase structure that refulects mathematical functions, such that f(x) -> y is written as: 

#### .f[x]:y

The letter symbols represent stored variables and functions. Functions require an additional piece of information that describes the inputs, where brackets with contained argument variables are placed right after the function.

### Grammar
The use of brackets is restricted, such that any instance is considered invalid unless it does immediately follows a function and has both open and close brackets, in that order. The period symbol indicates a “begin” statement, where the current statement is replaced with a blank statement. The colon indicates a “store” expression, where the calculated left value becomes the new value of the right variable.
