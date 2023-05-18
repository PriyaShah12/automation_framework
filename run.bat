pytest ui_test/testCases/ -vs
pytest database/ -vs
pytest api_test/ -vs
rem pytest -v -s

rem pytest -v -s -m "sanity"