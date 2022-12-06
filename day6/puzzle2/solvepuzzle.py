data = open('input.txt').read()
data = data.replace('\n', '')

buffer = []
for i, char in enumerate(data):
    if len(buffer) == 14:
        if len(list(set(buffer))) == 14:
            print(buffer)
            print(i)
            break
        else:
            buffer.pop(0)
    buffer.append(char)

