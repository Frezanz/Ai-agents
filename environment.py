class Environment:
    """
    The world in which the agent exists.

    Responsibilities:
    - hold the current world state
    - expose an observation to the agent
    - receive an action from the agent
    - apply the world's rules
    - produce the next state
    - determine whether the episode is finished
    """

    def __init__(self):
        self.state = None

    def reset(self):
        """Create/reset the environment to its initial state."""
        raise NotImplementedError

    def observe(self):
        """Return what the agent can currently perceive."""
        raise NotImplementedError

    def step(self, action):
        """Apply an agent action and update the world."""
        raise NotImplementedError