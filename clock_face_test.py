import unittest
from clock_face import Clock

class TestClockFace(unittest.TestCase):

    def setUp(self):
        self.clock = Clock()

    def test_calculate_angle(self):
        self.clock.hours = 9
        self.clock.minutes = 30
        self.assertEqual(self.clock.calculate_angle(), 105.0)

    def test_calculate_midnight(self):
        self.clock.hours = 12
        self.clock.minutes = 0
        self.assertEqual(self.clock.calculate_angle(), 0.0)

        # 24hr midnight:
        self.clock.hours = 0
        self.clock.minutes = 0
        self.assertEqual(self.clock.calculate_angle(), 0.0)

    def test_calculate_3_40(self):
        self.clock.hours = 3
        self.clock.minutes = 40
        self.assertEqual(self.clock.calculate_angle(), 130.0)

    def test_calculate_15_40(self):
        self.clock.hours = 15
        self.clock.minutes = 40
        self.assertEqual(self.clock.calculate_angle(), 130.0)

if __name__ == '__main__':
    unittest.main()
