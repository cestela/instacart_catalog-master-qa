#!/bin/bash
#CHROME
pytest -v -s -m "regression" -n=3 --html=Reports/report_chrome.html --browser chrome
# pytest -v -s -m "sanity" -n=3 --html=Reports/report_chrome.html --browser chrome
# pytest -v -s -m "sanity or regression" -n=3 --html=Reports/report_chrome.html --browser chrome
# pytest -v -s -m "sanity and regression" -n=3 --html=Reports/report_chrome.html --browser chrome

#FIREFOX
pytest -v -s -m "regression" -n=3 --html=Reports/report_firefox.html --browser firefox
# pytest -v -s -m "sanity" -n=3 --html=Reports/report_firefox.html --browser firefox
# pytest -v -s -m "sanity or regression" -n=3 --html=Reports/report_firefox.html --browser firefox
# pytest -v -s -m "sanity and regression" -n=3 --html=Reports/report_firefox.html --browser firefox

