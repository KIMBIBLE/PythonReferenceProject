import csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """

    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """

    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)




if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasvile".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]

    path1 = "output.csv"
    path2 = "output2.csv"

    csv_writer(data, path1)

    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

        csv_dict_writer(path2, fieldnames, my_list)
