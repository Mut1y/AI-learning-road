# AI Agent 白话笔记


## 什么是 Agent？

### 我的理解

Agent 就像一个公司的员工系统。


里面有：

老板：
LLM

秘书：
Python程序

员工：
Tools


用户提出需求：

↓

老板分析：

↓

秘书安排任务：

↓

员工执行：

↓

结果返回老板：

↓

回答用户。



---

## 技术理解


Agent = LLM + Tools + Memory + Loop


LLM负责思考

Tools负责执行

Memory负责记忆

Loop负责不断循环处理任务。



---

## 我的代码对应


我的项目：

AI-learning-road Day30


LLM：

DeepSeek API


Tools：

calculator_tool

github_tool


执行：

run_tool()


工具管理：

tool_registry.py



---

## 遇到的问题


问题：

AI知道工具，但是不会调用参数。


原因：

JSON格式不正确。


解决：

修改tool description。

# Tool Calling


## 白话理解


Tool Calling就是：

老板不会自己做所有事情。

他会告诉秘书：

“去找计算部门算一下。”



## 技术理解


LLM输出JSON：

{
"name":"calculator_tool",
"arguments":{
"expression":"999*888"
}
}


Python收到以后：

调用对应函数。



## 我的代码


ai_service.py


ask_ai()


↓

run_tool()


↓

calculator.py



## 我的Bug


一开始：

arguments为空。


原因：

模型不知道需要expression。


解决：

修改工具描述。

## Day31：Memory（记忆）
什么是 Memory？
Memory 就是 Agent 能够记住之前发生过的事情，而不是每次都像第一次见到用户一样。
为什么需要？
没有 Memory，Agent 每轮对话都是独立的，无法理解"他""那个""继续"等上下文，也不能持续完成复杂任务。
我的 Day30 有吗？
没有。
目前我的 Agent 每次只发送当前用户输入给 LLM，因此属于无状态（Stateless）Agent。
Day31 学到了什么？
把历史消息保存在 messages 中，每次调用 LLM 时一起发送，让模型获得上下文，这就是最基础的对话记忆（Conversation Memory）。
真实项目怎么用？
真实 Agent 通常不仅保存聊天记录，还会维护长期记忆、任务状态、工具执行记录等，并通过数据库、向量库或摘要机制管理这些记忆，而不是无限保存所有消息。
一句话总结
Memory 不是让 LLM 自己记住，而是程序把需要记住的信息重新提供给 LLM。

Memory 和 Context 的区别
很多人认为：
Memory就是让AI自己记住。
这是错误理解。
实际上：
Memory：保存过去的信息
Context：当前提供给LLM的信息
LLM没有真正的永久记忆。
程序负责管理Memory，并选择哪些内容放入Context。
一句话：
Memory负责存，Context负责送，LLM负责想。