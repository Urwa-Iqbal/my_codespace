import unittest
import sys
from io import StringIO

class TestOutput(unittest.TestCase):
    def test_output(self):
        expected_output = "hello, Human\n"

        # Redirect sys.stdout to capture the output
        sys.stdout = captured_output = StringIO()

        # Write the code to produce the expected output
        print("hello, Human")

        # Restore sys.stdout
        sys.stdout = sys.__stdout__

        # Compare the expected output with the captured output
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
