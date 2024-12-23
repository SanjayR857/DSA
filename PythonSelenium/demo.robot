*** Settings ***
Library     SeleniumLibrary
Library     PDF.py



*** Variables ***




*** Keywords ***
Open Website
    Open Browser    https://us.idec.com/idec-us/en/USD/medias/IDEC-FC6A-Microsmart-PLUS-CPU-Sales-Brochure.pdf?context=bWFzdGVyfGRvY3VtZW50c3w5MjM3OTk0fGFwcGxpY2F0aW9uL3BkZnxkb2N1bWVudHMvaGU2L2gyMy85MTUxMzM1ODkwOTc0LnBkZnxjMGExNGYzZDhkNjc4YjdlZDE0YzExYjYwOTk1ZTRkN2Y1ZDkzNjhjMDQzYmUyODAwNmM2ZjExNjU3ZDlmNjFk     chrome
    Sleep    1s
    Pdf Download Using Python
    Log To Console    Bye

*** Test Cases ***

Test 1
    Open Website
