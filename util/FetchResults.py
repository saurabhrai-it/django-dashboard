import ast
import re

import bs4 as bs
import urllib.request
from util import Result, Dataparser
from util.Constants import JENKINS_URL
from util.Constants import JENKINS_Job

jenkinsUrl = str(JENKINS_URL)
jenkinsJob = str(JENKINS_Job)


def fetch(buildDir, buildNumber, loadtestPurpose):
    simulation_name = str(getSimulationName(buildNumber))
    sourceCode = urllib.request.urlopen( jenkinsUrl +
                                        '/job/' + jenkinsJob + '/'
                                        + str(buildNumber) + '/gatling/'
                                        'report/' + simulation_name +
                                        '/source/index.html').read()
    soup = bs.BeautifulSoup(sourceCode,'html.parser')

    _90centData, maxData = Result.fetch90centMax(soup)
    errorGraphData = Result.fetchErrorGraph(soup)
    errorData = Result.fetchError(soup)
    userData = Result.fetchUserData(buildNumber, jenkinsJob, simulation_name)
    aggReport = Result.fetchAggData(buildDir, buildNumber, jenkinsJob, simulation_name)
    parsedErrorData = Dataparser.parseError(errorData)
    loadtestDetail = Result.getDetails(buildDir, buildNumber, jenkinsJob)

    file = open(buildDir + "\\loadtestPurpose.txt", "w+")
    file.write(str(loadtestPurpose))
    file.close()

    file = open(buildDir + "\\errorData.txt", "w+")
    file.write(str(errorData))
    file.close()

    file = open(buildDir + "\\errorGraphData.txt", "w+")
    file.write(str(errorGraphData))
    file.close()

    file = open(buildDir + "\\parsedErrorData.txt", "w+")
    file.write(str(parsedErrorData))
    file.close()

    file = open(buildDir + "\\_90cent.txt", "w+")
    file.write(str(_90centData))
    file.close()

    file = open(buildDir + "\\_maxData.txt", "w+")
    file.write(str(maxData))
    file.close()

    file = open(buildDir + "\\_userData.txt", "w+")
    file.write(str(userData))
    file.close()

    file = open(buildDir + "\\_aggReport.txt", "w+")
    file.write(str(aggReport))
    file.close()

    file = open(buildDir + "\\loadtestDetail.txt", "w+")
    file.write(str(loadtestDetail))
    file.close()


def getSimulationName(buildNumber):
    sourceCode = urllib.request.urlopen(jenkinsUrl + '/job/' + jenkinsJob + '/' + str(buildNumber) + '/').read()

    soup = bs.BeautifulSoup(sourceCode, 'lxml')
    pattern = re.compile("(?is)gatling/report/(.+?)\"")
    script = soup.find("body")
    if script:
        match = pattern.search(str(script))
        if match:
            return match.group(1)
    return "webservicesimulation"
