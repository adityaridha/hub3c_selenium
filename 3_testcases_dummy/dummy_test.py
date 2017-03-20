from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from datetime import datetime
from collections import Counter
import texttable as tt
import time
import csv


USER_NAME 			= "aditya.ridharrahman@geekseat.com.au"
PASSWORD 			= "ZXasqw12"
HUB3C_URL			= "https://test.hub3c.com/"
HUB3C_DASHBOARD_URL = "http://demo.hub3c.com/Home/Index"

def convert_round(data):
    if len(data) == 3:
        round_value = round(int(latency), -2)
    if len(data) == 4:
        round_value = round(int(latency), -3)
    if len(data) == 5:
        round_value = round(int(latency), -3)
    return round_value

'''time test'''
# print(time.localtime(time.time()))
# localtime = time.asctime( time.localtime(time.time()) )
# print ("Local current time :", localtime)
# print(datetime.now())

'''read csv test'''
# tab = tt.Texttable()
# with open('load_test.csv') as csvfile:
#     readcsv = csv.reader(csvfile, delimiter=',')
#     data = list(readcsv)
#     row_count = len(data) - 1 #minus 1 for decline the header
#     label_list= []
#
#     for row in data[1:]:
#         label_list.append(row[4])
#     label_data = list(Counter(label_list))
#
#     print("Action type list : {}".format(label_data))
#     print("Number sample per action : {}".format(int(row_count/len(label_data))))
#
#     for label in label_data :
#         round_latency_list = []
#         latency_total = 0
#         print("\nCollecting data for {} activity".format(label))
#
#         for row in data[1:] :
#             if label == row[4] :
#                 latency = row[9]
#                 round_latency = convert_round(latency)
#                 round_latency_list.append(round_latency)
#                 latency_total = latency_total + int(latency)
#             latency_average = latency_total / row_count
#             distributions_time = list(Counter(round_latency_list).keys())
#             distributions_time.sort()  #if it pass as a variable will return 'None'
#
#             sample_count_total = 0
#
#         response_data = [['header','header']]
#         for sample in distributions_time :
#             sample_count = Counter(round_latency_list)[sample]
#             response_data.append([sample, sample_count])
#             # print("Response Time : {}, Count : {}".format(sample, sample_count))
#             sample_count_total = sample_count_total + sample_count
#         print("sample total : {}".format(sample_count_total))
#         print("latency average = {} ms".format(latency_average))
#
#         tab.reset()
#         tab.add_rows(response_data)
#         tab.set_cols_align(['r', 'r'])
#         tab.header(['Response Time', 'Count'])
#         print(tab.draw())

'''table test'''
# tab = tt.Texttable()
# with open('load_test.csv') as csvfile:
#     readcsv = csv.reader(csvfile, delimiter=',')
#     data = list(readcsv)
#     row_count = len(data) - 1 #minus 1 for decline the header
#

#
# x = [[]] # The empty row will have the header
#
# for i in range(1,11):
#     x.append([i,i**2,i**3])
#

'''write csv test'''

with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])