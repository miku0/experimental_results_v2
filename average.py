import csv
import sys
#filename = sys.argv[1]
file_query = ["project_search.csv", "project2_search.csv"]
file_counts = ["project_counts.csv", "project2_counts.csv"]

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def set_address(filename):
    set_address = set()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            set_address.add(row[0])
    return set_address

def cal_average(data):
    false_count = 0
    number_sum = 0
    for row in data:
        if row[1] == "false":
            false_count += 1
        else:
            number_sum += int(row[1])
    false_average = false_count / len(data)
    number_average = number_sum / (len(data) - false_count)
    print("false_num, average: ", false_average, number_average)

def cal_selected_average(data,set_address):
    false_count_ok = 0
    number_sum_ok = 0
    false_count_ng = 0
    number_sum_ng = 0
    for row in data:
        if row[0] in set_address:
            if row[1] == "false":
                false_count_ok += 1
            else:
                number_sum_ok += int(row[1])
        else:
            if row[1] == "false":
                false_count_ng += 1
            else:
                number_sum_ng += int(row[1])
    false_average_ok = false_count_ok / len(set_address)
    number_average_ok = number_sum_ok / (len(set_address) - false_count_ok)
    print("success search: ", false_average_ok, number_average_ok)
    false_average_ng = false_count_ng / (len(data)-len(set_address))
    number_average_ng = number_sum_ng / (len(data)-len(set_address) - false_count_ng)
    print("false search: ", false_average_ng, number_average_ng)


print("Used all addresses")
for i in range(len(file_query)):
    print(i)
    cal_average(read_csv(file_query[i]))

print("Used selected address")
for i in range(len(file_query)):
    print(i)
    cal_selected_average(read_csv(file_query[i]),set_address(file_counts[i]))
