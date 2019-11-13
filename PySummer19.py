files = ['201906citibiketripdata.csv', '201907citibiketripdata.csv', 
         '201908citibiketripdata.csv', '201909citibiketripdata.csv']

with open('PySummer19.csv', 'w+') as outfile:
    for index, filename in enumerate(files):
        with open(filename) as infile:
            rows = infile.readlines()
            if index == 0:
                outfile.write(rows[0])
            for row in rows[1:]:
                outfile.write(row)