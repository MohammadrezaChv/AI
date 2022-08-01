from agents import *
from notebook import psource
def RANDOM():
    psource(TrivialVacuumEnvironment)

    # These are the two locations for the two-state environment
    loc_A, loc_B = (0, 0), (1, 0)

    # Initialize the two-state environment
    trivial_vacuum_env = TrivialVacuumEnvironment()

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

def TABLE():
    psource(TrivialVacuumEnvironment)
    trivial_vacuum_env = TrivialVacuumEnvironment()

    table = {((loc_A, 'Clean'),): 'Right',
                 ((loc_A, 'Dirty'),): 'Suck',
                 ((loc_B, 'Clean'),): 'Left',
                 ((loc_B, 'Dirty'),): 'Suck',
                 ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
                 ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
                 ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
                 ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
                 ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
                 ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck'
            }

    # Create a table-driven agent
    table_driven_agent = Agent(program=TableDrivenAgentProgram(table=table))



    # Add the table-driven agent to the environment
    trivial_vacuum_env.add_thing(table_driven_agent)

    print("TableDrivenVacuumAgent is located at {}.".format(table_driven_agent.location))

    # Run the environment
    trivial_vacuum_env.step()

    # Check the current state of the environment
    print("State of the Environment: {}.".format(trivial_vacuum_env.status))

    print("TableDrivenVacuumAgent is located at {}.".format(table_driven_agent.location))

def SIMPLE():
    loc_A = (0, 0)
    loc_B = (1, 0)
    psource(TrivialVacuumEnvironment)
    trivial_vacuum_env = TrivialVacuumEnvironment()
    """We change the simpleReflexAgentProgram so that it doesn't make use of the Rule class"""


    def SimpleReflexAgentProgram():
        """This agent takes action based solely on the percept. [Figure 2.10]"""

        def program(percept):
            loc, status = percept
            return ('Suck' if status == 'Dirty'
                    else 'Right' if loc == loc_A
            else 'Left')

        return program


    # Create a simple reflex agent the two-state environment
    program = SimpleReflexAgentProgram()
    simple_reflex_agent = Agent(program)
    trivial_vacuum_env.add_thing(simple_reflex_agent)

    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))

    # Run the environment
    trivial_vacuum_env.step()

    # Check the current state of the environment
    print("State of the Environment: {}.".format(trivial_vacuum_env.status))

    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))

def MODEL():
    # Delete the previously added simple reflex agent
    psource(TrivialVacuumEnvironment)
    trivial_vacuum_env = TrivialVacuumEnvironment()

    # TODO: Implement this function for the two-dimensional environment
    def update_state(state, action, percept, model):
        pass

    # Create a model-based reflex agent
    model_based_reflex_agent = ModelBasedVacuumAgent()

    # Add the agent to the environment
    trivial_vacuum_env.add_thing(model_based_reflex_agent)

    print("ModelBasedVacuumAgent is located at {}.".format(model_based_reflex_agent.location))

    # Run the environment
    trivial_vacuum_env.step()

    # Check the current state of the environment
    print("State of the Environment: {}.".format(trivial_vacuum_env.status))

    print("ModelBasedVacuumAgent is located at {}.".format(model_based_reflex_agent.location))

    print("State of the Environment: {}.".format(trivial_vacuum_env.status))


RANDOM()
TABLE()
SIMPLE()
MODEL()