import csv

#method1 : Using CSV modile's reader function
def csv_reader(file_obj):
    """
    read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

#method2 : Using DictReader class
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader"
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])



if __name__ == "__main__":
    csv_path = "data.csv"    
    with open(csv_path) as f_obj:
        csv_dict_reader(f_obj)

    print("="*200)

    
    csv_path = "TB_data_dictionary_2016-12-22.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)

 

