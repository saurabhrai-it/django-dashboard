
def parseError(errorData):
    try:
        parsedError = [[]]
        temp = 0
        for err in errorData:
            if "found nothing" in err[0] or "unexpectedly found" in err[0]:
                temp = temp + err[1]

        if temp != 0:
            parsedError.append(["Assertion Errors", temp])

        tempCounter = counter(errorData, "actually found 400")
        if tempCounter != 0:
            parsedError.append(["HTTP 400 (Bad Request)", tempCounter])

        tempCounter = counter(errorData, "actually found 404")
        if tempCounter != 0:
            parsedError.append(["HTTP 404 (Not Found)", tempCounter])

        tempCounter = counter(errorData, "actually found 408")
        if tempCounter != 0:
            parsedError.append(["HTTP 408 (Request Timeout)", tempCounter])

        tempCounter = counter(errorData, "actually found 500")
        if tempCounter != 0:
            parsedError.append(["HTTP 500 (Internal Server Error)", tempCounter])

        tempCounter = counter(errorData, "actually found 502")
        if tempCounter != 0:
            parsedError.append(["HTTP 502 (Bad Gateway)", tempCounter])

        tempCounter = counter(errorData, "actually found 503")
        if tempCounter != 0:
            parsedError.append(["HTTP 503 (Service Unavailable)", tempCounter])

        tempCounter = counter(errorData, "actually found 504")
        if tempCounter != 0:
            parsedError.append(["HTTP 504 (Gateway Timeout)", tempCounter])

        tempCounter = counter(errorData, "j.n.s.SSLException")
        if tempCounter != 0:
            parsedError.append(["j.n.s.SSLException", tempCounter])

        tempCounter = counter(errorData, "j.u.c.TimeoutException")
        if tempCounter != 0:
            parsedError.append(["j.u.c.TimeoutException", tempCounter])

        tempCounter = counter(errorData, "j.n.ConnectException")
        if tempCounter != 0:
            parsedError.append(["j.n.ConnectException", tempCounter])

        tempCounter = counter(errorData, "o.a.e.RemotelyClosedException")
        if tempCounter != 0:
            parsedError.append(["o.a.e.RemotelyClosedException", tempCounter])

        tempCounter = counter(errorData, "j.n.UnknownHostException")
        if tempCounter != 0:
            parsedError.append(["j.n.UnknownHostException", tempCounter])

        parsedError.pop(0)
    except:
        parsedError = [[]]
    return parsedError


def counter(errorData, errorString):
    temp1 = 0
    for err in errorData:
        if errorString in err[0]:
            temp1 = temp1 + err[1]
    return temp1
