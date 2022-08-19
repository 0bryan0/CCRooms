# Lots of help from Priyabrata Panda's 
# blog at https://blog.ineuron.ai/Reading-Text-and-Tables-From-PDF-using-Python-p3VDhjsmf9 

import tabula as tb
import csv     

def convertToCSV(inputFilename, outputFilename):
    dataFrame = tb.convert_into(f"startingResources/Dorm Dimensions/{inputFilename}", f"dormInfoCSV/{outputFilename}", 
                                pages="all", output_format="csv", lattice = True)
    return dataFrame


convertToCSV("Burton_Room_Dimensions.pdf", "BurtonDimensions.csv")
convertToCSV("Cassat_Room_Dimensions.pdf", "CassatDimensions.csv")
convertToCSV("Davis_Room_Dimensions.pdf", "DavisDimensions.csv")
convertToCSV("Evans_Room_Dimensions.pdf", "EvansDimensions.csv")
convertToCSV("Goodhue_Room_Dimensions.pdf", "GoodhueDimensions.csv")
convertToCSV("James_Room_Dimensions.pdf", "JamesDimensions.csv")
convertToCSV("Musser_Room_Dimensions.pdf", "MusserDimensions.csv")
convertToCSV("Myers_Room_Dimensions.pdf", "MyersDimensions.csv")
convertToCSV("Nourse_Room_Dimensions.pdf", "NourseDimensions.csv")
convertToCSV("Severence_Room_Dimensions.pdf", "SeverenceDimensions.csv")
convertToCSV("Watson_Room_Dimensions.pdf", "WatsonDimensions.csv")

# dataFrame = tb.convert_into("Dorm Dimensions/Burton_Room_Dimensions.pdf", 
#                             "dormInfoCSV/BurtonTest.csv", output_format = "csv")

