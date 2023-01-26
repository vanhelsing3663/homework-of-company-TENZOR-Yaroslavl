with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    line = input_file.readline().split()
    c, h, o = int(line[0]), int(line[1]), int(line[2])
    a1 = c // 2
    b1 = h // 6
    c1 = o // 1
    num = min(a1, b1, c1)
    print(f'Число молекул которое можно  составить {num}')
    output_file.write(str(num))
