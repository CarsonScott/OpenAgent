# OpenAgent

### Base Agents

An agent has a set of actions (functions) it can perform, as well as memory (variables) it can manipulate. Sequences of actions that reference/store data in memory are used to calculate an agent's output. The functions called during each action are also agents, called subagents, which are said to be "nested" in the upper-level agent. 

A hierarchy of agents is called a society, such that every member shares a common root, where a root is an agent not nested by another). In other words, a society is a set of subagents, along with every subagent's subagents, and so on. 

## A Language for Nested Automata

### Notation

Dot (DO-OF-TO) notation is a phrase structure that reflects mathematical functions, such that f(x) -> y is written as: 

#### .f[x]:y

The letter symbols represent stored variables and functions. Functions require an additional piece of information that describes the inputs, where brackets with contained argument variables are placed right after the function.

### Grammar
The use of brackets is restricted, such that all brackets are considered invalid except for those that immediately follows functions.

Periods define the start of new statements, as well as the end of previous statements. Colons indicate the storage of values, where the left side contains a variable and the right side contains a value, and the result of the colon is that the variable takes on the value.

