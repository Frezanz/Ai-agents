class GridWorld:
    ACTIONS = ("UP", "DOWN", "LEFT", "RIGHT")

    def __init__(self):
        self.grid = [
            [".", ".", ".", ".", ".", "."],
            [".", "A", ".", "#", ".", "."],
            [".", ".", ".", "#", ".", "."],
            [".", "#", ".", ".", "G", "."],
            [".", ".", ".", ".", ".", "."],
        ]
        self.agent = (1, 1)
        self.goal = (3, 4)
        self.done = False
        self.steps = 0

    def observe(self):
        r, c = self.agent
        gr, gc = self.goal

        return {
            "position": self.agent,
            "goal": self.goal,
            "delta": (gr - r, gc - c),
            "available_actions": self.available_actions(),
            "steps": self.steps,
        }

    def available_actions(self):
        result = []
        for action in self.ACTIONS:
            if self._valid(action):
                result.append(action)
        return result

    def _next_position(self, action):
        r, c = self.agent
        moves = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1),
        }
        dr, dc = moves[action]
        return r + dr, c + dc

    def _valid(self, action):
        if action not in self.ACTIONS:
            return False

        r, c = self._next_position(action)

        if not (0 <= r < len(self.grid)):
            return False
        if not (0 <= c < len(self.grid[0])):
            return False
        if self.grid[r][c] == "#":
            return False

        return True

    def step(self, action):
        if self.done:
            return {"success": False, "reason": "episode already complete"}

        if not self._valid(action):
            self.steps += 1
            return {
                "success": False,
                "reason": "invalid action",
                "position": self.agent,
            }

        self.agent = self._next_position(action)
        self.steps += 1

        if self.agent == self.goal:
            self.done = True

        return {
            "success": True,
            "position": self.agent,
            "goal_reached": self.done,
        }

    def render(self):
        output = []
        for r, row in enumerate(self.grid):
            line = []
            for c, cell in enumerate(row):
                if (r, c) == self.agent:
                    line.append("A")
                else:
                    line.append(cell)
            output.append(" ".join(line))
        return "\n".join(output)
