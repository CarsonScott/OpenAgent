import OpenAgent as oa

# Initialize agent, size of memory  
ca = oa.CustomAgent(3)

# Delegate memory to set of parameters 
ca.add_input(0)
ca.add_input(1)

# Delegate memory to set of outputs 
ca.add_output(2)

# Store subordinates to call their functions
b = oa.Add()
ca.add_agent(b)

# Store phrases to convert into actions
a = ".0[0,1]:2"
ca.add_action(a)

# Compute output
x = [100, 23]
y = ca.f(x)
