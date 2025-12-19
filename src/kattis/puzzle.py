# Problem: 2-Puzzle (Sliding Puzzle)
# URL: https://open.kattis.com/problems/2puzzle
#
# Find minimum moves to solve a 2x2 sliding puzzle using BFS.

from collections import deque

def solve_puzzle(start):
    goal = "123-"
    
    if start == goal:
        return 0
    
    q = deque([(start, 0)])
    seen = {start}
    
    while q:
        state, moves = q.popleft()
        pos = state.index('-')
        r, c = pos // 2, pos % 2
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 2 and 0 <= nc < 2:
                new_pos = nr * 2 + nc
                new_state = list(state)
                new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
                new_state = ''.join(new_state)
                
                if new_state == goal:
                    return moves + 1
                
                if new_state not in seen:
                    seen.add(new_state)
                    q.append((new_state, moves + 1))
    
    return -1
