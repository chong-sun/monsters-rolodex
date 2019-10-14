import csv
with open('b.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    with open('a.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                writer.writerow([row[0], row[1]])
                line_count += 1
            else:
                writer.writerow([row[0], row[1].replace('1', '').replace('2', '').replace('3', '').replace(':', '')])
                line_count += 1
        print(f'Processed {line_count} lines.')


