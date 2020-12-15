# Jessica Valenzuela
# Assignment 9
# This program will 5 analysis on the Pew_survery.csv file provided to us in class.
# Analysis 1  How often do you use the internet?
# Analysis 2: Do you ever use social media sites?
# Analysis 3: Do you mostly use the internet via cell phone, or some other device?
# Analysis 4: Percentage of people use each type of social media
# Analysis 5: Does gender have an affect on if use social media site?
# After it collects these results it will display them both on the terminal and a graph that is saved as png in your current directory

# TO RUN THE PROGRAM
# first pip3 install pandas, numpy and matplotlib
# next run python3 Valenzuela_HW9.

import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# list all the columns for your analysis
col_list = ["respid", "intfreq", "q20", "snsint2", "web1a", "web1b",
            "web1c", "web1d", "web1e", "web1f", "web1g", "web1h", "web1i", "sex"]

# use pandas to read csv
df = pd.read_csv("Pew_Survey.csv", usecols=col_list)


# average function
def average(list):
    # return the sum of a given list devided by the length of the list
    return sum(list)/len(list)

# countResults is a function that count the results for each survey question (one column)
# https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray helped me count unique values


def countResults(list):
    # first create an array with results being passed in
    results = np.array(list)
    # create two variables unique and count and then use numpy to get unique results and set count to true
    unique, counts = np.unique(results, return_counts=True)
    # return a dictionary with the unique result and the amount of times unique result appeared.
    return(dict(zip(unique, counts)))


# function to help me calculate the pectentage of the amount of people who voted for a certain answer
def percentage(number, list):
    return((number/len(list))*100)


# Analysis 1
# intfreq: How often do you use the internet.
print("\nHow often do you use the internet?")
print("=============Results==============")
# get the count of the unique results of the column intefreq
intfreqResults = countResults(df["intfreq"])
# get the average answer of column intfreq
averageIntfreq = average(df['intfreq'])
# get the average answer of column intfreq
ipercentage1 = percentage(intfreqResults[1], df["intfreq"])
ipercentage2 = percentage(intfreqResults[2], df["intfreq"])
ipercentage3 = percentage(intfreqResults[3], df["intfreq"])
ipercentage4 = percentage(intfreqResults[4], df["intfreq"])
ipercentage5 = percentage(intfreqResults[5], df["intfreq"])
ipercentage8 = percentage(intfreqResults[8], df["intfreq"])
ipercentage9 = percentage(intfreqResults[9], df["intfreq"])

# print the results
print(f"Average result: {averageIntfreq}")
print(f"Percentage voted for 1 (Almost contantly): {ipercentage1}%")
print(f"Percentage voted for 2 (Several times a day): {ipercentage2}%")
print(f"Percentage voted for 3 (About once a day): {ipercentage3}%")
print(f"Percentage voted for 4 (Several times a week): {ipercentage4}%")
print(f"Percentage voted for 5 (Less often): {ipercentage5}%")
print(f"Percentage voted for 8 (Don’t know): {ipercentage8}%")
print(f"Percentage voted for 9 (Refused): {ipercentage9}%")

# Plot results into bar graph
# followed this website to plot bar graph https://benalexkeen.com/bar-charts-in-matplotlib/

# style the graph
plt.style.use('ggplot')

# the different voting options
intfreq = ["Almost constantly", "Several times a day", "About once a day", "Several times a week", "Less often",
           "Don't know", "Refused"]
# the amount of people voted for each option
intfreqAmount = [intfreqResults[1], intfreqResults[2], intfreqResults[3], intfreqResults[4],
                 intfreqResults[5], intfreqResults[8], intfreqResults[9]]
intfreq_pos = [i for i, _ in enumerate(intfreq)]

# create figure and give it a width and height
fig = plt.figure(figsize=(20, 10))

# create bar graph with color green and bar width .8
plt.bar(intfreq_pos, intfreqAmount, color='g', width=.8)

# label y and x axis
plt.ylabel("Amount of People")
plt.xlabel("Voting Options")
# label xticks
plt.xticks(intfreq_pos, intfreq)
# title of graph
plt.title("How often do you use the internet?")
# save figure as png
fig.savefig('Valenzuela_Internet_BarGraph.png')


# Analysis 2
# snsint2: Do you ever use social media sites?

print("\nDo you ever use social media sites?")
print("=============Results==============")
# get the count of the unique results of the column snsint2
snsint2Results = countResults(df["snsint2"])
# get the average answer of column snsint2
averagesnsint2 = average(df['snsint2'])
# calculate the percentage for each unique result
spercentage1 = percentage(snsint2Results[1], df["snsint2"])
spercentage2 = percentage(snsint2Results[2], df["snsint2"])

