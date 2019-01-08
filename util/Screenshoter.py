import os
import shutil

from selenium import webdriver
from PIL import Image
from io import BytesIO

def getScreenshot(buildDir, completePath,):
    try:
        driver = webdriver.PhantomJS(executable_path=r'C:\Users\saurabhrai\Desktop\sso\learn\learnDjango\util\phantomjs.exe')
        driver.set_window_size(1024, 768)
        driver.get(completePath)
        driver.find_element_by_xpath("//*[@class='highcharts-legend-item']/*[text()='max']").click()
        driver.find_element_by_xpath("//*[@class='highcharts-legend-item']/*[text()='99%']").click()
        driver.find_element_by_xpath("//*[@class='highcharts-legend-item']/*[text()='95%']").click()

        element = driver.find_element_by_xpath("//*[@data-highcharts-chart='4']")
        location = element.location
        size = element.size
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        im.save(buildDir + "\\responsetimegraph.png")

        element = driver.find_element_by_xpath("//*[@data-highcharts-chart='5']")
        location = element.location
        size = element.size
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        im.save(buildDir + "\\reqpersec.png")

        driver.find_element_by_xpath("//*[@data-highcharts-chart='6']//*[@class='highcharts-legend-item']/*[text()='OK']").click()
        driver.find_element_by_xpath("//*[@data-highcharts-chart='6']//*[@class='highcharts-legend-item']/*[text()='All']").click()
        element = driver.find_element_by_xpath("//*[@data-highcharts-chart='6']")
        location = element.location
        size = element.size
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        im.save(buildDir + "\\failedresponsepersec.png")

        download(driver,"save_me.pdf")
        return "true"
    except Exception as ex:
        return str(ex)

def download(driver, target_path):
    def execute(script, args):
        driver.execute('executePhantomScript',
                       {'script': script, 'args': args})
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
    page_format = 'this.paperSize = {format: "tabloid", orientation: "portrait" };'
    execute(page_format, [])
    render = '''this.render("{}")'''.format(target_path)
    execute(render, [])

