# OpenAgent

## A Formal Language for Nested Automata

### Notation

Dot (DO-OF-TO) notation is a phrase structure that refulects mathematical functions, such that f(x) -> y is written as: 

#### .f[x]:y

The letter symbols represent stored variables and functions. Functions require an additional piece of information that describes the inputs, where brackets with contained argument variables are placed right after the function.

### Grammar
The use of brackets is restricted, such that all brackets are considered invalid except for those that immediately follows functions.

Periods define the start of new statements, as well as the end of previous statements. Colons indicate the storage of values, where the left side contains a variable and the right side contains a value, and the result of the colon is that the variable takes on the value.
