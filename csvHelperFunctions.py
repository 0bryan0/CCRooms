import csv

def hasAdjoiningRooms(fileName):
    with open(filename, mode = 'r') as file:
        csvFile = csv.reader(file) 

        if csvFile.__next__().__contains__("Adjoining Rooms"):
            return True
        else:
            return False

