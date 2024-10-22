import csv

class CSVHelper:

    def read_csv(self,file_name):
        test_data = []
        with open(file_name, newline='') as csvfile:
            datareader = csv.reader(csvfile)
            next(datareader)
            for row in datareader:
                test_data.append(row)
        return test_data