import os
import re
import ast
import urllib
import bs4 as bs
import json
import objectpath
from util.Constants import JENKINS_URL

jenkinsUrl = str(JENKINS_URL)

def fetch90centMax(soup):
    responseTimeGraphArray = []
    responseTimeGraphDate90cent = [[]]
    responseTimeGraphDateMax = [[]]

    pattern = re.compile("(?is)var responseTimePercentiles =.+?unpack\((.+?)\);")
    script = soup.find("script", text=pattern)
    if script:
        match = pattern.search(script.text)
        if match:
            responseTimeGraphArray = match.group(1)
            responseTimeGraphArray = responseTimeGraphArray.replace("null","[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]")
            responseTimeGraphArray = ast.literal_eval(responseTimeGraphArray)
    for i in responseTimeGraphArray:
        responseTimeGraphDate90cent.append([int(i[0])*1000-14400000, i[1][6]])
        responseTimeGraphDateMax.append([int(i[0])*1000-14400000, i[1][9]])
    responseTimeGraphDate90cent.pop(0); responseTimeGraphDateMax.pop(0);
    return responseTimeGraphDate90cent, responseTimeGraphDateMax

def fetchErrorGraph(soup):
    errorGraphArray = []
    errorGraph = [[]]

    pattern = re.compile("(?is)var container_responses = unpack\((.+?)\);")
    script = soup.find("script", text=pattern)
    if script:
        match = pattern.search(script.text)
        if match:
            errorGraphArray = match.group(1)
            errorGraphArray = ast.literal_eval(errorGraphArray)
    for i in errorGraphArray:
        errorGraph.append([int(i[0])*1000-14400000, i[1][1]])
    errorGraph.pop(0)
    return errorGraph

