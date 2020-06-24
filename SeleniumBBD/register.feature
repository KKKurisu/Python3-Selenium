#coding=utf-8
Feature: Regiter User Form

   As a developer
   I should be able to use given text snippets

    Scenario: open register website
        #Given 假设
        #when 时间
        #then 下一步
        #and 与
        #feature 特性
        #background 背景
        #scenario outline 场合大纲
        When I open the register website
        Then I expect that the title is "注册 - 快乐学习 - 乐学,让学习更有效！ - Powered By EduSoho"


    Scenario: input username
        When I set with useremail "mushishi@qq.com"
        #And I set with username "mushishi01"
        #And I set with password "111111"
        #And I set with code "test"
        #Then I expect that element contains text "验证码错误"