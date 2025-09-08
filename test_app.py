import unittest
from monitor import get_system_stats

class TestMonitoring(unittest.TestCase):
    def test_get_system_stats_values(self):
        cpu, memory, disk = get_system_stats()

        self.assertIsInstance(cpu, (int, float))
        self.assertIsInstance(memory, (int, float))
        self.assertIsInstance(disk, (int, float))

        self.assertGreaterEqual(cpu, 0)
        self.assertLessEqual(cpu, 100)
        self.assertGreaterEqual(memory, 0)
        self.assertLessEqual(memory, 100)
        self.assertGreaterEqual(disk, 0)
        self.assertLessEqual(disk, 100)

if __name__ == "__main__":
    unittest.main()
