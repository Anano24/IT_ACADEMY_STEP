
with open("text.txt", "w") as file:
    for i in range(1, 1001):
        file.write(f"{i}. This is line {i}\n")



non_empty_lines = 0

with open("text.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.strip():
            non_empty_lines += 1

print(f'Total lines in the file: {len(lines)}')
print(f'Number of non-empty lines: {non_empty_lines}')
