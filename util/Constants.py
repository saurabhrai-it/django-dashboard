import configparser

config = configparser.ConfigParser()
config.read('util\\config.ini')

URL = config.get('server', 'localurl')
JENKINS_URL = config.get('server', 'jenkins')
JENKINS_Job = config.get('server', 'jenkinsjob')

load_generating_tool = "Gatling 2.3.1"

spaceBtwTable = """
<br/>
<br/>
"""

def purposeOfTest(testPurpose):

    try:
        purposeMail = """
    <ul style="margin-top:0in" type="disc">
	    <li style="text-autospace:none">
            <b>
                <span style="color:black">Purpose of load test:</span>
            </b>
		    """ + testPurpose + """
	    </li>
    </ul>    
    """
    except Exception as ex:
        purposeMail = str(ex)

    return purposeMail


def sectohourandminute(timestring):
    splitstring = timestring.split(" ")
    timeinsec = int(splitstring[0])
    timeinhour = int(timeinsec / 3600)

    timeinminute = 0
    timeleftinsec = 0
    remaindertime = timeinsec % 3600

    if remaindertime != 0:
        timeinminute = int(remaindertime / 60)

        if (remaindertime % 60) != 0:
            timeleftinsec = remaindertime % 60

    strTime = str(timeinhour) + " hour"
    if timeinminute != 0:
        strTime = strTime + " " + str(timeinminute) + " minutes"
    if timeleftinsec != 0:
        strTime = strTime + " " + str(timeleftinsec) + " seconds"
    return strTime


def machineConfigTemplate(data):

    tableStart = """
    <table style="width:312.35pt;border-collapse:collapse" border="0" cellpadding="0" cellspacing="0" width="0">
        <tbody>
            <tr style="height:16.0pt">
                <td colspan="2" style="width:312.35pt;border:solid windowtext 1.0pt;background:#a4a4a4;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt" valign="bottom" width="416">
                    <p style="text-align:center;text-autospace:none" align="center">
                        <b><span style="color:black">Load Test Machine Configuration</span></b>
                        <u></u><u></u>
                    </p>
                </td>
            </tr>
            <tr style="height:10.65pt">
                <td style="width:155.7pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:10.65pt" width="208">
                    <p style="text-align:center;text-autospace:none" align="center">
                        <b><span style="color:black">Type</span></b><u></u><u></u>
                    </p>
                </td>
                    <td style="width:156.65pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:10.65pt" valign="bottom" width="209">
                    <p style="text-align:center;text-autospace:none" align="center"><b><span style="color:black">IP</span></b><u></u><u></u></p>
                </td>
            </tr>
    """

    config_master_temp = ""
    config_slave_temp = ""

    if len(data["masterIp"]) != 0:
        masterIp = str(data["masterIp"])
        config_master_temp = """
            <tr style="height:10.65pt">
                <td style="width:155.7pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:10.65pt" valign="top" width="208">
                    <p style="text-align:center" align="center">master<u></u><u></u></p>
                </td>
                <td style="width:156.65pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:10.65pt" valign="top" width="209">
                    <p class="MsoNormal" style="text-align:center" align="center">""" + masterIp + """<u></u><u></u></p>
                </td>
            </tr>"""
    if len(data["slaveIp"]) != 0:
        for slave in data["slaveIp"]:
            config_slave_temp = config_slave_temp + """
            <tr style="height:10.25pt">
                <td style="width:155.7pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:10.25pt" valign="top" width="208">
                    <p class="MsoNormal" style="text-align:center" align="center">slave<u></u><u></u></p>
                </td>
                <td style="width:156.65pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:10.25pt" valign="top" width="209">
                    <p class="MsoNormal" style="text-align:center" align="center">""" + str(slave) + """<u></u><u></u></p>
                </td>
            </tr>
            """

    tableEnd = """    </tbody>
    </table>
    """

    return tableStart + config_master_temp + config_slave_temp + tableEnd


