from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
from util import FetchResults, MailSender
import shutil
from util.Constants import URL

url = str(URL)

def index(request):
    return render(request, 'fetcher/GetTestDetail.html')


def savedata(request, buildNumber, loadtestPurpose):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.sep.join(dir_path.split(os.path.sep)[:-1])
    result_dir = os.path.join(base_dir, "Results")

    build_dir = os.path.join(result_dir, str(buildNumber))
    if os.path.isdir(build_dir):
        return HttpResponse("Result of build number : " + str(buildNumber) + " is already present.")
    else:
        try:
            os.mkdir(build_dir)
            FetchResults.fetch(result_dir, build_dir, buildNumber, loadtestPurpose.replace("+", " "))

            MailSender.send(build_dir, buildNumber)
            return HttpResponse("Result is saved successfully!!! "
                                "<a href='" + url + "/" + str(buildNumber) + "'>Click here</a> to view results for this build.")
        except Exception:
            shutil.rmtree(build_dir)
            return HttpResponse("Internal Error occured! " + Exception.args)


def saveBaselineBuild(request, buildNumber, baselineBuildNumber):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.sep.join(dir_path.split(os.path.sep)[:-1])
    result_dir = os.path.join(base_dir, "Results")

    build_dir = os.path.join(result_dir, str(buildNumber))
    if os.path.isdir(build_dir):
        fileBaseline = open(build_dir + "\\baselineFile.txt", "w+")
        fileBaseline.write(str(baselineBuildNumber))
        fileBaseline.close()
        return redirect(url + "/" + str(buildNumber))
    else:
        return HttpResponse("Internal Error occured!")