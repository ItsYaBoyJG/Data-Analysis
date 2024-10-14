import csv

with open("Data_Sets/iFood_BA_Test/ifood_df.csv") as file:
    reader = csv.reader(file)
    with open('Data_Sets/iFood_BA_Test/new_ifood_df.csv') as new:
        writer = csv.writer(new)
        for row in reader:
            nr = [' '.join(row)]
            writer.writerow(nr)