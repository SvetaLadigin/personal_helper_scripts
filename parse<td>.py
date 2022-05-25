import sys
with open(sys.argv[1], 'r') as file, open('output.txt', 'w') as fout:
    for line in file:
        tmp = line
        new_line = tmp.replace("<td>",'')
        new_line = new_line.replace("</td>",'')
        new_line = new_line.replace(" ",'')
        fout.write(new_line)
        print(new_line)

