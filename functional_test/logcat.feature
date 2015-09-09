# Created by tksn at 9/8/15

Feature: Logcat monitoring and notification

  phonetest.logcat monitors adb logcat
  and raises exception if fatal failure event occurs

  Scenario: phonetest.logcat catches FATAL ERROR
    Given PhoneProbe is activated
    When I tap crash button
    Then logcat raises exception

