with open('file1.txt', 'r') as file1:
    with open('file2.txt', 'r') as file2:
        different = set(file1).difference(file2)

different.discard('\n')

with open('result1.txt', 'w') as file_out:
    for line in different:
        file_out.write(line)


with open('file2.txt', 'r') as file2:
    with open('file1.txt', 'r') as file1:
        different = set(file2).difference(file1)

different.discard('\n')

with open('result2.txt', 'w') as file_out:
    for line in different:
        file_out.write(line)
