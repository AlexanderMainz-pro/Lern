import unittest

def temperature_status(temp):
    if temp < -30:
        return "Too Cold"
    elif -30 <= temp < 0:
        return "Cold"
    elif 0 <= temp < 30:
        return "Warm"
    elif 30 <= temp < 50:
        return "Hot"
    else:
        return "Too Hot"

class TestTemperatureStatus(unittest.TestCase):

    def test_too_cold(self):
        self.assertEqual(temperature_status(-31), "Too Cold")

    def test_cold_boundary(self):
        self.assertEqual(temperature_status(-30), "Cold")

    def test_cold(self):
        self.assertEqual(temperature_status(-10), "Cold")

    def test_warm_boundary(self):
        self.assertEqual(temperature_status(0), "Warm")

    def test_warm_positive(self):
        self.assertEqual(temperature_status(10), "Warm")

    def test_warm_high(self):
        self.assertEqual(temperature_status(20), "Warm")

    def test_hot_boundary(self):
        self.assertEqual(temperature_status(30), "Hot")

    def test_hot(self):
        self.assertEqual(temperature_status(40), "Hot")

    def test_too_hot(self):
        self.assertEqual(temperature_status(100), "Too Hot")

if __name__ == "__main__":
    unittest.main()