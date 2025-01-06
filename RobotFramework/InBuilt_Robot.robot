*** Settings ***

*** Variables ***
# comment
@{list} =    1      2     3     4
#${user}=    Create Dictionary    name=name1    age=12    city=ben


*** Keywords ***
Continue for loop example
    # continue for loop used to skip if condition met
    FOR    ${i}    IN     @{list}
        Run Keyword If    ${i}==2    Continue For Loop
        Log To Console    ${i}
    END
    # contnue for loop if will skip if cont is true
    FOR    ${i}     IN    @{list}
    Continue For Loop If    ${i}==3
    Log To Console    ${i}
    END


Exit for loop example 
    # this keyword used to exit for loop when condition met 
    FOR   ${i}    IN    @{list}
        Run Keyword If    ${i}==2    Exit For Loop
        Log To Console    ${i}
    END
    FOR  ${i}    IN    @{list}
        Exit For Loop If    ${i}==1
        Log To Console    ${i}
    END


Converting Values in Robot example 
    # set local variable  which is used to create value keyword and that cont be accessed outside the keyword  
    Set Local Variable    ${local_variable}    4
    ${binary}    Convert To Binary    ${local_variable}
    Log To Console    binary ${binary}
    # it will convert float to number
    ${number}     Convert To Number    ${binary}
    Log To Console    number ${number}
    ${boolean}    Convert To Boolean    ${number}
    Log To Console    boolean ${boolean}
    ${string}  Convert To String    ${boolean}
    Log To Console    string ${string}

       
Create Dictionary example
    &{user}    Create Dictionary    name=sanjay    age=12    city=bengaluru
    # calling the dict based on keys
    Log To Console    name1: ${user.name} name2: ${user.age}
    # calling the dit based on keys 
    Log To Console    nam1 ${user['name']}
    Log To Console    ${user}

    FOR     ${key}    ${Value}  IN  &{user}
        Log To Console    ${key}:${Value}
    END


Create List example
    ${list}  Create List    a   b   c    d
    FOR    ${i}    IN    @{list}
        Log To Console    ${i}
    END
    Log To Console    ${list}


Evaluate example
    # Evaluates the given expression in Python and returns the result
    ${bool}  Evaluate    0<10
    Log To Console   0<10 ${bool}
    ${add}  Evaluate    1+3
    Log To Console    add 1+3: ${add}
    ${list1}    Evaluate    list(int(x) for x in @{list})
    Log To Console    list ${list1}


Fail and Fatal Error Example 
    ${var}     Set Variable    1
    #Fails the test with the given message and optionally alters its tags
    Run Keyword If    ${var}==2     Fail    Message 
    Log To Console    Hello
    #Stops the whole test execution. The test or suite where this keyword is used fails with the provided
    #Possible teardowns will nevertheless be executed
    Run Keyword If    ${var}==2     Fatal Error    Message


Get Methods Examples
    Set Local Variable    ${name}    sanjay
    # Returns and logs how many times
    ${count}    Get Count    ${name}    a 
    Log To Console   a: count ${count}
    #Returns and logs the length of the given item as an integer
    ${length}    Get Length    ${name}
    Log To Console    lenght ${name} is ${length}
    #Verifies that the length of the given item is correct
    Length Should Be    ${name}    6    length is greater than 6
    #Returns the currently active instance of the specified library
    ${time}   Get Time    
    Log To Console    time: ${time}
    ${year}     ${month}     ${day}    Get Time     year,month,day
    Log To Console    year: ${year} month: ${month} day: ${day}
    #Returns variable value or ``default`` if the variable does not exist
    ${var_name}  Get Variable Value    ${name}
    ${var_name2}  Get Variable Value    ${name1}    23
    ${var_name3}  Get Variable Value    ${name2}
    Log To Console    var name : ${name}
    Log To Console    var name2: ${var_name2}
    Log To Console    var name3: ${var_name3}
    #Returns a dictionary containing all variables in the current scope
    ${list2} =    Get Variables
    #Log To Console    ${list2}
    
 
