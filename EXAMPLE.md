## Example- Custom agent that returns the sum of two inputs 

![Custom Agent](https://github.com/CarsonScott/OpenAgent/blob/master/img/CustomAgent.png)

First, include the module in your file:
        
        import OpenAgent as oa

Create an agent and set the memory size:
        
        ca = oa.CustomAgent(3)

Define elements of memory to hold the input/output values:

        ca.add_input(0)
        ca.add_input(1)
        ca.add_output(2)

Store sub-agents to call their functions:

        b = oa.Add()
        ca.add_agent(b)

Store statements to convert into actions:

        a = ".0[0,1]:2"
        ca.add_action(a)

Calculate results:

        x = [27, 81]
        y = ca.f(x) 
        
        # Output: [108] 
        
