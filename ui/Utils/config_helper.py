import csv

class ConfigHelper:
    def __init__(self, config_file):
        self.config_file = config_file

    def get_browser(self):
        with open(self.config_file, newline='') as csvfile:
            datareader = csv.reader(csvfile)
            next(datareader)  # Skip header
            for row in datareader:
                return row[0].strip().lower()