Import example
    #Imports a library with the given name and optional arguments     
    Import Library    path     arg
    #Imports a resource file with the given path
    Import Resource    path
    #Imports a variable file with the given path and optional arguments
    Import Variables    path   arg


Log example
    # Logs the given message to the console
    Log To Console    Hi there
    # Logs the given message with the given level
    Log    hi there
    #Logs the given messages as separate entries using the INFO level [list dict]
    Log Many    hi there
    # logs the all the given variables in the suite
    Log Variables
    Reset Log Level


Pass Execution example 
     ${var}  Set Variable    3
     #Skips rest of the current test, setup, or teardown with PASS status
     #When used in any setup or teardown (suite, test or keyword), passes that setup or teardown. Possible keyword teardowns of the started keywords are executed. Does not affect execution or statuses otherwise. - When used in a test outside setup or teardown, passes that particular test case. Possible test and keyword teardowns are executed.
     #Pass Execution If    cond
     Run Keyword If    ${var}==3    Pass Execution    done
     Log To Console    ${var}
     Remove Tags    tagname

Run Keywords examples
    #Return From Keyword is used in the for loop to return the value and exit the loop and return from the keyword
    FOR    ${i}    IN RANGE    0    4    1
    #Run Keyword If  ${number} % 2 == 0  Return From Keyword  Even
    #Run Keyword If  ${number} % 2 != 0  Return From Keyword  Odd
    #Return From Keyword If    ${number} % 2 != 0     Odd
    Log To Console    ${i}
    END

    #Executes the given keyword with the given arguments
    Run Keyword    Pass Execution Example
    
    #Executes all the given keywords in a sequence
    run keywords
    #Runs the given keyword with the given arguments, if ``condition`` is true
    Run Keyword If    ${True}    Log To Console    Keyword call or any operation

    #Runs the keyword and continues execution even if a failure occurs.
    #The execution is not continued if the failure is caused by invalid syntax, timeout, or fatal exception.
    Run Keyword And Continue On Failure	 Fail	This is a stupid example
    Log To Console    This keyword is executed

    #If the expected error occurs, the error message is returned and it can be further processed or tested if needed. If there is no error, or the error does not match the expected error, this keyword fails.
    Run Keyword And Expect Error

    #Runs the given keyword with the given arguments and ignores possible error
    #Errors caused by invalid syntax, timeouts, or fatal exceptions are not caught by this keyword. Otherwise this keyword itself never fails.
    Run Keyword And Ignore Error    keyword

    #Runs the specified keyword and returns from the enclosing user keyword.
    Run Keyword And Return If
    Run Keyword And Return
    
    #Runs the given keyword with given arguments and returns the status as a Boolean value
    Run Keyword And Return Status

    #Runs the specified keyword logs a warning if the keyword fails.
    Run Keyword And Warn On Failure

    #Runs the given keyword with the given arguments, if all tests passed.
    Run Keyword If All Tests Passed
    
    #Runs the given keyword with the given arguments, if one or more tests failed.
    Run Keyword If Any Tests Failed
    
    #Runs the given keyword with the given arguments, if the test failed.
    Run Keyword If Test Failed
    
    #Runs the given keyword with the given arguments, if the test passed.
    Run Keyword If Test Passed
    
    #Runs the given keyword if either a test or a keyword timeout has occurred.
    Run Keyword If Timeout Occurred
    
    #Runs the given keyword with the given arguments if condition is false
    Run Keyword Unless    condt     keyword
    