def testParamTemplate(data, st, ed):
    tableStart = """
    <table style="width:311.5pt;border-collapse:collapse" border="0" cellpadding="0" cellspacing="0" width="0">
        <tbody>
            <tr style="height:12.2pt">
                <td colspan="2" style="width:311.5pt;border:solid windowtext 1.0pt;background:#a4a4a4;padding:0cm 5.4pt 0cm 5.4pt;height:12.2pt" valign="bottom" width="415">
                    <p style="text-align:center;text-autospace:none" align="center">
                        <b><span style="color:black">Load Test Run – Parameters</span></b><u></u><u></u>
                    </p>
                </td>
            </tr>
    """
    try:
        userCount = str(data["UserCount"])
        rampUp = sectohourandminute(str(data["RampUp"]))
        steadyState = sectohourandminute(str(data["SteadyState"]))
        thinkTime = str(data["MinDelay"]) + "-" + str(data["MaxDelay"])
        totalDuration = sectohourandminute(str(data["TestDuration"]))

        maindata = """
            <tr style="height:8.1pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:8.1pt" width="207">
                    <p style="text-autospace:none"><span style="color:black">Maximum Running users</span><u></u><u></u></p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:8.1pt" valign="bottom" width="208">
                    <span style="color:black">""" + userCount + """ users</span><u></u><u></u>
                </td>
            </tr>
            <tr style="height:8.1pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:8.1pt" width="207">
                    <p style="text-autospace:none"><span style="color:black">Ramp Up Time</span><u></u><u></u></p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:8.1pt" valign="bottom" width="208">
                    <p>""" + str(rampUp) + """<u></u><u></u></p>
                </td>
            </tr>
            <tr style="height:12.7pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" width="207">
                    <p style="text-autospace:none"><span style="color:black">Steady State</span><u></u><u></u></p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" valign="bottom" width="208">
                    <span style="color:black">""" + str(steadyState) + """</span><u></u><u></u>
                </td>
            </tr>
            <tr style="height:12.7pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" width="207">
                    <p style="text-autospace:none"><span style="color:black">Think Time</span><u></u><u></u></p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" valign="bottom" width="208">
                    <p><span style="color:black">""" + str(thinkTime) + """</span><u></u><u></u></p>
                </td>
            </tr>
            <tr style="height:3.4pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:3.4pt" width="207">
                    <p style="text-autospace:none"><span style="color:black">Total duration</span><u></u><u></u></p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:3.4pt" valign="bottom" width="208">
                    <span style="color:black">""" + str(totalDuration) + """</span><u></u><u></u></p>
                </td>
            </tr>
            <tr style="height:4.45pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:4.45pt" width="207">
                    <p class="m_-7512363272757720309xmsonormal" style="text-autospace:none">
                        <span style="color:black">Start Time:<u></u><u></u></span>
                    </p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:4.45pt" valign="bottom" width="208">
                <p><span style="color:black">""" + str(st.strftime('%I:%M:%S %p')) + """</span></p>
                </td>
            </tr>
            <tr style="height:4.45pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:4.45pt" width="207">
                    <p class="m_-7512363272757720309xmsonormal" style="text-autospace:none">
                        <span style="color:black">End Time:<u></u><u></u></span>
                    </p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:4.45pt" valign="bottom" width="208">
                <p><span style="color:black">""" + str(ed.strftime('%I:%M:%S %p')) + """</span></p>
                </td>
            </tr>
            <tr style="height:12.7pt">
                <td style="width:155.45pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" width="207">
                    <p style="text-autospace:none">
                        <span style="color:black">Tool used <u></u><u></u></span>
                    </p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" valign="bottom" width="208">
                    <p><span style="color:black">""" + load_generating_tool + """<u></u><u></u></span></p>
                </td>
            </tr>
        """
    except Exception as e:
        maindata = str(e)

    tableEnd = """</tbody>
    </table>
    """

    return tableStart + maindata + tableEnd


def summaryTemplate(data):
    tableStart = """
    <table style="width:311.65pt;border-collapse:collapse" border="0" cellpadding="0" cellspacing="0" width="0">
        <tbody>
            <tr style="height:12.7pt">
                <td colspan="2" style="width:311.65pt;border:solid windowtext 1.0pt;background:#a4a4a4;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" width="416">
                    <p style="text-align:center;text-autospace:none" align="center"><b><span style="color:black">Summary</span></b><u></u><u></u></p>
                </td>
            </tr>
    """
    try:
        summarydata = ""
        for key in data:
            summarydata = summarydata + """
            <tr style="height:12.7pt">
                <td style="width:155.6pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" width="207">
                    <p style="text-autospace:none"><span style="color:black">""" + str(key[0]) + """<u></u><u></u></span></p>
                </td>
                <td style="width:156.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" valign="bottom" width="208">
                    <p style="text-align:center" align="center">""" + str(key[1]) + """<span style="color:black"><u></u><u></u></span></p>
                </td>
            </tr>
        """
    except Exception as e:
        summarydata = str(e)

    tableEnd = """</tbody>
    </table>
    """

    return tableStart + summarydata + tableEnd


