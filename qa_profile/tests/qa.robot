*** Settings ***
Library  qa.py

*** Test Cases ***
Test Hello Service
    [Template]  Test Hello

    sheena     Hi there, sheena!
    ${EMPTY}   Hi there, !
    1          Hi there, 1!

