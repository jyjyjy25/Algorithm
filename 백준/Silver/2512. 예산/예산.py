import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
total_budget = int(sys.stdin.readline())

if sum(budgets) <= total_budget:
    print(max(budgets))
else:
    low, high = 1, max(budgets)

    while (low <= high):
        mid = (low + high) // 2
        
        new_budgets = []
        for budget in budgets:
            if budget <= mid:
                new_budgets.append(budget)
            else:
                new_budgets.append(mid)

        if sum(new_budgets) > total_budget:
            high = mid - 1
        else:
            low = mid + 1

    print(high)