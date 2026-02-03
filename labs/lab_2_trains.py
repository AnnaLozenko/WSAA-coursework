# Lab 2: Trains
# Author Anna Lozenko

# Write a program that prints the data for all trains in Ireland to the console, using the Irish Rail Real Time API (XML).


import requests
import csv
from xml.dom.minidom import parseString
url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
'''
print(doc.toprettyxml(), end = " ")

# store the XML data in a file named "trains.xml"
with open("trains.xml", "w") as xmlfp:
    doc.writexml(xmlfp)
'''
# The XML file contains data about all trains currently running in Ireland. For each train, the <objTrainPositions> tag is used and following information is provided:
# Train status
# Train latitude
# Train longitude
# Train code
# Train date
# Public message
# Direction

# Modify the program to print out each of the trains codes. I.e. find the listings and iterate through them to print each train code out. Check it works.

trainNodeList = doc.getElementsByTagName("objTrainPositions")
print(len(trainNodeList))
for train in trainNodeList:
    trainCodeNode = train.getElementsByTagName("TrainCode").item(0)
    trainCode = trainCodeNode.firstChild.nodeValue.strip()
    print(trainCode)

# modify the program so that it prints out the latitudes
for train in trainNodeList:
    trainLatitudeNode = train.getElementsByTagName("TrainLatitude").item(0)
    trainLatitude = trainLatitudeNode.firstChild.nodeValue.strip()
    print(trainLatitude)

# Store the train codes in a CSV file named "train_codes.csv", with one train code per line.
with open("train_codes.csv", "w") as csvfp:
    train_writer = csv.writer(csvfp)
    trainNodeList = doc.getElementsByTagName("objTrainPositions")
    for train in trainNodeList:
        trainCodeNode = train.getElementsByTagName("TrainCode").item(0)
        trainCode = trainCodeNode.firstChild.nodeValue.strip()
        dataList = []
        dataList.append(trainCode)
        train_writer.writerow(dataList)

# Modify the program to store any other information.

with open ("train_info.csv", "w") as csvfp:
    train_writer = csv.writer(csvfp)
    # retrieve tags list
    retrieveTags = ['TrainStatus',
                    'TrainLatitude',
                    'TrainLongitude',
                    'TrainCode',
                    'TrainDate',
                    'PublicMessage',
                    'Direction']
    trainNodeList = doc.getElementsByTagName("objTrainPositions")
    for train in trainNodeList:
        dataList = []
        for tag in retrieveTags:
            tagNode = train.getElementsByTagName(tag).item(0)
            tagValue = tagNode.firstChild.nodeValue.strip()
            dataList.append(tagValue)
        train_writer.writerow(dataList)


# As an exercise only store the trains whose traincode starts with a D

with open ("train_code_d.csv", "w") as csvfp:
    train_writer = csv.writer(csvfp)
    trainNodeList = doc.getElementsByTagName("objTrainPositions")
    for train in trainNodeList:
        trainCodeNode = train.getElementsByTagName("TrainCode").item(0)
        trainCode = trainCodeNode.firstChild.nodeValue.strip()
        if trainCode.startswith("D"):
            dataList = []
            dataList.append(trainCode)
            train_writer.writerow(dataList)
