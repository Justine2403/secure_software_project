import unittest


def collapse(value=None):
    # Return None if the input is not a string containing only digits
    if not isinstance(value, str) or not value.isdigit():
        return None

    # Convert value to integer for summing digits
    num = int(value)
    # Sum its digits until we reach a single digit which correspond to a number less than 10
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return str(num)


class CollapseTest(unittest.TestCase):

    # Happy path test
    def test100_ShouldCollapseSingleDigit(self):
        value = '5'
        expectedResult = '5'
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)

    def test110_ShouldCollapseSingleDigit(self):
        value = '0'
        expectedResult = '0'
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)

    # More test cases goes here
    # Test 120: Double-digit value
    def test120_ShouldCollapseDoubleDigit(self):
        value = '10'
        expectedResult = '1'  # 1 + 0 = 1
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    # Test 130: Triple-digit value
    def test130_ShouldCollapseTripleDigit(self):
        value = '123'
        expectedResult = '6'  # 1 + 2 + 3 = 6
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)

    # Test 140: Sum with repeated collapsing until single digit is achieved
    def test140_ShouldCollapseRepeatSums(self):
        value = '99'
        expectedResult = '9'  # 9 + 9 = 18, 1 + 8 = 9
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    # Test 150: Double repeat sums with larger input
    def test150_ShouldCollapseDoubleRepeatSums(self):
        value = '98769'
        expectedResult = '3'  # 9 + 8 + 7 + 6 + 9 = 39, 3 + 9 = 12, 1 + 2 = 3
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)

    # Test 160: Check same result with explicit parameter name
    def test160_ShouldCollapseDoubleRepeatSumsWithNamedParameter(self):
        value = '98769'
        expectedResult = '3'
        actualResult = collapse(value=value)
        self.assertEqual(expectedResult, actualResult)

    # Test 170: Fifty-digit value with only 0 should collapse to 0
    def test170_ShouldCollapseFiftyDigitString(self):
        value = '0' * 50
        expectedResult = '0'
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    # Sad path test

    def test901_ShouldCollapseNoParameterPassed(self):
        expectedResult = None
        actualResult = collapse()
        self.assertEqual(expectedResult, actualResult)

    def test902_ShouldCollapseStringOfCharacters(self):
        value = 'a'
        expectedResult = None
        actualResult = collapse(value)
        self.assertEqual(expectedResult, actualResult)

    # More test cases goes here
    
    def test903_ShouldCollapseDigits(self):
    # Test case for input number that is not a string
        value = 1
        expected = None
        actual = collapse(value)
        self.assertEqual(actual, expected)



