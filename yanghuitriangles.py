def triangles():
    row=[1]
    while True:
        yield row
        row=[1]+[row[i]+row[i+1] for i in range(len(row)-1)]+[1]
