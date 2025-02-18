import sys

docs = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()
word_len = len(word)

answer = 0
i = 0
while (i < len(docs)):
    if word == docs[i:i+word_len]:
        answer += 1
        i += word_len
    else:
        i += 1

print(answer)