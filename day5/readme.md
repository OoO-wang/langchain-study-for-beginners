# 本次学习middleware

## langChain内置的middleware

### SummarizationMiddleware
主要用于记录对话信息，一般的使用场景如下：
- 当达到context限制时，记录对话内容
- 多轮的长对话
- 需要保留完整对话

详细请看示例代码

### HumanInTheLoopMiddleware
主要用于在model call tools时，人工能够介入判断是否能够执行或其他操作，主要使用场景如下：

- 高风险或重依赖人工的任务

详细请看示例代码





