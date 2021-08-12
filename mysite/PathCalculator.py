from selenium import webdriver
from time import sleep


def find(source_location, destination, sourceLocation, targetLocation, shortestRouteTitle, shortestRouteDistance):
    chrome = webdriver.Chrome()
    sleep(2)
    source_location = source_location
    chrome.get("https://www.google.com/maps/dir/" + source_location)
    minDistance = 10000
    minIndex = 0
    routeTitleCol = []
    sleep(5)
    targetLocationInput = chrome.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input')
    targetLocationInput.send_keys(destination)
    sleep(5)
    searchButton = chrome.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]')
    searchButton.click()
    sleep(5)
    routes = chrome.find_elements_by_class_name('section-directions-trip-title')
    routes_distances = chrome.find_elements_by_class_name('section-directions-trip-distance')
    while len(routes) == 0:
        routes = chrome.find_elements_by_class_name('section-directions-trip-title')
        routes_distances = chrome.find_elements_by_class_name('section-directions-trip-distance')
    for routeTitle in routes:
        routeTitleText = routeTitle.text
        if routeTitleText != '':
            routeTitleCol.append(routeTitleText)
    count = 0
    for routeDistance in routes_distances:
        routeDistanceText = routeDistance.text.replace('km', '')
        routeDistanceText = routeDistanceText.replace('كم', '')
        routeDistanceText = routeDistanceText.replace('m', '')
        routeDistanceInKM = routeDistanceText.replace('م', '')
        if routeDistanceInKM == '':
            routeDistanceInKM = '10000'
        minRouteDistance = float(routeDistanceInKM.strip())
        if minRouteDistance < minDistance:
            minDistance = minRouteDistance
            minIndex = count
        count = count + 1
    sourceLocation.append(source_location)
    targetLocation.append(destination)
    shortestRouteDistance.append(minDistance)
    shortestRouteTitle.append(routeTitleCol[minIndex])
    dict_result = {"sourceLocation": sourceLocation, "targetLocation": targetLocation,
                   "shortestRouteDistance": shortestRouteDistance, "shortestRouteTitle": shortestRouteTitle}
    chrome.quit()
    return dict_result
