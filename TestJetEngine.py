import unittest
from engine import JetEngine

class TestJetEngine(unittest.TestCase):
    def test_thrust_positive(self):
        engine = JetEngine(altitude=10000, use_afterburner=False)
        result = engine.simulate()
        self.assertGreater(result['Net Thrust'], 0, "Thrust should be positive")

    def test_tsfc_reasonable(self):
        engine = JetEngine()
        result = engine.simulate()
        self.assertTrue(0 < result['TSFC'] < 1, "TSFC should be within a reasonable range")

if __name__ == '__main__':
    unittest.main()
