from agent import Agent
from environment import GridWorld

def test_agent_reaches_goal():
    world = GridWorld()
    agent = Agent()

    for _ in range(100):
        if world.done:
            break

        observation = world.observe()
        action = agent.decide(observation)
        world.step(action)

    assert world.done
    assert world.agent == world.goal


def test_agent_only_chooses_legal_actions():
    world = GridWorld()
    agent = Agent()

    for _ in range(20):
        if world.done:
            break

        observation = world.observe()
        action = agent.decide(observation)

        assert action in observation["available_actions"]
        world.step(action)