def errorTemplate(data):
    tableStart = """
    <table style="width:311.65pt;border-collapse:collapse" border="0" cellpadding="0" cellspacing="0" width="0">
        <tbody>
            <tr style="height:11.5pt">
                <td colspan="2" style="width:311.65pt;border:solid windowtext 1.0pt;background:#a4a4a4;padding:0cm 0cm 0cm 0cm;height:11.5pt" valign="top" width="416">
                    <p style="text-align:center;text-autospace:none" align="center"><b><span style="color:black">Error List</span></b><u></u><u></u></p>
                </td>
            </tr>
            <tr style="height:7.6pt">
                <td style="width:233.6pt;border:solid windowtext 1.0pt;border-top:none;background:#d9d9d9;padding:0cm 5.4pt 0cm 5.4pt;height:7.6pt" width="311">
                    <p style="text-align:center;text-autospace:none" align="center"><b><span style="color:black">Error Type</span><u></u><u></u></b></p>
                </td>
                <td style="width:78.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#d9d9d9;padding:0cm 0cm 0cm 0cm;height:7.6pt" valign="top" width="104">
                    <p style="text-align:center" align="center"><b><span style="color:black">Error Count</span><u></u><u></u></b></p>
                </td>
            </tr>
    """
    try:
        errordata = ""
        for item in data:
            errordata = errordata + """
            <tr style="height:12.05pt">
                <td style="width:233.6pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:12.05pt" valign="top" width="311">
                    <p>""" + str(item[0]) + """<u></u><u></u></p>
                </td>
                <td style="width:78.05pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 0cm 0cm 0cm;height:12.05pt" valign="top" width="104">
                    <p style="text-align:center" align="center">""" + str(item[1]) + """<u></u><u></u></p>
                </td>
            </tr>
        """
    except Exception as e:
        errordata = str(e)

    tableEnd = """</tbody>
    </table>
    """

    return tableStart + errordata + tableEnd


def buildServerTemplate(data):
    tableStart = """
    <table style="width:311.15pt;border-collapse:collapse" border="0" cellpadding="0" cellspacing="0" width="0">
        <tbody>
            <tr style="height:12.2pt">
                <td colspan="2" style="width:311.15pt;border:solid windowtext 1.0pt;background:#a4a4a4;padding:0cm 5.4pt 0cm 5.4pt;height:12.2pt" valign="bottom" width="415">
                    <p style="text-align:center;text-autospace:none" align="center"><b><span style="color:black">Build Versions</span></b><u></u><u></u></p>
                </td>
            </tr>
    """
    try:
        buildData = ""
        for key, value in data.items():
            buildData = buildData + """
            <tr style="height:12.7pt">
                <td style="width:155.3pt;border:solid windowtext 1.0pt;border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" width="207">
                    <p style="text-autospace:none"><span style="color:black">"""+str(key)+"""</span><u></u><u></u></p>
                </td>
                <td style="width:155.85pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:12.7pt" valign="bottom" width="208">
                    <p><span style="color:black">"""+str(value)+"""</span><u></u><u></u></p>
                </td>
            </tr>
        """
    except Exception as e:
        buildData = str(e)

    tableEnd = """</tbody>
    </table>
    """

    return tableStart + buildData + tableEnd


def flowsTemplate(data):
    tableStart = """
    <table style="width:413.6pt;border-collapse:collapse" border="0" cellpadding="0" cellspacing="0" width="0">
        <tbody>
            <tr style="height:12.05pt">
                <td colspan="2" style="width:413.6pt;border:solid windowtext 1.0pt;background:#a4a4a4;padding:0cm 0cm 0cm 0cm;height:12.05pt" valign="top" width="551">
                    <p style="text-align:center;text-autospace:none" align="center"><b><span style="color:black">User distribution</span></b><u></u><u></u></p>
                </td>
            </tr>
            <tr style="height:8.0pt">
                <td style="width:243.0pt;border:solid windowtext 1.0pt;background:#d9d9d9;padding:0cm 5.4pt 0cm 5.4pt;height:8.0pt" width="324">
                    <p style="text-align:center;text-autospace:none" align="center"><b><span style="color:black">Workflow Name</span></b><u></u><u></u></p>
                </td>
                <td style="width:108.0pt;border:solid windowtext 1.0pt;background:#d9d9d9;padding:0cm 0cm 0cm 0cm;height:8.0pt" valign="top" width="144">
                    <p style="text-align:center" align="center"><b><span style="color:black">%Distribution</span></b><u></u><u></u></p>
                </td>
            </tr>
    """
    try:
        flowData = ""
        for scenario in data["scn"]:
            flowData = flowData + """
            <tr>
                <td style="width:243.0pt;border:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:8.0pt" width="324">
                    <p style="text-autospace:none"><span style="color:black">"""+str(scenario[0])+"""</span><u></u><u></u></p>
                </td>
                <td style="width:108.0pt;border:solid windowtext 1.0pt;padding:0cm 0cm 0cm 0cm;height:8.0pt" valign="bottom" width="144">
                    <p style="text-align:center;text-autospace:none" align="center">"""+str(scenario[1])+"""<u></u><u></u></p>
                </td>
            </tr>
        """
    except Exception as e:
        flowData = str(e)

    tableEnd = """</tbody>
    </table>
    """

    return tableStart + flowData + tableEnd