# print the results
print(f"Average result: {averagesnsint2}")
print(f"Percentage voted for 1 (yes): {spercentage1}%")
print(f"Percentage voted for 2 (no): {spercentage2}%")

# Plot results into bar graph
# followed this website to plot bar graph https://benalexkeen.com/bar-charts-in-matplotlib/

# style the graph
plt.style.use('ggplot')

# the different voting options
snsint2 = ["yes", "no"]

# the amount of people voted for each option
snsint2Amount = [snsint2Results[1], snsint2Results[2]]
snsint2_pos = [i for i, _ in enumerate(snsint2)]

# create figure and give it a width and height
fig = plt.figure(figsize=(10, 5))

# create bar graph with color green and bar width .4
plt.bar(snsint2_pos, snsint2Amount, color='g', width=.4)

# label y and x axis
plt.ylabel("Amount of People")
plt.xlabel("Voting Options")
# label xticks
plt.xticks(snsint2_pos, snsint2)
# title of graph
plt.title("Do you ever use social media sites?")
# save figure as png
fig.savefig('Valenzuela_SocialMediaUsage_BarGraph.png')

# Analysis 3
# q20 Do you mostly use the internet via cell phone, or some other device?
print("\nDo you mostly use the internet via cell phone, or some other device?")
print("=============Results==============")
# get the count of the unique results of the column q20
q20Results = countResults(df["q20"])
# calculate the percentage for each unique result
qpercentage1 = percentage(q20Results['1'], df['q20'])
qpercentage2 = percentage(q20Results['2'], df['q20'])
qpercentage3 = percentage(q20Results['3'], df['q20'])
qpercentage4 = percentage(q20Results['4'], df['q20'])
qpercentage8 = percentage(q20Results['8'], df['q20'])
qpercentage9 = percentage(q20Results['9'], df['q20'])
qpercentage = percentage(q20Results[' '], df['q20'])

# print the results
print(f"Percentage voted for 1 (Mostly on cell phone): {qpercentage1}%")
print(f"Percentage voted for 2 (Mostly on something else): {qpercentage2}%")
print(f"Percentage voted for 3 (Both equally): {qpercentage3}%")
print(f"Percentage voted for 4 (Depends): {qpercentage4}%")
print(f"Percentage voted for 8 (Don’t know): {qpercentage8}%")
print(f"Percentage voted for 9 (Refused): {qpercentage9}%")
print(f"Percentage voted for none of the above: {qpercentage}%")

# Plot results into bar graph
# followed this website to plot bar graph https://benalexkeen.com/bar-charts-in-matplotlib/

# style the graph
plt.style.use('ggplot')

# the different voting options
q20 = ["Mostly on cell phone", "Mostly on something else", "Both equally", "Depends", "Don’t know",
       "Refused", "None of the Above"]

# the amount of people voted for each option
q20Amount = [q20Results['1'], q20Results['2'], q20Results['3'], q20Results['4'],
             q20Results['8'], q20Results['9'], q20Results[' ']]
q20_pos = [i for i, _ in enumerate(q20)]

# create figure and give it a width and height
fig = plt.figure(figsize=(20, 10))
# create bar graph with color green and bar width .8
plt.bar(q20_pos, q20Amount, color='g', width=.8)
# label y and x axis
plt.ylabel("Amount of People")
plt.xlabel("Voting Options")
# label xticks
plt.xticks(q20_pos, q20)
# title of graph
plt.title("Do you mostly use the internet via cell phone, or some other device?")
# save figure as png
fig.savefig('Valenzuela_Cellphone_BarGraph.png')


# Analysis 4
# Percentage of people use each type of social media
print("\nWhat is the percentage of social media sites that people use?")
print("=============Results==============")

# get the count of the results stating 1(yes) of the columns web1a, web1b, web1c, web1d, web1e, web1f, web1g, web1h, web1i to get the amount of people use each social media site
twitterResults = countResults(df["web1a"])
useTwitter = twitterResults[1]

igResults = countResults(df["web1b"])
useIg = igResults[1]

fbResults = countResults(df["web1c"])
useFb = fbResults[1]

scResults = countResults(df["web1d"])
useSc = scResults[1]

ytResults = countResults(df["web1e"])
useYt = ytResults[1]

waResults = countResults(df["web1f"])
useWa = waResults[1]

pinResults = countResults(df["web1g"])
usePin = pinResults[1]

