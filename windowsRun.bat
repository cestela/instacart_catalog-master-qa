rem CHROME
pytest -v -s -m "regression" --html=Reports/report_chrome.html --browser chrome
rem pytest -v -s -m "sanity" --html=Reports/report_chrome.html --browser chrome
rem pytest -v -s -m "sanity or regression" --html=Reports/report_chrome.html --browser chrome
rem pytest -v -s -m "sanity and regression"  --html=Reports/report_chrome.html --browser chrome

rem FIREFOX
pytest -v -s -m "regression" --html=Reports/report_firefox.html --browser firefox
rem pytest -v -s -m "sanity" --html=Reports/report_firefox.html --browser firefox
rem pytest -v -s -m "sanity or regression"  --html=Reports/report_firefox.html --browser firefox
rem pytest -v -s -m "sanity and regression"  --html=Reports/report_firefox.html --browser firefox