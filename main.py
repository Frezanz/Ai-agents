from agent import Agent
from environment import GridWorld

def main():
    world = GridWorld()
    agent = Agent()

    print("Initial world:")
    print(world.render())

    while not world.done:
        observation = world.observe()
        action = agent.decide(observation)

        result = world.step(action)

        print(f"\nObservation: {observation}")
        print(f"Decision:    {action}")
        print(f"Result:      {result}")
        print(world.render())

    print("\nSUCCESS: goal reached.")

if __name__ == "__main__":
    main()
