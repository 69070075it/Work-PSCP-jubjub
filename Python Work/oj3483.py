'''มาเป็นทีม'''
def main():
    '''มาเป็นทีม'''
    n, m = map(int, input().split())

    if not (1 <= n <= 10 and 1 <= m <= 20):
        print("Data Incorrect")
        return

    teams = []
    for _ in range(n):
        scores = list(map(int, input().split()))
        if len(scores) != m or any(not (0 <= s <= 100) for s in scores):
            print("Data Incorrect")
            return
        teams.append(scores)

    total_all = 0
    for i, scores in enumerate(teams, 1):
        team_sum = sum(scores)
        team_avg = team_sum / m
        team_max = max(scores)
        total_all += team_sum
        print(f"Team {i}: Average = {team_avg:.2f}, Max = {team_max}")

    print(f"Total Score of All Teams = {total_all}")

main()
