import ast

from django.http import HttpResponse
from django.shortcuts import render
import os


def compareData(request, baseBuildNumber, currBuildNumber):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.sep.join(dir_path.split(os.path.sep)[:-1])
    result_dir = os.path.join(base_dir, "Results")

    baseBuildDir = os.path.join(result_dir, str(baseBuildNumber))
    currBuildDir = os.path.join(result_dir, str(currBuildNumber))


    if os.path.isdir(baseBuildDir):
        summaryFileBase = open(baseBuildDir + "\\summaryData.txt","r")
        summaryDataBase = ast.literal_eval(summaryFileBase.read())
        summaryFileBase.close()

        summaryFileCurr = open(currBuildDir + "\\summaryData.txt", "r")
        summaryDataCurr = ast.literal_eval(summaryFileCurr.read())
        summaryFileCurr.close()

        summaryDataComp = [[]]

        counter = 0
        for i, j in zip(summaryDataBase, summaryDataCurr):
            if counter < 3:
                summaryDataComp.append([i[0],i[1],j[1], int(j[1]) - int(i[1])])
                counter = counter + 1
            else:
                summaryDataComp.append([i[0], i[1], j[1], float("{0:.3f}".format(float(j[1]) - float(i[1])))])

        aggRepFileBase = open(baseBuildDir + "\\_aggReport.txt","r")
        aggRepDataBase = ast.literal_eval(aggRepFileBase.read())
        aggRepFileBase.close()

        aggRepFileCurr = open(currBuildDir + "\\_aggReport.txt", "r")
        aggRepDataCurr = ast.literal_eval(aggRepFileCurr.read())
        aggRepFileCurr.close()

        aggRepComp = [['Transaction', 'Mean Response Time(Sec)', 'Samples', 'Error %', 'Mean Response Time(Sec)',
                       'Samples', 'Error %', "Delta Res Time("+str(currBuildNumber)+"-"+str(baseBuildNumber)+")",
                       "Delta Sample("+str(currBuildNumber)+"-"+str(baseBuildNumber)+")"]]
        setBase = set()
        setCurr = set()
        setAllTransaction = set()
        baseCompData = {}
        currCompData = {}
        finalComparedData = []

        for tempBase in aggRepDataBase:
            setBase.add(tempBase[0])
            baseCompData[str(tempBase[0])] = [str(tempBase[2]), str(tempBase[1]), str(tempBase[7])]

        for tempCurr in aggRepDataCurr:
            setCurr.add(tempCurr[0])
            currCompData[str(tempCurr[0])] = [str(tempCurr[2]), str(tempCurr[1]), str(tempCurr[7])]

        if setBase.__len__() != 0 and setCurr.__len__() != 0:
            setAllTransaction = setBase | setCurr

        baseSample = "-"; baseResTime = "-"; baseError = "-";
        currSample = "-"; currResTime = "-"; currError = "-";
        deltaResTime = "-"; deltaSample = "-";

        for transaction in setAllTransaction:
            if transaction in setBase and transaction in setCurr:
                baseSample = baseCompData[transaction][1]
                baseResTime = baseCompData[transaction][0]
                baseError = baseCompData[transaction][2]
                currSample = currCompData[transaction][1]
                currResTime = currCompData[transaction][0]
                currError = currCompData[transaction][2]
                deltaResTime = "{0:.3f}".format(float(currResTime) - float(baseResTime))
                deltaSample = str(int(currSample) - int(baseSample))

            elif transaction not in setBase and transaction in setCurr:
                baseSample = baseResTime = baseError = deltaResTime = deltaSample = "-"
                currSample = currCompData[transaction][1]
                currResTime = currCompData[transaction][0]
                currError = currCompData[transaction][2]

            elif transaction in setBase and transaction not in setCurr:
                currSample = currResTime = currError = deltaResTime = deltaSample = "-"
                baseSample = baseCompData[transaction][1]
                baseResTime = baseCompData[transaction][0]
                baseError = baseCompData[transaction][2]

            finalComparedData.append([transaction, baseSample, baseResTime, baseError, currSample,
                                      currResTime, currError, deltaResTime, deltaSample])
        finalComparedData.pop(0)

        _90centFileBase = open(baseBuildDir + "\\_90cent.txt","r")
        _90centDataBase = ast.literal_eval(_90centFileBase.read())
        _90centFileBase.close()

        _90centFileCurr = open(currBuildDir + "\\_90cent.txt","r")
        _90centDataCurr = ast.literal_eval(_90centFileCurr.read())
        _90centFileCurr.close()

        # cent90InSecBase = [[]]
        # cent90InSecCurr = [[]]
        # for tempVar in _90centDataBase:
        #     tempVar[0] = int(tempVar[0]/1)
        #     cent90InSecBase.append([tempVar[0], tempVar[1]])
        #
        # for tempVar in _90centDataCurr:
        #     tempVar[0] = int(tempVar[0]/1)
        #     cent90InSecCurr.append([tempVar[0], tempVar[1]])

        # cent90InSecCurr.pop(0)
        # cent90InSecBase.pop(0)



        # _errGraphFile = open(build_dir + "\\errorGraphData.txt","r")
        # _errGraphData = ast.literal_eval(_errGraphFile.read())
        #
        # _maxFile = open(build_dir + "\\_maxData.txt","r")
        # _maxData = ast.literal_eval(_maxFile.read())

        try:
            errFileBase = open(baseBuildDir + "\\errorGraphData.txt","r")
            errDataBase = ast.literal_eval(errFileBase.read())
            errFileBase.close()
        except:
            errDataBase = 0

        try:
            errFileCurr = open(currBuildDir + "\\errorGraphData.txt","r")
            errDataCurr = ast.literal_eval(errFileCurr.read())
            errFileCurr.close()
        except:
            errDataCurr = 0

        try:
            maxFileBase = open(baseBuildDir + "\\_maxData.txt","r")
            maxDataBase = ast.literal_eval(maxFileBase.read())
            maxFileBase.close()
        except:
            maxDataBase = 0

        try:
            maxFileCurr = open(currBuildDir + "\\_maxData.txt","r")
            maxDataCurr = ast.literal_eval(maxFileCurr.read())
            maxFileCurr.close()
        except:
            maxDataCurr = 0

        try:
            buildFileBase = open(baseBuildDir + "\\buildDetail.txt","r")
            buildDataBase = ast.literal_eval(buildFileBase.read())
            buildFileBase.close()
        except:
            buildDataBase = 0

        try:
            buildFileCurr = open(currBuildDir + "\\buildDetail.txt","r")
            buildDataCurr = ast.literal_eval(buildFileCurr.read())
            buildFileCurr.close()
        except:
            buildDataCurr = 0

        return render(request, 'compare/CompareData.html', {'baseBuildNumber': baseBuildNumber,
                                                            'currBuildNumber': currBuildNumber,
                                                            'summaryDataComp': summaryDataComp,
                                                            'aggReportComp': finalComparedData,
                                                            'currBuild': currBuildNumber,
                                                            'baseBuild': baseBuildNumber,
                                                            'base90centData': _90centDataBase,
                                                            'curr90centData': _90centDataCurr,
                                                            'baseErrorData': errDataBase,
                                                            'currErrorData': errDataCurr,
                                                            'baseMaxData': maxDataBase,
                                                            'currMaxData': maxDataCurr,
                                                            'buildDataBase': buildDataBase,
                                                            'buildDataCurr': buildDataCurr
                                                         })
    else:
        return HttpResponse("Baseline Load Test Data Is Not Present!")
