#!/bin/bash
#CHROME
pytest -v -s -m "regression" --html=Reports/report_chrome.html --browser chrome
# pytest -v -s -m "sanity" --html=Reports/report_chrome.html --browser chrome
# pytest -v -s -m "sanity or regression" --html=Reports/report_chrome.html --browser chrome
# pytest -v -s -m "sanity and regression" -n= --html=Reports/report_chrome.html --browser chrome

#FIREFOX
pytest -v -s -m "regression" --html=Reports/report_firefox.html --browser firefox
# pytest -v -s -m "sanity" --html=Reports/report_firefox.html --browser firefox
# pytest -v -s -m "sanity or regression" --html=Reports/report_firefox.html --browser firefox
# pytest -v -s -m "sanity and regression" --html=Reports/report_firefox.html --browser firefox

