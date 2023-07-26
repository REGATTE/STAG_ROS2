from generate import Generate

import unittest

class TestClass(unittest.TestCase):

    number_of_bits = 48
    border_width = 0.125
    outer_circle_radius = 0.4
    inner_circle_radius = 0.35
    code_radius = 0.062482177287080
    filler_code_radius = 0.7
    file_size = 1000

    def test_fill_location(self):
        Generate.fill_location(self)
        
if __name__ == "__main__":
    unittest.main()
    