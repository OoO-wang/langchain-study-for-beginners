# 本次学习定制化middleware

除了预构建的middleware，还可以自己构建middleware，定制化的控制agent

## 定制化middleware有两种形式
- 直接使用装饰方法，简单快捷，但功能简单
- 实现类，复杂，但可实现多功能复杂的middleware

## 使用装饰方法实现定制化middleware
- @before_model装饰方法，可在模型调用前运行，做一些前置工作
- @after_model装饰方法，模型调用后运行，可以做一些验证工作
- 其他装饰方法

## 使用具体类实现定制化middleware
- 需要继承AgentMiddleware类，然后定制化的实现before_model、after_model等方法

