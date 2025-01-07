*** Settings ***
Library    String

*** Keywords ***
string example 
    ${string_value1}    Set Variable    String123
    ${lower_Case}     Convert To Lower Case    ${string_value1}
    Log To Console    ${lower_Case}
    ${upper_case}    Convert To Upper Case    ${string_value1}
    Log To Console    ${upper_case}
    ${titl_case}    Convert To Title Case    ${string_value1}
    Log To Console    ${titl_case}
    ${random_string}    Generate Random String    10     char 
    Log To Console    ${random_string}
    ${string_line}    Set Variable    sanjay\nvikas\nvarun
    Log To Console    ${string_line}
    ${line}    Get Line    ${string_line}    2 
    Log To Console    line:${line}
    ${lines}    Get Line Count    ${string_line}
    Log To Console    number of line count:${lines}
    ${list_split}    Split String    ${string_line}    \n 
    Log To Console    ${list_split}
    ${list_line}    Split To Lines    ${string_line}
    Log To Console    ${list_line}
    ${char_split}    Split String To Characters    ${string_line}
    Log To Console    ${char_split}
    ${string_line}       Replace String    ${string_line}    sanjay     san
    Log To Console    ${string_line}
    ${string_line}       Remove String        ${string_line}     san
    Log To Console    ${string_line}
    ${strip1}    Set Variable    111    2222
    ${strip_var}    Strip String    ${strip1}    mode=left
    Should Be String
    Should Not Be String
    Should Be Upper Case
    Should Be Lower Case
    Should Be Title Case


*** Test Cases ***
Test String example 
    string example 
    