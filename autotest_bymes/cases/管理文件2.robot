*** Settings ***

Library  管理文件2.py   WITH NAME  F

Library  管理文件2.c1   WITH NAME  c1



*** Test Cases ***

管理员首页 ui-0101

  c1.teststeps
