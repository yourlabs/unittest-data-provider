from unittest import TestCase
from mock import Mock, call
from dummy import Dummy


class TestDataProvider(TestCase):
    def test_lambda_decoration(self):
        """Test data provider with a lambda function"""
        called_func_mock = Mock()
        dummy = Dummy(called_func_mock)
        dummy.decorated_by_lambda_method()
        called_func_mock.assert_has_calls([
            call(Dummy.ARG1, Dummy.ARG2),
            call(Dummy.ARG3, Dummy.ARG4),
        ])

    def test_def_decoration(self):
        """Test data provider with a class static method"""
        called_func_mock = Mock()
        dummy = Dummy(called_func_mock)
        dummy.decorated_by_def_method()
        called_func_mock.assert_has_calls([
            call(Dummy.ARG1, Dummy.ARG2),
            call(Dummy.ARG3, Dummy.ARG4),
        ])
