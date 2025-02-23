class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # Brute Force Approach
        # for _ in range(n):
        #     new_cells = [0]*8
        #     for i in range(1, 7):
        #         if cells[i-1] == cells[i+1]:
        #             new_cells[i] = 1
        #         else:
        #             new_cells[i] = 0
        #     cells = new_cells
        # return cells

        # Time Complexity = O(N X 8) => N = number of days, 8 = number of cells
        # Space Complexity = O(1) => only store current state

        # Optimized Approach
        # Detect cycles in state transition => There are 2^8 = 256 states -> repeat itself after certain number of days
        # Simulate state transition -> store each state in a dictionary with day occured
        # If state repeats -> calculate cycle length and skip unncessesary simulation
        # Use Cycle length to determine state after N days

        def next_state(state):
            new_state = [0]*8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    new_state[i] = 1
                else:
                    new_state[i] = 0
            return new_state

        # Store state and corresponding days
        seen = {}
        cycle_length = 0

        # Simulate until cycle detected
        for day in range(n):
            state_key = tuple(cells)
            if state_key in seen:
                cycle_length = day - seen[state_key]
                remaining_days = (n - day) % cycle_length
                for _ in range(remaining_days):
                    cells = next_state(cells)
                return cells
            else:
                seen[state_key] = day
                cells = next_state(cells)

        return cells

        # Time Complexity = O(256) => 256 possible states
        # Space Complexity = O(256) => storing states in dictionary