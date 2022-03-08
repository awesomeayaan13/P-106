
from time import sleep
import plotly.express as px
import csv
import numpy as np


def getDataSource(dataPath):
    sleep=[]
    coffee=[]
    with open(dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            sleep.append(float(row["sleep in hours"]))
            coffee.append(float(row["Coffee"]))
    return{"x":sleep,"y":coffee}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])

def setup():
    dataPath="cups of coffee vs hours of sleep.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

setup()