def data_provider(fn_data_provider):
    """
    Data provider decorator,
    allows another callable to provide the data for the test
    """
    def test_decorator(fn):
        def test_repl(self, *args):
            if hasattr(fn_data_provider, '__func__'):
                data = fn_data_provider.__func__()
            else:
                data = fn_data_provider()

            for i in data:
                try:
                    fn(self, *i)
                except AssertionError:
                    print("Assertion error caught with data set ", i)
                    raise
        return test_repl
    return test_decorator
