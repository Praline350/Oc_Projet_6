import csv


class Tool:
    def __init__(self):
        pass

    def read_data(self, file):
        data = []
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(tuple(row))
            return data
        
    def write_data(self, file, data):
        with open(file, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)


