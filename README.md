# OpenAgent

### Agents, Oligarchies, and Control 

An agent is defined by a set of data and a set of functions, called memory and actions, respectively. An agent has a function that executes a sequence of actions, which manipulate data in the memory. Every action is made of the function of a lower-level agent.The superagent (higher-level) is said to contain the subagent(lower-level). 

A superagent passing inputs to subagents is like a supervisor delegating tasks to employees. The superagent controls behavior and of subagents, as well as their access to information.  

This enables control over multi-level systems. Top-level agents need only control those from one level down, and allow control to "propagate" down to the lowest-level agents. 

## A Language for Nested Automata

### Notation

Dot (DO-OF-TO) notation is a phrase structure that reflects mathematical functions, such that f(x) -> y is written as: 

#### .f[x]:y

The letter symbols represent stored variables and functions. Functions require an additional piece of information that describes the inputs, where brackets with contained argument variables are placed right after the function.

### Grammar
The use of brackets is restricted, such that all brackets are considered invalid except for those that immediately follows functions.

Periods define the start of new statements, as well as the end of previous statements. Colons indicate the storage of values, where the left side contains a variable and the right side contains a value, and the result of the colon is that the variable takes on the value.