linkResults = countResults(df["web1h"])
useLink = linkResults[1]

redResults = countResults(df["web1i"])
useRed = redResults[1]

# calculate the total amount of people calculated by adding up all the results of who uses what social media site
total = useTwitter + useIg + useFb + useSc + \
    useYt + useWa + usePin + useLink + useRed

# print result and find percentage by dividing the amount of people who use a certain social media by the total and multiply by 100
print(f"Percentage of people who use Twitter: {(useTwitter/total)*100}%")
print(f"Percentage of people who use Instagram:{(useIg/total)*100}%")
print(
    f"Percentage of people who use Facebook: {(useFb/total)*100}%")
print(f"Percentage of people who use Snapchat: {(useSc/total)*100}%")
print(f"Percentage of people who use Youtube: {(useYt/total)*100}%")
print(f"Percentage of people who use WhatsApp: {(useWa/total)*100}%")
print(f"Percentage of people who use Pintrest: {(usePin/total)*100}%")
print(f"Percentage of people who use Linkedin: {(useLink/total)*100}%")
print(f"Percentage of people who use Reddit: {(useRed/total)*100}%")

# Plot results into bar graph
# followed this website to plot bar graph https://benalexkeen.com/bar-charts-in-matplotlib/

# style the graph
plt.style.use('ggplot')

# the different social media sites
media = ["Twitter", "Instagram", "Facebook", "Snapchat", "Youtube",
         "WhatsApp", "Pintrest", "LinkedIn", "Reddit"]
# the amount each social media site is used
mediaAmount = [useTwitter, useIg, useFb, useSc,
               useYt, useWa, usePin, useLink, useRed]
media_pos = [i for i, _ in enumerate(media)]

# create figure and give it a width and height
fig = plt.figure(figsize=(20, 10))
# create bar graph with color green and bar width .8
plt.bar(media_pos, mediaAmount, color='g', width=.8)
# label y and x axis
plt.ylabel("Amount of People")
plt.xlabel("Social Medias")
# label xticks
plt.xticks(media_pos, media)
# title of graph
plt.title("Popularity of Social Media Sites")
# save figure as png
fig.savefig('Valenzuela_SocialMedia_BarGraph.png')

# Analysis 5
# Does gender have an affect on if use social media site?
print("\nDo you ever use social media sites? (Gender Analysis)")
print("=============Results==============")
# get the count of the unique results of a combination of both columns snsint2 and sex

# https://stackoverflow.com/questions/35268817/unique-combinations-of-values-in-selected-columns-in-pandas-data-frame-and-count helped me ged the unique result of two selected results

# stored new dataframe into a variable countData
countData = df.groupby(['snsint2', 'sex']).size(
).reset_index().rename(columns={0: 'count'})

# read dataframe countData
df2 = pd.DataFrame(countData)

# total amount of unique results = getting the sum of all unique results
totalCount = df2.iloc[0]['count'] + df2.iloc[1]['count'] + \
    df2.iloc[2]['count'] + df2.iloc[3]['count']

# assign variables to each unique result
yesMale = df2.iloc[0]['count']
yesFemale = df2.iloc[1]['count']
noMale = df2.iloc[2]['count']
noFemale = df2.iloc[3]['count']

# print result
#yes + male
print(
    f"Percentage of Males who voted yes: {yesMale/totalCount*100}%")
#yes + female
print(
    f"Percentage of Females who voted yes: {yesFemale/totalCount*100}%")
#no + male
print(
    f"Percentage of Males who voted no: {noMale/totalCount*100}%")
#no + female
print(
    f"Percentage of Females who voted no: {noFemale/totalCount*100}%\n")

# Plot results into bar graph
# followed this website to plot bar graph https://benalexkeen.com/bar-charts-in-matplotlib/

# style the graph
plt.style.use('ggplot')

# the different voting options
gender = ["Yes(Male)", "Yes(Female)", "No(Male)", "No(Female)"]
# the amount of people voted for each option
genderAmount = [yesMale, yesFemale, noMale, noFemale]
gender_pos = [i for i, _ in enumerate(gender)]
# create figure and give it a width and height
fig = plt.figure(figsize=(20, 10))
# create bar graph with color green and bar width .8
plt.bar(gender_pos, genderAmount, color='g', width=.8)
# label y and x axis
plt.ylabel("Amount of People")
plt.xlabel("Gender Votes")
# label xticks
plt.xticks(gender_pos, gender)
# title of graph
plt.title("Do you ever use social media sites? (Gender Analysis)")
# save figure as png
fig.savefig('Valenzuela_Gender_BarGraph.png')
