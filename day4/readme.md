# 本次学习agent相关内容
简单来讲，agent是由model模型和tool工具的组成，然后完成某项任务

## 模型（model）

完成某项任务的agent可以使用多种不同的模型，使用模型有两种方式：
- static model
  - 预先声明model，直接使用
- dynamic model
  - 根据状态、上下文或请求在运行时判断使用何种模型
  - langChain提供了langchain.agents.middleware模块的wrap_model_call, ModelRequest, ModelResponse方法和类，便捷的实现运行时选择模型

## 工具（tools）

工具一般使用方式如下：
- 多个tools连续调用，一般通过提示词可以实现
- 多个tools并行调用
- 多个tools选择其一调用，和model同理
- ReAct loop，即reasoning+acting，模型通过tools结果进行推理，再次循环调用tools、再推理，直到得到满意结果或达到loop条件

tools定义
- langChain提供了langchain.tools模块的tool装饰器，只需在一个函数前加@tool就可以使其成为tools
- langChain同时提供了langchain.agents.middleware模块的wrap_tool_call装饰器，作用时在调用tools时，经过中间件，可以对tools调用时的错误进行处理

# 其他组成

## 提示词prompt
- 不做过多解释，除了直接使用声明的提示词，还可以使用langchain.agents.middleware模块的dynamic_prompt装饰器，来动态的填充和选择提示词

## 结构化输出
- 不算是agent组成部分，是langChain提供的能力，使用langchain.agents.structured_output模块的ToolStrategy方法，可以将模型结果格式化输出

## 记忆memory
- agent memory分为短期记忆和长期记忆后面详细介绍


