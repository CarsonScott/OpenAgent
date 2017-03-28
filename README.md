## A Multi-Agent System for Hierarchical Control 

The following paper is a theoretical outline of OpenAgent systems. [See examples](https://github.com/CarsonScott/OpenAgent/blob/master/EXAMPLE.md) for actual code and step-by-step instructions.

### Agents

An agent is a system of memory and a set of actions, where the actions are functions that manipulate memory, and the functions are agents that are stored in a set.

### Oligarchies 

Stored agents are considered to be subordinates of the higher agent. Their interactions mimic that of a manager-employee relationship, where the manager's job is to delegate tasks to employees, whose job it is to carry out those tasks and report back when finished. In a sense, agents are given "tasks" when a higher agent calls their functions, and  "report back" when it receives their outputs. Therefore superagents control the behavior of subagents, along with their access to information.  

### Control

This allows control over multiple layers. The top-level supervisor controls its direct subordinates, which triggers a wave of activity that propagates to the lowest level. an agent receives inputs from a supervisor to store in memory. Each subagent is given a subset of memory, which starts the process over again. 

This  happens recursively until bottom-level output is received by their supervisors. Now activity propagates upward, and eventually reaches the top-level agent where a single output is produced and sent to the environment.

## A Formal Language for Nested Automata

### Notation

DOT (DO-OF-TO) notation is a phrase structure that reflects mathematical functions> A function f(x) -> y is written as: 

#### .f[x]:y

The letters x and y are stored variables, and f is a function. The brackets immediately following f are the parameters. In this case, f receives one parameter x.

### Grammar

A period signals that a new statement is starting. A colon indicates that a value (left of symbol) is being stored in memory (right of symbol).


