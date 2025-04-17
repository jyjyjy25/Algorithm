import sys

T = int(sys.stdin.readline())
for _ in range(T):
    input_data = list(map(int, sys.stdin.readline().split()))
    case_num = input_data[0]
    students = input_data[1:]
    
    steps = 0
    sorted_students = []
    for i in range(len(students)):
        sorted_students.append(students[i])
        lp, rp = i-1, i
        while lp >= 0:
            if sorted_students[lp] > sorted_students[rp]:
                steps += 1
                sorted_students[lp], sorted_students[rp] = sorted_students[rp], sorted_students[lp]
                lp -= 1
                rp -= 1
            else:
                break

    print(f"{case_num} {steps}")