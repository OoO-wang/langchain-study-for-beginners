# 本次学习runtime

## runtime对象附带一下信息
- Context，存储静态信息，user id、数据库连接等
- Store，用于long-term memory的一个BaseStore实例
- Stream writer，用于访问流模式的对象

## 使用前提
- 使用create_agent创建agent
- 对context_schema赋值

## 在tools中使用runtime
- langchain.tools模块提供ToolRuntime对象，供在工具中访问runtime中的数据

具体实现详细参考代码

## 在middleware中使用runtime
- 可以使用ModelRequest中的runtime对象访问runtime中的数据

由于langChain v1版本的ModelResponse的bug还没修复，这块代码先不演示
