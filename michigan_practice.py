""" with open('practice.txt', 'r') as file:
    data = file.readlines()
    num_char = len(data)
    print(num_char)
    
f = open('first_forty', 'w')
with open('practice.txt', 'r') as s:
    for i in s:
        f.write(i) """

olympians = [('Laoise', 31, 'Paris'), ('Harry', 37, 'London'), ('Harald', 39, 'London'), ('Agatha', 49, 'Madrid')]

outfile = open("reduce_olympics.csv", "w")
header_row = "Name, age, City"
outfile.write(header_row)
print(header_row)
for name, age, city in olympians:
    row_string = f'{name}, {age}, {city}'
    outfile.write('\n' + row_string)
    print(row_string)

outfile.close()