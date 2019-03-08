import os
import ast

dir_path = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.sep.join(dir_path.split(os.path.sep)[:-1])
result_dir = os.path.join(base_dir, "Results")
allResultBuildNumber = os.listdir(result_dir+"\\")

histogramRequestFile = open(result_dir + "\\reqCountHisto.txt","w+")
try:
    histoReqData = ast.literal_eval(histogramRequestFile.read())
except:
    histoReqData = []
for i in allResultBuildNumber:

    try:
        summaryFile = open(result_dir + "\\" + i + "\\summaryData.txt","r")
        summaryFileData = ast.literal_eval(summaryFile.read())
        summaryFile.close()

        userFile = open(result_dir + "\\" + i + "\\_userData.txt","r")
        userStartData = ast.literal_eval(userFile.read())
        userFile.close()

        histoReqData.append([userStartData[0][0], summaryFileData[0][1], summaryFileData[1][1], summaryFileData[2][1], int(i)])
    except Exception as e:
        print(e)

histogramRequestFile.write(str(histoReqData))
histogramRequestFile.close()

