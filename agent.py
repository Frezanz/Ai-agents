class Agent:
    def decide(self, observation):
        r, c = observation["position"]
        gr, gc = observation["goal"]
        available = observation["available_actions"]

        # Prefer reducing horizontal distance, then vertical distance.
        candidates = []

        if gc > c:
            candidates.append("RIGHT")
        elif gc < c:
            candidates.append("LEFT")

        if gr > r:
            candidates.append("DOWN")
        elif gr < r:
            candidates.append("UP")

        # Fall back to any legal action.
        candidates.extend(available)

        for action in candidates:
            if action in available:
                return action

        raise RuntimeError("Agent has no valid action.")
