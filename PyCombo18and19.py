files = ['PySummer18.csv', 'PySummer19.csv']

with open('PyCombo18and19.csv', 'w+') as outfile:
    for index, filename in enumerate(files):
        with open(filename) as infile:
            rows = infile.readlines()
            if index == 0:
                outfile.write(rows[0])
            for row in rows[1:]:
                outfile.write(row)