class AgentState:


    def __init__(self):

        self.status = "idle"

        self.question = None

        self.thought = None

        self.action=None

        self.tool = None

        self.arguments = None

        self.observation = None



    def update(
        self,
        status=None,
        question=None,
        thought=None,
        action=None,
        tool=None,
        arguments=None,
        observation=None
    ):


        if status:
            self.status=status

        if question:
            self.question=question

        if thought:
            self.thought = thought

        if action:
            self.action=action

        if tool:
            self.tool=tool

        if arguments:
            self.arguments=arguments

        if observation:
            self.observation=observation



    def show(self):

        print("""
====== Agent状态 ======
状态:
{}

问题:
{}

思考:
{}

动作:
{}

工具:
{}

参数:
{}

结果:
{}

=======================
""".format(
self.status,
self.question,
self.thought,
self.action,
self.tool,
self.arguments,
self.observation
))