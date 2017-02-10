"""This module does blah blah."""
from tensorflow.python import Variable, constant, add, assign, initialize_all_variables, Session

class DemoBase(object):
    '''DemoBase'''

    @staticmethod
    def run():
        """run the demo."""
        pass

class OpSessDemo(DemoBase):
    '''OpSessDemo'''

    @staticmethod
    def run():
        # 创建一个变量, 初始化为标量 0.
        state = Variable(0, name="counter")

        # 创建一个 op, 其作用是使 state 增加 1

        one = constant(1)
        new_value = add(state, one)
        update = assign(state, new_value)

        # 启动图后, 变量必须先经过`初始化` (init) op 初始化,
        # 首先必须增加一个`初始化` op 到图中.
        init_op = initialize_all_variables()

        # 启动图, 运行 op
        with Session() as sess:
            # 运行 'init' op
            sess.run(init_op)
            # 打印 'state' 的初始值
            print(sess.run(state))
            # 运行 op, 更新 'state', 并打印 'state'
            for _ in range(3):
                sess.run(update)
                print(sess.run(state))
                # 输出:

                # 0
                # 1
                # 2
                # 3
