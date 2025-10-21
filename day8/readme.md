# 本次学习context工程

### 当一个agent表现不尽人意的时候，往往可以归咎于两个原因
- 调用的LLM能力不行
- 没有将正确的context传给LLM

一般来说，我们选择了一个可靠的LLM，只需要确保正确的context传给LLM即可

### context的类型
- Instructions，一般就是指提示词，传递给LLM
- Tools，供LLM调用的工具，工具参数、响应、描述都可视为context传递给LLM
- Structured output，结构化输出，传递给LLM
- Session context，对话内容
- Long term memory，长期记忆，如用户偏好等
- Runtime configuration context，agent配置，不会改变但会影响LLM，例如DB连接

