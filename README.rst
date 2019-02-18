Package for this snippet:
http://melp.nl/2011/02/phpunit-style-dataprovider-in-python-unit-test/

Install::

    pip install unittest-data-provider

Import::

    import unittest
    from unittest_data_provider import data_provider

You can then use data_provider without having to stick this snippet somewhere
...

Thanks drm !

Original blog post by drm pasted here in case the original link goes down
=========================================================================

PHPUnit has a handy feature with which you can provide testdata to your tests.
This is called a data provider, and is implemented by annotating a test with
@dataProvider methodName. Python’s unittest module doesn’t seem to have such a
feature.

PHPUnit’s version
-----------------

The data provider returns a two-dimensional array of test arguments. For
example::

    class CssParserTest extends PHPUnit_Framework_TestCase {
        function setUp() {
            $this->parser = new CssParser();
        }
    
        /**
        * @dataProvider cssColors
        */
        function testParseColor($color, $notation) {
            $this->assertEquals($color, $this->parser->parseColor($notation));
        }
    
    
        function cssColors() {
            return array(
                array(array(0, 0, 0), '#000'),
                array(array(0, 0, 0), '#000000'),
                array(array(0, 0, 0), 'rgb(0, 0, 0)')
                array(array(0, 0, 0), 'black')
            );
        }
    }

Running this test would call the testParseColor() test 4 times, with each of
the arrays returned by cssColors() as the arguments.

Python: providing test data using a decorator
---------------------------------------------

While writing tests for some Python code, I discovered that Python’s unittest
doesn’t seem to have such a feature. So I implemented my own, using a
decorator::

    def data_provider(fn_data_provider):
        """Data provider decorator, allows another callable to provide the data for the test"""
        def test_decorator(fn):
            def repl(self, *args):
                for i in fn_data_provider():
                    try:
                        fn(self, *i)
                    except AssertionError:
                        print "Assertion error caught with data set ", i
                        raise
            return repl
        return test_decorator

Example usage::

    class CssParserTest:
        def setUp(self):
            self.parser = CssColor()
    
        @staticmethod
        def colors():
            return (
            ( (0, 0, 0), '#000' ),
            ( (0, 0, 0), '#000000' ),
            ( (0, 0, 0), 'rgb(0, 0, 0)' ),
            ( (0, 0, 0), 'black' )
        )
    
        @data_provider(colors)
        def test_parse_color(self, color, notation):
            self.assertEquals(color, self.parser.parse_color(notation))

Suggestions of alternatives are greatly appreciated, by the way.
