files = ['201806citibiketripdata.csv', '201807citibiketripdata.csv', 
         '201808citibiketripdata.csv', '201809citibiketripdata.csv']

with open('PySummer18.csv', 'w+') as outfile:
    for index, filename in enumerate(files):
        with open(filename) as infile:
            rows = infile.readlines()
            if index == 0:
                outfile.write(rows[0])
            for row in rows[1:]:
                outfile.write(row)