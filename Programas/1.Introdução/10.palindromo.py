s = input()
s = list(s)

inv = s[::-1]

count = 0

if len(s) % 2 == 0:
    for i in range(len(s)):
        if s[i] != inv[i]:
            count += 1
else:
    for i in range(len(s)):
        if s[i] != inv[i]:
            if i == len(s) // 2:
                count += 10
            else:
                count += 1
        else:
            if i == len(s) // 2:
                count += 20

if count == 2 or count == 12 or count == 20 or count == 22:
    print("POSSÍVEL")
else:
    print("IMPOSSÍVEL")
