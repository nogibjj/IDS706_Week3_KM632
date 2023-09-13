import unittest
import polars as pl
from main import find_mean, find_median, find_std

data = {"Loan Amount(in USD)": [1000, 2000, 3000, 4000, 5000]}
df = pl.DataFrame(data)


class TestSumFunction(unittest.TestCase):
    def test_stats(self):
        data = {"Loan Amount(in USD)": [1000, 2000, 3000, 4000, 5000]}
        df = pl.DataFrame(data)
        expected_mean = "$3,000.00"
        expected_median = "$3,000.00"
        expected_std = "$1,581.00"
        mean_result = find_mean(df)
        median_result = find_median(df)
        std_result = find_std(df)
        self.assertEqual(mean_result, expected_mean)
        self.assertEqual(median_result, expected_median)
        self.assertEqual(std_result, expected_std)


if __name__ == "__main__":
    unittest.main()
