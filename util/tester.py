#
#
# base = [['Total Request', 31334192], ['Total Passed Request', 31332646], ['Total Failed Request', 1546], ['Average Hits per seconds', '2770.486'], ['Overall Mean Response Time', 0.08], ['90% Mean Response Time', 0.096], ['Error %', 0.0]]
# curr = [['Total Request', 312192], ['Total Passed Request', 3131146], ['Total Failed Request', 1146], ['Average Hits per seconds', '210.486'], ['Overall Mean Response Time', 0.18], ['90% Mean Response Time', 0.196], ['Error %', 1.0]]
#
# newL = [['Type', 'base', 'curr', 'delta']]
#
# for i, j in zip(base, curr):
#     newL.append([i[0],i[1],j[1], float(j[1]) - float(i[1])])
# print(newL)

import splunklib.client as client
import splunklib.results as results
# HOST = "aa"
# PORT = 8089
# USERNAME = "aa"
# PASSWORD = "aa"
# SCHEME = "https"
# service = client.connect(
#     host=HOST,
#     port=PORT,
#     username=USERNAME,
#     password=PASSWORD)
#
# kwargs_oneshot = {"earliest_time": "2018-08-02T02:50:00.000-07:00",
#                   "latest_time": "2018-08-02T02:52:00.000-07:00"}
# searchquery_oneshot = "search index=\" indexname\""
#
# oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)
#
# # Get the results and display them using the ResultsReader
# reader = results.ResultsReader(oneshotsearch_results)
# for item in reader:
#     print(item)
#     print(item)
HOST = "hostinfo"
PORT = 8089
USERNAME = "username"
PASSWORD = "password"
SCHEME = "https"
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

kwargs_oneshot = {"earliest_time": "2018-08-30T01:44:00.000",
                  "latest_time": "2018-08-30T04:52:00.000"
                  }
# searchquery_oneshot = """
# search index="est_gatling_test" logger="io.gatling.http.ahc.ResponseProcessor" level="DEBUG"
# | rex field=_raw "List\\(GroupBlock\\(List\\((?<SimulationName>.+?), (?<TransactionName>.+?)\\).+?HTTP request:\\\n(POST|GET) (?<RequestUrl>.+?)\\\n.+?HTTP response:\\\nstatus=\\\n(?<ResponseCode>.+?)\\\n"| table SimulationName TransactionName RequestUrl ResponseCode
# """

# searchquery_oneshot = """
# search index="est_gatling_test" logger="io.gatling.http.ahc.ResponseProcessor" level="DEBUG"
# """
#
#
# job = service.jobs.create(searchquery_oneshot, **kwargs_oneshot)
# result_stream = job.results(count=0)
# reader = results.ResultsReader(result_stream)
# file = open("errorGraphData.txt", "a+")
# for item in reader:
#     msg = list(item.values())[3]
#     file.write((msg) + "\n")
#     # file.write(str(list(item.values())[3]) + "\n")
# file.close()

# oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)
#
# # Get the results and display them using the ResultsReader
# reader = results.ResultsReader(oneshotsearch_results)
# for item in reader:
#     for key, value in item.items():
#         print(key, value)


# data = """\
# <span style='font-family:Symbol' lang='EN-US'>
#       <span>·
#             <span style='font:8.0pt;Times New Roman;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
#       </span>
# </span>
# <span style='color:black' lang='EN-US'>Observed errors on 'Resource Backend Errors' graph
#                                        throughout the load test duration.
# </span>
# """
#
# part2 = MIMEText(data, 'html')
#
# msg.attach(part2)
# server.sendmail(frm, to, msg.as_string())
#
# import re
# import urllib
# import bs4 as bs
# # req = urllib.request.urlopen(' ').read()
# # soup = bs.BeautifulSoup(req, 'lxml')
# # reqPattern = re.compile(r"Implementation: (.+?)\s")
# #
# # script = soup.find("body")
# # match = reqPattern.search(str(soup))
# # file = open("loadtestDetail1.txt", "w+")
# # file.write(str(script))
# # file.close()
# builddetail = {}
# uiReq = urllib.request.urlopen('').read()
# uiSoup = bs.BeautifulSoup(uiReq, 'lxml')
# uiScript = uiSoup.find("body")
# uiBuildPattern = re.compile(r"p>(.+?)<")
# match = uiBuildPattern.search(str(uiScript))
# if match:
#     builddetail["UI"] = str(match.group(1))

# print(match.group(1))
# print(builddetail)
import ast
# _90centFileBase = open("_90cent.txt","r")
# _90centDataBase = ast.literal_eval(_90centFileBase.read())
# _90centFileBase.close()
#
# cent90InSecBase = [[]]
# cent90InSecCurr = [[]]
# for tempVar in _90centDataBase:
#     tempVar[0] = int(tempVar[0]/1000) - int(_90centDataBase[0][0]/1000)
#     cent90InSecBase.append([tempVar[0], tempVar[1]])
# import os
#
# allResultBuildNumber = os.listdir("\\")
# allResultBuildNumber.sort(reverse=True)
# print(allResultBuildNumber)