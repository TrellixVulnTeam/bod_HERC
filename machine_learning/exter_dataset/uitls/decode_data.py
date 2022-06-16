import csv

def TSV (path, delimiter="\t"):
    list =[]
    with open(path) as file:
        tsv_file = csv.reader(file, delimiter=delimiter)
        row_index = 0
        top = []
        for line in tsv_file:
            if row_index == 0:
                top=line
            else:
                data = {}
                colum_index = 0
                for cell in line:
                    try:
                        data[top[colum_index]] = cell
                    except:
                        pass
                    colum_index = colum_index + 1
                list.append(data)
            row_index = row_index + 1
    return list