variable declaration examples
    #Makes a variable available globally in all tests and suites.
    #Variables assigned locally based on keyword return values or by using Set Suite Variable, Set Test Variable or Set Local Variable override
    #these variables in that scope, but the global value is not changed in those cases.
    Set Global Variable    ${global_var}    4
    Log To Console    global var it can be used in other methods: ${global_var}

    #Makes a variable available everywhere within the local scope.
    Set Local Variable    ${local_var}     3
    Log To Console    local var can be called in same method ${local_var}
    
    Set Suite Variable    ${suite_var}    6
    Log To Console      ${suite_var}  
    
    Set Test Variable    ${Test_var}    7
    Log To Console    ${Test_var}
    
    ${var}    Set Variable    3
    ${cond_var}    Set Variable If    3<4    10
    
    
    #Sets the log threshold to the specified level
    Set Log Level
    #Resets the log level to the original value
    Reset Log Level

    Set Suite Metadata
    Set Suite Documentation    
    Set Test Documentation    
    Set Test Message    
    Set Tags

    Set Global Variable	Global — Available across all test cases, suites, and keywords	Sets a variable accessible everywhere in the entire test run.
    Set Local Variable	Local — Available only within the current keyword	Defines a variable limited to the keyword where it is set.
    Set Suite Variable	Suite — Available within the current suite (all test cases)	Makes a variable accessible to all test cases and keywords in the suite.
    Set Test Variable	Test — Available within the current test case	Makes a variable accessible only within the test case where it is set.
    Set Task Variable	Task — Available within the current task (e.g., setup or teardown)	Makes a variable accessible within a task such as test or suite setup/teardown.
    Set Variable	Local — Same as Set Local Variable	A general-purpose keyword that sets a local variable within a keyword or test case.

    Variable Should Exist
    Variable Should Not Exist
    Wait Until Keyword Succeeds

Assertion example
    # Creating empty list 
    ${var_1}    Create List
    Should Be Empty     ${var_1}
    Should Not Be Empty    1
    ${var_2}  Set Variable    One
    # Fails if the given objects are unequal.
    Should Be Equal    One    one     msg=Tru    ignore_case=True
    Should Not Be Equal    One     one 
    ${var_3}  Set Variable    1
    ${var_4}  Set Variable    1.11
    ${var_5}  Set Variable    string  
    Should Be Equal As Integers    ${var_3}    1
    Should Not Be Equal As Integers    ${var_3}    2
    Should Be Equal As Numbers     ${var_4}    1.11
    Should Not Be Equal As Numbers    ${var_4}    1.14
    Should Be Equal As Strings     ${var_5}    string
    Should Not Be Equal As Strings    ${var_5}    string1

    Should Be True    1<7
    Should Not Be True    1>7

    # it should contain value 
    Should Contain    12345    5    msg=Number is not there  
    Should Not Contain       12345    6    msg=Number is not there

    # any one value should be there in the list 
    Should Contain Any       1 2 3 4 5     6   7   8   2
    Should Not Contain Any    1  2  3  4  5     9    10    11

    # value should be there x times in the item
    Should Contain X Times        hellohelloworldworld    hello  2

    Should Start With    HelloWolrd     Hello
    Should Not Start With    HelloWorld    World
    
    Should End With     HelloWolrd     d
    Should Not End With     HelloWolrd     h

    Log To Console    regexp
#    Should Match
#    Should Not Match
#    Should Match Regexp
#    Should Not Match Regexp

skip example
    # skip the Execution
#    Skip    Hello
#    Skip If    1<7
    Log To Console    Skip the exp


*** Test Cases ***
Test case
     Continue for loop example
     Exit For Loop Example
     Converting Values in Robot example
     Create Dictionary example
     Create List Example
     Evaluate example
     Fail And Fatal Error Example
     Get Methods Examples
     Run Keyword And Ignore Error    Import example
     Log example
     Pass Execution example
     #Executes the specified keyword multiple times
     Repeat Keyword    5 times    Pass Execution Example
     Replace Variables
     Run Keywords examples
     variable declaration examples
     Assertion example
     skip example
      

     


     

     


      
     
     
    
    
