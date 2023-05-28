from unittest import TestCase
from main import Solution


class Test(TestCase):

    """TEST SUITE1 (PRIORITY: HIGH) - PARAMETER TESTS (BASE AND EXPONENT OF POWER)"""

    def test_solution_both_params_negative(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(-12.4, -1), -0.08064516129)

    def test_solution_base_negative_exp_zero(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(-12.4, 0), 1)

    def test_solution_base_negative_exp_positive(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(-12, 1), -12)

    def test_solution_base_zero_exp_negative(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(0, -4)

    def test_solution_both_params_zero(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(0, 0)

    def test_solution_base_zero_exp_positive(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(0, 3), 0)

    def test_solution_base_positive_exp_negative(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(9.2, -1), 0.10869565217391305)

    def test_solution_base_positive_exp_zero(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(9.2, 0), 1)

    def test_solution_base_positive_exp_positive(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(9.2, 3), 778.688)

    """ANSWER TESTS ne nujni tk uje polucheni vse vozmozjnie
    varianti otvetov int i float positive i negative a tak zje  zero  """

    """TEST SUITE2 (PRIORITY: MEDIUM) BORDER VALUES TESTS"""

    def test_solution_base_below_min(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(-100.01, 2)

    def test_solution_base_above_min(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(-99.9999, 2), 9999.9800)

    def test_solution_base_below_max(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(99.9999, 2), 9999.9800)

    def test_solution_base_above_max(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(100.001, 1)

    def test_solution_exp_below_min(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(1.000, -2**31-1)

    def test_solution_exp_equal_min(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(1, -2**31), 1, 3)

    def test_solution_exp_above_min(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(1, -2**31+1), 1, 3)

    def test_solution_exp_below_max(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(1.000000001, 2**31-2), 8.56328, 5)

    def test_solution_exp_equal_max(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(1.000000001, 2**31-1), 8.56328, 5)

    def test_solution_exp_above_max(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(1, 2**31)

    def test_solution_ans_below_min(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(-22, 3)

    def test_solution_ans_above_min(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(-21, 3), -9261)

    def test_solution_ans_above_max(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.myPow(22, 3)

    def test_solution_ans_below_max(self):
        sut = Solution()
        self.assertAlmostEqual(sut.myPow(21, 3), 9261)

        """TEST SUITE3 (PRIORITY: MEDIUM) INPUT DATA TESTS"""

    def test_solution_float_exponent(self):
        sut = Solution()
        with self.assertRaises(TypeError):
            sut.myPow(10, 2.1)

    def test_solution_symbol_exponent(self):
        sut = Solution()
        with self.assertRaises(TypeError):
            sut.myPow(2, "qwert123")

    def test_solution_bool_exponent(self):
        sut = Solution()
        with self.assertRaises(TypeError):
            sut.myPow(2, False)

    def test_solution_symbol_base(self):
        sut = Solution()
        with self.assertRaises(TypeError):
            sut.myPow("abra", 2)

    def test_solution_bool_base(self):
        sut = Solution()
        with self.assertRaises(TypeError):
            sut.myPow(False, 2)








