## A Multi-Agent System for Hierarchical Control 

The following paper is a theoretical outline of OpenAgent systems. [See examples](https://github.com/CarsonScott/OpenAgent/blob/master/EXAMPLE.md) for actual code and step-by-step instructions.

### Agents

An agent is a system of memory and a set of actions, where the actions are functions that manipulate memory, and the functions are agents that are stored in a set.

### Oligarchies 

Stored agents are considered to be subordinates of the higher agent. Their interactions mimic that of a manager-employee relationship, where the manager's job is to delegate tasks to employees, whose job it is to carry out those tasks and report back when finished. In a sense, agents are given "tasks" when a higher agent calls their functions, and  "report back" when it receives their outputs.

A superagent passing inputs to subagents is like a supervisor delegating tasks to employees. The superagent controls behavior and of subagents, as well as their access to information.  

### Control

This enables control over multi-level systems. Top-level agents need only control those from one level down, and allow control to "propagate" down to the lowest-level agents. 

## A Formal Language for Nested Automata

### Notation

DOT (DO-OF-TO) notation is a phrase structure that reflects mathematical functions, such that f(x) -> y is written as: 

#### .f[x]:y

The letter symbols represent stored variables and functions. Functions require an additional piece of information that describes the inputs, where brackets with contained argument variables are placed right after the function.

### Grammar

The use of brackets is restricted, such that all brackets are considered invalid except for those that immediately follows functions.

Periods define the start of new statements, as well as the end of previous statements. Colons indicate the storage of values, where the left side contains a variable and the right side contains a value, and the result of the colon is that the variable takes on the value.

