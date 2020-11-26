import plotly.figure_factory as ff
import plotly.graph_objs as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv(
    "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Python Classes/Single sample z-tests/Data1.csv")

data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math_score"], show_hist=False)

ReadingScore_Mean = statistics.mean(data)
Sd = statistics.stdev(data)

print("Mean of the Data : ", ReadingScore_Mean)
print("Standard Deviation of the Data : ", Sd)

# fig.show()


def randomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    ReadingScore_Mean = statistics.mean(dataSet)
    return ReadingScore_Mean


meanList = []
for i in range(0, 1000):
    setOfMeans = randomSetOfMean(1000)
    meanList.append(setOfMeans)

ReadingScore_SD = statistics.stdev(meanList)

ReadingScore_first_std_deviation_start, ReadingScore_first_std_deviation_end = ReadingScore_Mean - \
    ReadingScore_SD, ReadingScore_Mean+ReadingScore_SD
ReadingScore_second_std_deviation_start, ReadingScore_second_std_deviation_end = ReadingScore_Mean - \
    (2*ReadingScore_SD), ReadingScore_Mean+(2*ReadingScore_SD)
ReadingScore_third_std_deviation_start, ReadingScore_third_std_deviation_end = ReadingScore_Mean - \
    (3*ReadingScore_SD), ReadingScore_Mean+(3*ReadingScore_SD)

# fig1 = ff.create_distplot([meanList], ["Student1"], show_hist=False)
# fig1.add_trace(go.Scatter(x=[ReadingScore_Mean, ReadingScore_Mean], y=[
#                0, 0.17], mode="lines", name="Mean"))

# fig1.add_trace(go.Scatter(x=[ReadingScore_first_std_deviation_start, ReadingScore_first_std_deviation_start], y=[
#                0, 0.17], mode="lines", name="Start STD 1"))
# fig1.add_trace(go.Scatter(x=[ReadingScore_first_std_deviation_end, ReadingScore_first_std_deviation_end], y=[
#                0, 0.17], mode="lines", name="End STD 1"))

# fig1.add_trace(go.Scatter(x=[ReadingScore_second_std_deviation_start, ReadingScore_second_std_deviation_start], y=[
#                0, 0.17], mode="lines", name="Start STD 2"))
# fig1.add_trace(go.Scatter(x=[ReadingScore_second_std_deviation_end, ReadingScore_second_std_deviation_end], y=[
#                0, 0.17], mode="lines", name="End STD 2"))

# fig1.add_trace(go.Scatter(x=[ReadingScore_third_std_deviation_start, ReadingScore_third_std_deviation_start], y=[
#                0, 0.17], mode="lines", name="Start STD 3"))
# fig1.add_trace(go.Scatter(x=[ReadingScore_third_std_deviation_end, ReadingScore_third_std_deviation_end], y=[
#                0, 0.17], mode="lines", name="End STD 3"))

# fig1.show()

# df2 = pd.read_csv(
#     "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Python Classes/Single sample z-tests/Data2.csv")
# data2 = df["Math_score"].tolist()

# mean_of_sample1 = statistics.mean(data2)

# fig2 = ff.create_distplot([meanList], ["Student2"], show_hist=False)
# fig2.add_trace(go.Scatter(x=[ReadingScore_Mean, ReadingScore_Mean], y=[
#                0, 0.7], mode="lines", name="Mean"))

# fig2.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[
#                0, 0.7], mode="lines", name="Mean"))

# fig2.add_trace(go.Scatter(x=[ReadingScore_first_std_deviation_end, ReadingScore_first_std_deviation_end], y=[
#                0, 0.7], mode="lines", name="End STD 1"))

# fig2.show()

# df3 = pd.read_csv(
#     "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Python Classes/Single sample z-tests/Data3.csv")
# data3 = df["Math_score"].tolist()

# mean_of_sample3 = statistics.mean(data3)

# fig3 = ff.create_distplot([meanList], ["Student2"], show_hist=False)
# fig3.add_trace(go.Scatter(x=[ReadingScore_Mean, ReadingScore_Mean], y=[
#                0, 0.7], mode="lines", name="Mean"))

# fig3.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[
#                0, 0.7], mode="lines", name="Mean2"))

# fig3.add_trace(go.Scatter(x=[ReadingScore_first_std_deviation_end, ReadingScore_first_std_deviation_end], y=[
#                0, 0.7], mode="lines", name="End STD 1"))

# fig3.add_trace(go.Scatter(x=[ReadingScore_second_std_deviation_end, ReadingScore_second_std_deviation_end], y=[
#                0, 0.7], mode="lines", name="End STD 2"))

# fig3.show()

df4 = pd.read_csv(
    "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Python Classes/Single sample z-tests/Data3.csv")
data4 = df4["Math_score"].tolist()

mean_of_sample4 = statistics.mean(data4)

fig4 = ff.create_distplot([meanList], ["Student2"], show_hist=False)
fig4.add_trace(go.Scatter(x=[ReadingScore_Mean, ReadingScore_Mean], y=[
               0, 0.7], mode="lines", name="Mean"))

fig4.add_trace(go.Scatter(x=[mean_of_sample4, mean_of_sample4], y=[
               0, 0.7], mode="lines", name="Mean2"))

fig4.add_trace(go.Scatter(x=[ReadingScore_first_std_deviation_end, ReadingScore_first_std_deviation_end], y=[
               0, 0.7], mode="lines", name="End STD 1"))

fig4.add_trace(go.Scatter(x=[ReadingScore_second_std_deviation_end, ReadingScore_second_std_deviation_end], y=[
               0, 0.7], mode="lines", name="End STD 2"))

fig4.add_trace(go.Scatter(x=[ReadingScore_third_std_deviation_end, ReadingScore_third_std_deviation_end], y=[
               0, 0.7], mode="lines", name="End STD 3"))

fig4.show()

zScore = (mean_of_sample4-ReadingScore_Mean) / ReadingScore_SD
print("zScore for the sampling data 4 : ", zScore)
