# BAPC Award Ceremony Rank Tracker
# https://open.kattis.com/problems/bapc2023f
#

def final_rank(T, P, F, teams, chants):
    # Count initial accepted submissions for each team
    accepted = [row.count('A') for row in teams]

    # Store indexes of pending submissions per team (left to right)
    pending_pos = [[] for _ in range(T)]
    for i in range(T):
        for j in range(P):
            if teams[i][j] == 'P':
                pending_pos[i].append(j)

    # Process each pending submission reveal
    for _, result in chants:
        # Find lowest-ranked team with pending submissions
        team = None
        for i in range(T - 1, -1, -1):
            if pending_pos[i]:
                team = i
                break

        pos = pending_pos[team].pop(0)  # resolve leftmost pending

        # Rejected → nothing changes
        if result.startswith("Aaaw"):
            continue

        # Accepted → count extra 'y'
        y_count = result.count('y')
        passes = y_count - 3          # extra y's = number of passed teams
        accepted[team] += 1           # gain one accepted submission

        # Move team upward according to number of passes
        new_rank = max(0, team - passes)
        if new_rank < team:
            # Extract and reinsert team at new rank position
            acc_val = accepted.pop(team)
            pend = pending_pos.pop(team)
            accepted.insert(new_rank, acc_val)
            pending_pos.insert(new_rank, pend)

            # Adjust favourite team rank if needed
            if F - 1 == team:
                F = new_rank + 1
            elif new_rank <= (F - 1) < team:
                F += 1

    return F