def startPoint():
    try:
        pointer = """
    <span style="font-family:Symbol;color:black">
        <span><b>·</b>
            <span style="font:7.0pt &quot;Times New Roman&quot;">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
            </span>
        </span>
    </span>
    <u></u>
    """
    except Exception as ex:
        pointer = str(ex)

    return pointer


def instructorLogin(data):
    try:
        instloginline = startPoint() + """
    <span lang="EN-US" style="color:black">
        Mean response time for returning instructor lands on dashboard is <b>""" + str(data) + """.</b>
    </span>
    <u></u><u></u>
    """
    except Exception as ex:
        instloginline = str(ex)

    return instloginline


def studentLogin(data):
    try:
        studloginline = startPoint() + """
    <span lang="EN-US" style="color:black">
        Mean response time for returning student lands on dashboard(“Student Login”) is <b>""" + str(data) + """.</b>
    </span>
    <u></u><u></u>
    """
    except Exception as ex:
        studloginline = str(ex)

    return studloginline


def new_student_created(data):
    try:
        stud_created = startPoint() + """
    <span lang="EN-US" style="color:black">
        <b>""" + str(data) + """</b> new student accounts were created using Course key URL.
    </span>
    <u></u><u></u>
    """
    except Exception as ex:
        stud_created = str(ex)

    return stud_created


def new_student_created_response_time(data):
    try:
        new_student_created = startPoint() + """
    <span lang="EN-US" style="color:black">
       Mean response time for new student following registration with course key lands on dashboard(“CU_10_02_EnterCompleteDetails”) is <b>""" + str(data) + """.</b>
    </span>
    <u></u><u></u>
    """
    except Exception as ex:
        new_student_created = str(ex)

    return new_student_created


def meanTime(data):
    try:
        meanMail = startPoint() + """
    <span lang="EN-US" style="color:black">
       Overall mean response time – <b>""" + str(data) + """ sec.</b>
    </span>
    <u></u><u></u>
    """

    except Exception as ex:
        meanMail = str(ex)

    return meanMail


def errorPercent(data):
    try:
        errorCentMail = startPoint() + """
    <span lang="EN-US" style="color:black">
       Overall Error % – <b>""" + str(data) + """%.</b>
    </span>
    <u></u><u></u>
    """

    except Exception as ex:
        errorCentMail = str(ex)

    return errorCentMail


def pdfReport(data):
    try:
        pdfReportMail = startPoint() + """
    <span lang="EN-US" style="color:black">
       Detailed report attached  <b>CARES-SSO_""" + str(data) + """</b> contains summary for all the transactions and graphs.
    </span>
    <u></u><u></u>
    """
    except Exception as ex:
        pdfReportMail = str(ex)
    return pdfReportMail


def jenkinsBuildNumber(data):
    try:
        buildNumberMail = startPoint() + """
    <span lang="EN-US" style="color:black">
       <span lang=EN-US style='color:black'>Jenkins Build Number : </span><span class=MsoHyperlink><span style='color:windowtext;text-decoration:none'><a href="http://10.160.20.242:8000/""" + str(data) + """">""" + str(data) + """</a>.</span></span>
    </span>
    <u></u><u></u>
    """
    except Exception as ex:
        buildNumberMail = str(ex)
    return buildNumberMail


def student_login_courseurl_response_time(data):
    try:
        stud_login_courseurl = startPoint() + """<span lang="EN-US" style="color:black">Mean response time for new student following registration with course key lands on dashboard(“CU_10_02_EnterCompleteDetails”) is <b>""" + str(data) + """.</b></span><u></u><u></u>"""

    except Exception as ex:
        stud_login_courseurl = str(ex)

    return stud_login_courseurl


def startMail(data):
    try:
        starter = \
        """<span lang="EN-US" style="color:black">Hi All,<br><br>
            Below is the summary of """ + str(data) + """</span><u></u><u></u>"""

    except Exception as ex:
        starter = str(ex)

    return starter


# def transactionSLA(data):
#     if not data:
#         return ""
#     transactionline = startPoint() + """
#
#     """
#     return transactionline