def fetchError(soup):
    errorArray = [[]]
    try:
        table = soup.find("table", attrs={'id':'container_errors'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            errorArray.append([cols[0].find(text=True), int(cols[1].find(text=True))])
        errorArray.pop(0)
    except:
        errorArray = [[]]
    return errorArray

def fetchUserData(buildNumber, jenkinsJob, simulation_name):

    sourceCode = urllib.request.urlopen(jenkinsUrl +
                                        '/job/' + jenkinsJob + '/'
                                        +str(buildNumber)+'/gatling/'
                                        'report/' + simulation_name + '/'
                                                          'source/js/all_sessions.js').read()
    soup = bs.BeautifulSoup(sourceCode, 'lxml')
    pattern = re.compile(r"(?is)data: \[.+?(\[.+?)\s")

    script = soup.find("p", text=pattern)
    if script:
        match = pattern.search(script.text)
        if match:
            userDataArray = match.group(1)
    return "["+userDataArray+"]"

def getDetails(buildDir, buildNumber, jenkinsJob):
    testDetails = {}
    try:
        sourceCode = urllib.request.urlopen(jenkinsUrl + '/job/' + jenkinsJob + '/'
                                            +str(buildNumber)+'/logText/progressiveHtml').read()
        soup = bs.BeautifulSoup(sourceCode, 'lxml')
        envPattern = re.compile(r"(?is)DwsStudentDashboardUrl=https://(.+?)-www\.cengage\.com")
        flowPattern = re.compile(r"(?is)web\.service\.entities=(.+?) -D")
        weightPattern = re.compile(r"(?is)gatling\.service\.entities\.weight=(.+?) -D")
        ec2CountPattern = re.compile(r"(?is)ec2\.instance\.count=(.+?) -D")
        userPattern = re.compile(r"(?is)gatling\.users=(.+?) -D")
        rampUpPattern = re.compile(r"(?is)gatling\.rampup\.sec=(.+?) -D")
        sustainPattern = re.compile(r"(?is)gatling\.sustain\.sec=(.+?) -D")
        rampDownPattern = re.compile(r"(?is)gatling\.rampdown\.sec=(.+?) -D")
        minDelayPattern = re.compile(r"(?is)gatling\.request\.minDelay\.ms=(.+?) -D")
        maxDelayPattern = re.compile(r"(?is)gatling\.request\.maxDelay\.ms=(.+?) -D")
        masterIpPattern = re.compile(r"(?is)IpAddress: (.+?)\s")
        slaveIpPattern = re.compile(r"(?is)host = (.+?)\s")

        envDetail = []
        flowDetail = []
        weightDetail = []
        ec2CountDetail = []
        userDetail = []
        rampUpDetail = []
        sustainDetail = []
        rampDownDetail = []
        minDelayDetail = []
        maxDelayDetail = []
        masterIpDetail = []
        slaveIpDetail = []
        script = soup.find("p")
        match = envPattern.search(script.text)
        if match:
            envDetail = match.group(1)
            loadtestenv = str(envDetail)
            build = buildDetail(loadtestenv)
            try:
                file = open(buildDir + "\\buildDetail.txt", "w+")
                file.write(str(build))
                file.close()
            except:
                pass


        match = flowPattern.search(script.text)
        if match:
            flowDetail = match.group(1)

        match = weightPattern.search(script.text)
        if match:
            weightDetail = match.group(1)

        match = ec2CountPattern.search(script.text)
        if match:
            ec2CountDetail = match.group(1)

        match = userPattern.search(script.text)
        if match:
            userDetail = match.group(1)

        match = rampUpPattern.search(script.text)
        if match:
            rampUpDetail = match.group(1)

        match = sustainPattern.search(script.text)
        if match:
            sustainDetail = match.group(1)

        match = rampDownPattern.search(script.text)
        if match:
            rampDownDetail = match.group(1)

        match = minDelayPattern.search(script.text)
        if match:
            minDelayDetail = match.group(1)

        match = maxDelayPattern.search(script.text)
        if match:
            maxDelayDetail = match.group(1)

        match = masterIpPattern.search(script.text)
        if match:
            masterIpDetail = match.group(1)

        match = slaveIpPattern.findall(script.text)
        if match:
            slaveIpDetail = match

        testDetails['Environment'] = envDetail
        scenario = flowDetail.split(',')
        throughput = weightDetail.split(',')
        testDetails['scn'] = [[]]
        for i in range(0,scenario.__len__()):
            testDetails['scn'].append([str(scenario[i]), str(throughput[i])])
        testDetails['scn'].pop(0)
        testDetails['MachineCount'] = ec2CountDetail
        testDetails['masterIp'] = masterIpDetail
        testDetails['slaveIp'] = slaveIpDetail
        testDetails['UserCount'] = int(ec2CountDetail)*int(userDetail)
        testDetails['RampUp'] = str(int(rampUpDetail)) + " sec"
        testDetails['RampDown'] = str(int(rampDownDetail)) + " sec"
        testDetails['SteadyState'] = str(int(sustainDetail) - int(rampUpDetail)) + " sec"
        testDetails['TestDuration'] = str(int(sustainDetail) + int(rampDownDetail)) + " sec"
        testDetails['MinDelay'] = str(int(int(minDelayDetail)/1000)) + " sec"
        testDetails['MaxDelay'] = str(int(int(maxDelayDetail)/1000)) + " sec"
    except:
        testDetails = {}
    return testDetails

def fetchAggData(buildDir, buildNumber, jenkinsJob, simulation_name):
    try:
        sourceCode = urllib.request.urlopen(jenkinsUrl +
                                            '/job/' + jenkinsJob + '/'
                                            +str(buildNumber)+'/gatling/'
                                            'report/' + simulation_name +
                                            '/source/js/stats.js').read()
        soup = bs.BeautifulSoup(sourceCode,'lxml')
        pattern = re.compile("(?is)var stats = (\{.+?)function")
        script = soup.find("p", text=pattern)

        aggDataArray = [[]]
        globalDataArray = [[]]
        summaryDataArray = [[]]
        if script:
            match = pattern.search(script.text)
            if match:
                file = open(buildDir + "\\allData.txt","w+",encoding="utf8")
                file.write(str(match.group(1)))
                file.close()
            with open(os.path.join(buildDir, "allData.txt"), 'r') as content_file:
                matchedData = str(match.group(1)).replace("type","\"type\"") \
                                                .replace("path","\"path\"").replace("stats","\"stats\"") \
                                                .replace("contents","\"contents\"")
                matchedData = matchedData.replace("\"path\"Formatted","\"pathFormatted\"")
                matchedData = re.sub(r"[^\"|^-]name","\"name\"",matchedData)
                file = open(buildDir + "\\jsonAllData.txt", "w+", encoding="utf8")
                file.write(matchedData)
                file.close()


            with open(os.path.join(buildDir, "jsonAllData.txt"), 'r') as content_file:
                aggDataJson = json.loads(content_file.read())
                json_tree = objectpath.Tree(aggDataJson)
                label = json_tree.execute("$.stats.name")
                total = int(json_tree.execute("$.stats.numberOfRequests.total"))
                mean = int(json_tree.execute("$.stats.meanResponseTime.total"))/1000
                _90cent = int(json_tree.execute("$.stats.percentiles3.total"))/1000
                min = int(json_tree.execute("$.stats.minResponseTime.total"))/1000
                max = int(json_tree.execute("$.stats.maxResponseTime.total"))/1000
                throughput = json_tree.execute("$.stats.meanNumberOfRequestsPerSecond.total")
                ok = int(json_tree.execute("$.stats.numberOfRequests.ok"))
                ko = int(json_tree.execute("$.stats.numberOfRequests.ko"))
                koCent = float("{0:.2f}".format((ko/total)*100))
                globalDataArray.append([label, total, mean, _90cent, min, max, throughput, koCent])
                summaryDataArray.append(['Total Request', total])
                summaryDataArray.append(['Total Passed Request', ok])
                summaryDataArray.append(['Total Failed Request', ko])
                summaryDataArray.append(['Average Hits per seconds', throughput])
                summaryDataArray.append(['Overall Mean Response Time', mean])
                summaryDataArray.append(['90% Mean Response Time', _90cent])
                summaryDataArray.append(['Error %', koCent])
                tempContent = json_tree.execute("$.contents")
                for entry in tempContent:
                    tempContent1 = json_tree.execute("$.contents['"+entry+"'].contents")
                    for entry1 in tempContent1:
                        label = json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.name")
                        total = int(json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.numberOfRequests.total"))
                        mean = int(json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.meanResponseTime.total"))/1000
                        _90cent = int(json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.percentiles3.total"))/1000
                        min = int(json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.minResponseTime.total"))/1000
                        max = int(json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.maxResponseTime.total"))/1000
                        throughput = json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.meanNumberOfRequestsPerSecond.total")
                        ko = float("{0:.2f}".format((int(json_tree.execute("$.contents['"+entry+"'].contents['"+entry1+"'].stats.numberOfRequests.ko"))/total)*100))
                        aggDataArray.append([label, total, mean, _90cent, min, max, throughput, ko])
                aggDataArray.pop(0)
                globalDataArray.pop(0)
                summaryDataArray.pop(0)
                file = open(buildDir + "\\globalData.txt", "w+", encoding="utf8")
                file.write(str(globalDataArray))
                file.close()
                file = open(buildDir + "\\summaryData.txt", "w+", encoding="utf8")
                file.write(str(summaryDataArray))
                file.close()
                os.remove(buildDir + "\\allData.txt")
    except:
        aggDataArray = [[]]
    return aggDataArray

def buildDetail(env):
    builddetail = {}

    if env == "perf" or env == "s":
        env = env + "-c"
    try:
        instReq = urllib.request.urlopen('https://' + str(env) + '-login.cengagebrain.com/ssoinstructor/version.htm').read()
        instSoup = bs.BeautifulSoup(instReq, 'lxml')
        instScript = instSoup.find("body")
        instBuildPattern = re.compile(r"<strong>([0-9\.]+)\s")
        match = instBuildPattern.search(str(instScript))
        if match:
            builddetail["Instructor"] = str(match.group(1))
    except Exception as e:
        builddetail["Instructor"] = str(e)

    try:
        studReq = urllib.request.urlopen('https://' + str(env) + '-login.cengagebrain.com/cb/version.htm').read()
        studSoup = bs.BeautifulSoup(studReq, 'lxml')
        studScript = studSoup.find("body")
        studBuildPattern = re.compile(r"Version Number : (.+?)<")
        match = studBuildPattern.search(str(studScript))
        if match:
            builddetail["Student"] = str(match.group(1))
    except Exception as e:
        builddetail["Student"] = str(e)

    try:
        olrReq = urllib.request.urlopen('https://' + str(env) + '-ws.cengage.com/olrws/OLRws').read()
        olrSoup = bs.BeautifulSoup(olrReq, 'lxml')
        olrScript = olrSoup.find("body")
        olrBuildPattern = re.compile(r"Implementation: (.+?)\s")
        match = olrBuildPattern.search(str(olrScript))
        if match:
            builddetail["OLRws"] = str(match.group(1))
    except Exception as e:
        builddetail["OLRws"] = str(e)

    try:
        ssoReq = urllib.request.urlopen('https://' + str(env) + '-ws.cengage.com/ssows/SSOws').read()
        ssoSoup = bs.BeautifulSoup(ssoReq, 'lxml')
        ssoScript = ssoSoup.find("body")
        ssoBuildPattern = re.compile(r"Implementation: (.+?)\s")
        match = ssoBuildPattern.search(str(ssoScript))
        if match:
            builddetail["SSOws"] = str(match.group(1))
    except Exception as e:
        builddetail["SSOws"] = str(e)

    try:
        RSReq = urllib.request.urlopen('https://' + str(env) + '-studentdashboard.cengagebrain.com/api/v1/health').read()
        RSSoup = bs.BeautifulSoup(RSReq, 'lxml')
        RSScript = RSSoup.find("body")
        RSBuildPattern = re.compile(r"\"resource-server\":\"(.+?)\"")
        match = RSBuildPattern.search(str(RSScript))
        if match:
            builddetail["RS"] = str(match.group(1))
    except Exception as e:
        builddetail["RS"] = str(e)

    try:
        uiReq = urllib.request.urlopen('https://' + str(env) + '-studentdashboard.cengagebrain.com/version').read()
        uiSoup = bs.BeautifulSoup(uiReq, 'lxml')
        uiScript = uiSoup.find("body")
        uiBuildPattern = re.compile(r"p>(.+?)<")
        match = uiBuildPattern.search(str(uiScript))
        if match:
            builddetail["UI"] = str(match.group(1))
    except Exception as e:
        builddetail["UI"] = str(e)

    return builddetail
