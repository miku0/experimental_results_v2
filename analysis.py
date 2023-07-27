import csv
# Number of addresses found by normal and not found by trigger
set_found_normal = set()
with open("project_counts.csv", 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
for i in range(len(data)):
    set_found_normal.add(data[i][0])

set_NOfound_trigger = set()
with open("project2_zero.csv", 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
for i in range(len(data)):
    set_NOfound_trigger.add(data[i][0])

intersection_result = set_NOfound_trigger & set_found_normal
with open("normal_found_trigger_NOfound.csv", 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for item in intersection_result:
        writer.writerow([item])

# Number of addresses found by trigger and not found by normal
set_found_trigger = set()
with open("project2_counts.csv", 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
for i in range(len(data)):
    set_found_trigger.add(data[i][0])

set_NOfound_normal = set()
with open("project_zero.csv", 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
for i in range(len(data)):
    set_NOfound_normal.add(data[i][0])

intersection_result = set_NOfound_normal & set_found_trigger
with open("trigger_found_normal_NOfound.csv", 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for item in intersection_result:
        writer.writerow([item])
