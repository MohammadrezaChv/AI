from agents import *
from notebook import psource

psource(GraphicEnvironment)

# These are the two locations for the two-state environment


# Initialize the two-state environment
trivial_vacuum_env = GraphicEnvironment(3,3)
'''
# Check the initial state of the environment
print("State of the Environment: {}.".format(trivial_vacuum_env.status))

# Create the random agent
random_agent = Agent(program=RandomAgentProgram(['Right', 'Left', 'Suck', 'NoOp']))
# Add agent to the environment
trivial_vacuum_env.add_thing(random_agent)

print("RandomVacuumAgent is located at {}.".format(random_agent.location))
# Running the environment
trivial_vacuum_env.step()

# Check the current state of the environment
print("State of the Environment: {}.".format(trivial_vacuum_env.status))

print("RandomVacuumAgent is located at {}.".format(random_agent.location))

'''
