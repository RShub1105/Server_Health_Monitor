import unittest
from monitor import get_system_stats

class TestMonitoring(unittest.TestCase):
    """Unit tests for monitoring system stats: CPU, memory, disk usage."""

    def test_get_system_stats_values(self):
        """Test that CPU, memory, and disk usage are between 0 and 100%."""
        cpu, memory, disk = get_system_stats()

        # Ensure returned types are correct
        with self.subTest(metric="CPU type"):
            self.assertIsInstance(cpu, (int, float), f"CPU usage should be int or float, got {type(cpu)}")
        with self.subTest(metric="Memory type"):
            self.assertIsInstance(memory, (int, float), f"Memory usage should be int or float, got {type(memory)}")
        with self.subTest(metric="Disk type"):
            self.assertIsInstance(disk, (int, float), f"Disk usage should be int or float, got {type(disk)}")

        # Ensure values are within 0-100%
        for metric_name, value in [("CPU", cpu), ("Memory", memory), ("Disk", disk)]:
            with self.subTest(metric=metric_name):
                self.assertGreaterEqual(value, 0, f"{metric_name} usage should be >= 0, got {value}")
                self.assertLessEqual(value, 100, f"{metric_name} usage should be <= 100, got {value}")

    def test_get_system_stats_non_negative(self):
        """Test that all returned metrics are non-negative."""
        stats = get_system_stats()
        for metric_name, value in zip(["CPU", "Memory", "Disk"], stats):
            with self.subTest(metric=metric_name):
                self.assertGreaterEqual(value, 0, f"{metric_name} usage cannot be negative")

if __name__ == "__main__":
    print("\n🔍 Running Monitoring System Stats Tests\n")
    unittest.main(verbosity=2)
