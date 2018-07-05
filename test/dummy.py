from unittest_data_provider import data_provider


class Dummy:
    ARG1 = 'my_arg_1'
    ARG2 = 'my_arg_2'
    ARG3 = 'my_arg_3'
    ARG4 = 'my_arg_4'

    data_provider1 = lambda: (
        (Dummy.ARG1, Dummy.ARG2),
        (Dummy.ARG3, Dummy.ARG4)
    )

    @staticmethod
    def data_provider2():
        return (
            (Dummy.ARG1, Dummy.ARG2),
            (Dummy.ARG3, Dummy.ARG4)
        )

    def __init__(self, called_func):
        self.called_func = called_func

    @data_provider(data_provider1)
    def decorated_by_lambda_method(self, arg1, arg2):
        """Dummy method which use a lambda function as data provider"""
        self.called_func(arg1, arg2)

    @data_provider(data_provider2)
    def decorated_by_def_method(self, arg1, arg2):
        """Dummy method which use a class static method as data provider"""
        self.called_func(arg1, arg2)
