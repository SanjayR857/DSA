#ElementClickInterceptedException: not clicking
#ElementNotInteractableException:
#InvalidSelectorException: Message: invalid selector   in valid xpath
*** Settings ***
Library     SeleniumLibrary
Suite Setup    Open Browser    https://demo.automationtesting.in/Register.html    chrome

*** Variables ***

${url}     https://demo.automationtesting.in/Register.html


*** Keywords ***
Add Cookie example     
     Get Cookie
     Add Cookie
     Delete Cookie
     Delete All Cookies


alert handle example
    Mouse Over    //*[@id="header"]/nav/div/div[2]/ul/li[4]/a
    Sleep    2s
    Click Element    //*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[1]/a
    Sleep    1s
    Click Element    //*[@id="OKTab"]/button
    # it will default accept the alert   message check  action and timeout 
    Alert Should Be Present    text=I am an alert box!    action=dismiss     timeout=5

    # it will handle the alert and fails if its persent
    Alert Should Not Be Present
    Click Element    //*[text()='Alert with OK & Cancel ']
    Click Element    //*[@id="CancelTab"]/button
    # by default accept it
    Handle Alert    dismiss 
    Click Element    //*[text()='Alert with OK & Cancel ']
    Click Element    //*[@id="CancelTab"]/button
    #Leave alert open and get its message.
    Handle Alert    Leave
    Handle Alert

    # input text
    Click Element    //*[text()='Alert with Textbox ']
    Click Element    //*[@id="Textbox"]/button
    # input text and action
    Input Text Into Alert    sanjay


Click Element example
    Click Element    //*[@id="checkbox1"]
    Sleep    2s
    Scroll Element Into View      //*[@id="Button1"]
    Click Button     Submit
    Double Click Element    //*[@id="Button1"]
#    Click Image    //*[@id="imagetrgt"]
#    Click Link
#    Click Element At Coordinates      //*[@id="Button1"]    x=300     y=500


capture screenshot example 
    Capture Page Screenshot    filename
    Capture Element Screenshot      locator     filename

checkbox and radio btn example
    # checkbox
    Select Checkbox    //*[@id="checkbox1"]
    Checkbox Should Be Selected    //*[@id="checkbox1"]
    Unselect Checkbox    id:checkbox1
    Checkbox Should Not Be Selected    id:checkbox1
    # radio
    Radio Button Should Not Be Selected    radiooptions
    Select Radio Button    radiooptions    Male
    Radio Button Should Be Set To    radiooptions    Male


choose file example
    Choose File    locator=    filepath=
    #Overlapping UI elements: If an element is hidden behind a modal, popup, or another element, 
    #this keyword might be used to bring it into focus or handle the overlap.
    #Dynamic content loading: In modern web applications where content dynamically loads, sometimes elements are not interactable 
    #immediately. The Cover Element keyword could help address timing issues.
    Cover Element    locator=xpath


close browser example
    # it will close current browser
    Close Browser
    # close all the browser
    Close All Browsers
    # close current tab or window
    Close Window

