import unittest
from unittest.mock import patch, call
from main import decimal_to_binary

class DecimalToBinary(unittest.TestCase):
    @patch('builtins.print')
    def test_zero(self, mocked_print):
        expected = [call('0')]
        decimal_to_binary(0)

        self.assertEqual(expected, mocked_print.mock_calls)

    @patch('builtins.print')
    def test_one(self, mocked_print):
        expected = [call("1")]
        decimal_to_binary(1)

        self.assertEqual(expected, mocked_print.mock_calls)

    @patch('builtins.print')
    def test_five(self, mocked_print):
        expected = [call("101")]
        decimal_to_binary(5)

        self.assertEqual(expected, mocked_print.mock_calls)

    #chat-gpt generated test cases
    @patch('builtins.print')
    def test_lots_of_cases(self, mocked_print):
        test_cases = [
            (0, "0"),         # Smallest non-negative integer
            (1, "1"),         # Smallest positive integer
            (2, "10"),        # Powers of 2
            (3, "11"),        # Small odd number
            (4, "100"),
            (5, "101"),
            (10, "1010"),     # Composite number
            (15, "1111"),     # All 1's for a 4-bit binary
            (31, "11111"),    # All 1's for a 5-bit binary
            (32, "100000"),   # Power of 2
            (64, "1000000"),  # Larger power of 2
            (127, "1111111"), # Maximum 7-bit binary
            (128, "10000000"),# Smallest 8-bit binary
            (255, "11111111"),# Maximum 8-bit binary
            (256, "100000000"), # 2^8, next power of 2
            (1023, "1111111111"), # Maximum 10-bit binary
            (1024, "10000000000"),# Large power of 2
            (2047, "11111111111"),# Maximum 11-bit binary
            (4096, "1000000000000"), # Large power of 2
            (8191, "1111111111111"), # Maximum 13-bit binary
            (16384, "100000000000000"), # Large power of 2
            (32767, "111111111111111"), # Maximum 15-bit binary
            (65535, "1111111111111111"), # Maximum 16-bit binary
            (1048575, "11111111111111111111"), # Large composite
            (2097152, "100000000000000000000") # Large power of 2
        ]

        for decimal, expected_binary in test_cases:
            with self.subTest(decimal=decimal, expected_binary=expected_binary):
                mocked_print.reset_mock()  # Clear previous mock calls
                decimal_to_binary(decimal)
                self.assertEqual([call(expected_binary)], mocked_print.mock_calls)



if __name__ == '__main__':
    unittest.main()