*** Settings ***
Library     Collections


*** Variables ***
@{list_name}    value1    value2    value3    value4
@{list}    1    2    3    4 
&{Dict}    name=sanjay    lastname=r


*** Keywords ***
List example 
    Append To List    ${list}    5 
    Log To Console    ${list}
    ${list2} =    Create List    3    2 
    ${list3}    Combine Lists     ${list}     ${list2}
    Log To Console    ${list3}
    ${string}    Set Variable    string 
    ${list4}    Convert To List    ${string}
    Log To Console    ${list4}
    #deepcopy
    ${list5}    Copy List    ${list4}
    Log To Console    ${list5}
    ${count_number}    Count Values In List    ${list3}    2 
    Log To Console    ${count_number}
    # get value based on index 
    ${value}  Get From List    ${list4}    3 
    Log To Console    ${value}
    ${index}    Get Index From List    ${list4}    2 
    Log To Console    index:${index}
    ${slice}    Get Slice From List     ${list4}    0    3
    Log To Console   ${slice}
    Insert Into List    ${list}    0    10
    Log To Console    ${list}
    #Lists Should Be Equal
    List Should Contain Sub List    ${list}    ${list3}
    List Should Contain Value    ${list}    2
    #List Should Not Contain Value
    #List Should Not Contain Duplicates
    Remove Duplicates    ${list4}
    Remove From List    ${list}    index=1
    Remove Values From List    ${list}    1   2   3
    Log To Console    ${list4}
    Log To Console    ${list}
    Set List Value    ${list}    0    11
    Sort List    ${list}
    Log To Console    ${list}
    Reverse List    ${list}
    Log To Console    ${list}

    
Dict example 
    #${dict}    Convert To Dictionary    ${list_name}
    ${dict1}    Copy Dictionary    ${dict}
    Dictionary Should Contain Item    ${dict1}    name    sanjay
    Dictionary Should Contain Key    ${dict1}    name
    Dictionary Should Contain Value    ${dict1}    sanjay 
    Dictionary Should Contain Sub Dictionary    ${dict1}    ${dict}

    Dictionary Should Not Contain Key     ${dict1}    name1
    Dictionary Should Not Contain Value     ${dict1}    name1
    
    ${dict_item}     Get Dictionary Items    ${dict1}
    Log To Console    ${dict_item}
    
    ${dict_keys}    Get Dictionary Keys    ${dict1}
    Log To Console    ${dict_keys}
    
    ${dict_values}    Get Dictionary Values    ${dict1}
    Log To Console    ${dict_values}
    
    ${dict_Value_based_index}    Get From Dictionary    ${dict1}    name
    Log To Console    name:${dict_Value_based_index}
    
    Keep In Dictionary    ${dict1}    name    lastname
    
    ${dict_after_pop}     Pop From Dictionary    ${dict1}    name 
    Log To Console    ${dict_after_pop}
    
    Set To Dictionary    ${dict1}    name=Sanjay 
    Log To Console    ${dict1}
    
    Remove From Dictionary    ${dict1}    name    lastname
    Log To Console    ${dict1}
*** Test Cases ***
Test List example 
    List Example
    
Test Dict example
    Dict Example

