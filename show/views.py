import ast
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
import os
from util.Constants import URL
from util import Screenshoter

url = str(URL)

def index(request):
    file = open("pechankon.txt", "a")
    file.write( str(request.META.get('REMOTE_ADDR')) + "," + str(request.META.get('CLIENTNAME')) + "\n")
    file.close()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.sep.join(dir_path.split(os.path.sep)[:-1])
    result_dir = os.path.join(base_dir, "Results")
    # allResultBuildNumber = os.listdir(result_dir+"\\")
    # allResultBuildNumber.sort(reverse=True)
    try:
        histoReq = open(result_dir + "\\reqCountHisto.txt","r")
        histoReqData = ast.literal_eval(histoReq.read())
        histoReq.close()
    except:
        histoReqData = 0

    return render(request, 'show/GetTestDetail.html',{'histoRequestCount': histoReqData})


def showdata(request, buildNumber):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.sep.join(dir_path.split(os.path.sep)[:-1])
    result_dir = os.path.join(base_dir, "Results")
    allResultBuildNumber = os.listdir(result_dir+"\\")
    allResultBuildNumber.sort(reverse=True)
    build_dir = os.path.join(result_dir, str(buildNumber))
    if os.path.isdir(build_dir):
        try:
            purposeFile = open(build_dir + "\\loadtestPurpose.txt","r")
            purposeData = str(purposeFile.read())
            purposeFile.close()
        except:
            purposeData = "Verification Test."

        globalFile = open(build_dir + "\\globalData.txt","r")
        globalData = ast.literal_eval(globalFile.read())
        globalFile.close()

        summaryFile = open(build_dir + "\\summaryData.txt","r")
        summaryData = ast.literal_eval(summaryFile.read())
        summaryFile.close()

        aggRepFile = open(build_dir + "\\_aggReport.txt","r")
        aggRepData = ast.literal_eval(aggRepFile.read())
        aggRepFile.close()

        slaResponseTime = [[]]
        slaError = [[]]
        for data in aggRepData:
            if(float(data[2]) >= 3.00 ):
                slaResponseTime.append([data[0], data[2]])
            if(float(data[7]) >= 1.00 ):
                slaError.append([re.sub(r"\_", "_ ", data[0]), data[7]])
        slaResponseTime.pop(0)
        slaError.pop(0)

        _90centFile = open(build_dir + "\\_90cent.txt", "r")
        _90centData = ast.literal_eval(_90centFile.read())
        _90centFile.close()

        _errGraphFile = open(build_dir + "\\errorGraphData.txt", "r")
        _errGraphData = ast.literal_eval(_errGraphFile.read())
        _errGraphFile.close()

        _maxFile = open(build_dir + "\\_maxData.txt", "r")
        _maxData = ast.literal_eval(_maxFile.read())
        _maxFile.close()

        _userFile = open(build_dir + "\\_userData.txt", "r")
        _userData = ast.literal_eval(_userFile.read())
        _userFile.close()

        for i in range(0,_userData.__len__()):
            _userData[i][0] = int(_userData[i][0]) - 14400000

        testStartTime = datetime.utcfromtimestamp(int(_userData[0][0])/1000)
        testEndTime = datetime.utcfromtimestamp(int(_userData[_userData.__len__()-1][0])/1000)

        _errorFile = open(build_dir + "\\errorData.txt","r")
        _errorData = ast.literal_eval(_errorFile.read())
        _errorFile.close()

        _parsedErrorFile = open(build_dir + "\\parsedErrorData.txt","r")
        _parsedErrorData = ast.literal_eval(_parsedErrorFile.read())
        _parsedErrorFile.close()

        _loadTestFile = open(build_dir + "\\loadtestDetail.txt","r")
        _loadTestData = ast.literal_eval(_loadTestFile.read())
        _loadTestFile.close()

        try:
            buildFile = open(build_dir + "\\buildDetail.txt","r")
            buildData = ast.literal_eval(buildFile.read())
            buildFile.close()

        except Exception:
            buildData = 0

        try:
            baselineFile = open(build_dir + "\\baselineFile.txt","r")
            baselineTest = ast.literal_eval(baselineFile.read())
            baselineFile.close()

        except Exception:
            baselineTest = 0

        return render(request, 'show/Showstopper.html', {'buildNumber': buildNumber,
                                                         'aggRepData': aggRepData,
                                                         'slaErrorData': slaError,
                                                         'slaResponseData': slaResponseTime,
                                                         '90centData': _90centData,
                                                         'errGraphData': _errGraphData,
                                                         'maxData': _maxData,
                                                         'errorData': _errorData,
                                                         'parsedErrorData': _parsedErrorData,
                                                         'loadTestData': _loadTestData,
                                                         'globalData': globalData,
                                                         'summaryData': summaryData,
                                                         'testStartTime': testStartTime,
                                                         'testEndTime': testEndTime,
                                                         'userData': _userData,
                                                         'baselineTest': str(baselineTest),
                                                         'URL': url,
                                                         'buildData': buildData,
                                                         'purposeData': purposeData,
                                                         'allResultBuildNumber': allResultBuildNumber})
    else:
        return HttpResponse("Result of build number : " + str(buildNumber) + " is not present. "
                            "<a href='"+ url +"/fetcher/save/" + str(buildNumber) +
                            "/Verification Test'>Click here</a> to save the results for this build.")
