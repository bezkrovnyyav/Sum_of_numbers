total_num = 0

with open('input.txt', 'r') as inp, open('output.txt', 'w') as outp:
    for line in inp:
        try:
            num = float(line)
            total_num += num
        except ValueError:
           print(f'{line} is not a number!')
    outp.write(f'Total sum of all numbers: {total_num}')

print(f'Total sum of all numbers: {total_num}')