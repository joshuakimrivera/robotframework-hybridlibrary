*** Settings ***
Library                                                             HybridLibrary    

Test Setup                                                          Sleep           3s

*** Variable ***


*** Test Case ***

Test Library Create Session
    Open Hybrid Application                                         http://localhost:4723/wd/hub
    ...                                                             deviceName=XiaomiMi6
    ...                                                             udid=3a32a5ce7d2b
    ...                                                             platformName=Android
    ...                                                             browserName=Chrome
    ...                                                             autoGrantPermissions=true


# Test Library Set Context
#     Set Context                                                     NATIVE_APP


Test Library Get Context
    Sleep                                                           5s
    ${context}                                                      Get Current Context
    Log To Console                                                  ${context}


Test Library Get All Context
    Sleep                                                           5s
    ${contexts}                                                     Get All Contexts
    Log To Console                                                  ${contexts}


# Test Library Tap Element
#     FOR     ${index}                                                IN RANGE            0   4
#         Tap                                                         ${tutorial_button}
#         Sleep                                                       2s
#     END


Test Library Set Context to Webview
    ${context}                                                      Get Current Context
    # Set Context                                                     WEBVIEW_com.prometheus_service.midas.br.uat.nativex


# Test Library Get Window Handles
#     ${handles}                                                      Get Window Handles
#     Log To Console                                                  ${handles}

# Test Library Switch To Window
#     ${handles}                                                      Get Window Handles
#     Switch To Window                                                ${handles}[0]

# Test Navigate URL
#     Web Navigate To URL                                             https://www.google.com
#     Sleep                                           