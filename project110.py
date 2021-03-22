import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("project110.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["readingTime"], show_hist=False)
fig.show()
print("population mean:- ",statistics.mean(data))
def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex= random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["readingTime"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans= randomSetOfMean(10)
        meanList.append(setOfMeans)
    showFig(meanList)
    print("sampling mean:- ", statistics.mean(meanList))
setup()