frame example
    Mouse Over    //*[@id="header"]/nav/div/div[2]/ul/li[4]/a
    Sleep    2s
    Click Element    //a[text()='Frames']
    Select Frame    id:singleframe
    Current Frame Should Contain    iFrame Demo
    Current Frame Should Not Contain     Hi
    Input Text     (//input[1])    sanjay
    Unselect Frame
    Click Element    //a[normalize-space()='Iframe with in an Iframe']
    Select Frame    //*[@id="Multiple"]/iframe
    Select Frame    //div[@class='iframe-container']/iframe
    Input Text    (//input[1])    Test
    Frame Should Contain       //div[@class='iframe-container']/iframe    Nested Frame 


Element validation example
    Element Attribute Value Should Be    //*[@id="eid"]/input    type    email
    # when element is not interating
    #Element Should Be Disabled    //*[@id="eid"]/input
    Element Should Be Enabled    //*[@id="eid"]/input
    Element Should Not Be Visible     //*[@id="eid"]/input111111
    Element Should Be Visible    //*[@id="eid"]/input
    #Element Should Not Be Visible
    Set Focus To Element    //*[@id="eid"]/input
    Element Should Be Focused    //*[@id="eid"]/input
    Element Should Contain    (//div[contains(@class,'row')])[2]    Art Design
    Element Should Not Contain    (//div[contains(@class,'row')])[2]    Register
    Element Text Should Be    //*[@id="basicBootstrapForm"]/div[6]/div/div[1]/label    Cricket
    Element Text Should Not Be    //*[@id="basicBootstrapForm"]/div[6]/div/div[1]/label    124


javascript execution example  
    Execute Async Javascript    code=
    Execute Javascript    code=
    
page validation example 
    Page Should Contain    text=Register
    Page Should Contain Button    //*[@id="checkbox1"]
    Page Should Contain Checkbox    //*[@id="checkbox1"]
    Page Should Contain Element     //*[@id="checkbox1"]
    Page Should Contain Image    //*[@id="header"]/div/div/div/div[1]/a/img
    Page Should Contain Link    //*[@id="footer"]/div/div/div[2]/a[3]
    Page Should Contain List    //*[@id="Skills"]
    Page Should Contain Radio Button    radiooptions   
    Page Should Contain Textfield    //*[@id="basicBootstrapForm"]/div[1]/div[1]/input

    Page Should Not Contain    text=Register1
    Page Should Not Contain Button     //*[@id="basicBootstrapForm1"]
    Page Should Not Contain Checkbox     //*[@id="basicBootstrapForm1"]
    Page Should Not Contain Element     //*[@id="basicBootstrapForm1"]
    Page Should Not Contain List     //*[@id="basicBootstrapForm1"]
    Page Should Not Contain Image     //*[@id="basicBootstrapForm1"]
    Page Should Not Contain Link     //*[@id="basicBootstrapForm1"]
    Page Should Not Contain Radio Button     //*[@id="basicBootstrapForm1"]
    Page Should Not Contain Textfield     //*[@id="basicBootstrapForm1"]

    
wait validation example
    Set Selenium Implicit Wait    10s 
    ${wait}    Get Selenium Implicit Wait
    Log To Console    ${wait}
    Set Browser Implicit Wait    5s 
    ${wait1}     Get Selenium Implicit Wait
    Log To Console    ${wait1}
    Set Selenium Page Load Timeout    20s
    Set Selenium Speed   1
    Set Selenium Timeout    20s

    Wait For Condition	return jQuery.active == 0
    Wait For Expected Condition    xpath    value
    
    Wait Until Element Contains    xpath    text    timeout
    Wait Until Element Is Enabled
    Wait Until Element Is Visible

    Wait Until Element Does Not Contain
    Wait Until Element Is Not Visible

    #Waits until text appears on the current page.
    Wait Until Page Contains    text
    #Waits until the element locator appears on the current page.
    Wait Until Page Contains Element    xpath

    Wait Until Page Does Not Contain
    Wait Until Page Does Not Contain Element

    #Waits until the current URL  contains substring location location.
    Wait Until Location Contains
    #Waits until the current URL is expected.
    Wait Until Location Is

    Wait Until Location Does Not Contain
    Wait Until Location Is Not


dropdown validation example
    Select From List By Index    //*[@id="Skills"]    2
    Select From List By Value    //*[@id="country"]    Australia
    Select From List By Label    //*[@id="yearbox"]    1916
    Unselect From List By Index     //*[@id="Skills"]    2
    Unselect From List By Label     //*[@id="country"]    Australia
    Unselect From List By Value    //*[@id="yearbox"]    1916
    
    Select All From List    //*[@id="msdd"]
    Unselect All From List    //*[@id="msdd"]


Actions example
    Mouse Over    //*[@id="header"]/nav/div/div[2]/ul/li[4]/a
    Mouse Down    id:submitbtn
    Mouse Up      //a[normalize-space()='Home']
    Mouse Out     //a[normalize-space()='Home']
    Mouse Down On Image    //*[@id="imagetrgt"]
    Mouse Down On Link    //*[@id="footer"]/div/div/div[2]/a[1]
    Double Click Element
    Drag And Drop
    Drag And Drop By Offset
    #right click
    Open Context Menu    locator=

window example
    Maximize Browser Window
    Minimize Browser Window
    Set Window Position    500    500
    Set Window Size
    Switch Browser    New
    Switch Browser    Main
    Get Window Handles
    Get Window Identifiers
    Get Window Titles

browser example
    Open Browser    url=    brower=
    Go To    url=
    Reload Page
    Go Back
    Get Browser Aliases
    Get Browser Ids

Table example
    Get Table Cell
    Table Cell Should Contain
    Table Column Should Contain
    Table Row Should Contain
    Table Header Should Contain
    Table Should Contain
    
Text example 
    Clear Element Text    locator=
    Get Text    locator=
    Input Text    locator=    text=
    # used for mutl line input text
    Textarea Should Contain
    Textarea Value Should Be
    # used for single line input text
    Textfield Should Contain
    Textfield Value Should Be


get example
    #Returns a list containing ids of all links found in current page.
    ${list}=    Get All Links
    ${list2}=    Get Dom Attribute    //*[@id="basicBootstrapForm"]/div[1]/div[1]/input    type
    ${list3}=    Get Element Attribute    //*[@id="basicBootstrapForm"]/div[1]/div[1]/input     type
    Log To Console    ${list2}    ${list3}
    Get Element Count    //*[@id="basicBootstrapForm"]/div[1]/div[1]/input
    # locator width and height  it will return
    Get Element Size    //*[@id="basicBootstrapForm"]/div[1]/div[1]/input
    # return the all the labels or values in the selection drop dwon
    Get List Items
    Get Selected List Label    locotar
    Get Selected List Labels
    Get Selected List Value
    Get Selected List Values
    Get Text
    Get Title
    Get Value
    #Returns the first WebElement matching the given locator
    Get Webelement
    Get Webelements
    
*** Test Cases ***
Test Add Cookies 
    Add Cookie example

Test alert handle example
    alert handle example

Test element click example
    Click Element example

Test Capture SS example
    capture screenshot example

Test checkbox and radio example
    Checkbox And Radio Btn Example

Test choose file example 
    choose file example

Test frame example
    frame example

Test Element Validation example
    Element validation example

Test javascript execution example 
    javascript execution example 

Test page validation example 
    page validation example 

Test Wait valifdation example
    wait validation example

Test dropdown validation example 
    dropdown validation example 

Test Actions example
    Actions example

Test window example
    window example

Test browser example
    browser example

Test Table example
    Table example

Test Text example 
    Text example 
    
Test Get example 
    get example 
    
Test close browser example
    close browser example

