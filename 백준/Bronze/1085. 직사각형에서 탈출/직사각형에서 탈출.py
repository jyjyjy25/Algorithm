x, y, w, h = map(int, input().split())

list = []
list.append(w-x)
list.append(x-0)
list.append(h-y)
list.append(y-0)

print(min(list))