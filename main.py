class Solution: #"""Доработанное  мной решение, которое проходит все тесты и учитывает все требования"""
    def myPow(self, x: float = "", n: int = "") -> float:

        if x == "" or n == "":
            raise ValueError(f"Base and Exponent must exist, your is x = {x}, n = {n}")
        if not isinstance(n, int) or type(n) is bool:
            raise TypeError(f"Exponent power must be integer, your is {type(n)}")
        if not isinstance(x, (float, int)) or type(x) is bool:
            raise TypeError(f"Base power must be float, your is {type(x)}")
        if x == 0:
            if n == 0:
                raise ValueError("you can't raise 0 to the power of 0")
            if n < 0:
                raise ValueError("Can't divide by 0")
        if n < -2**31 or n > 2**31-1:
            raise ValueError("exponent must be between -2**31 <= n <= 2**31-1")
        if x <= -100 or x >= 100:
            raise ValueError(f"Base power must be between -100 and 100, your base power is {x}")

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        if -10**4 <= res <= 10**4:
            if n >=0:
                return res
            else:
                return 1/res
        else:
            raise ValueError(f"The result of the calculation doesnt meet the limit: -10**4 <= x**n <= 10**4/n Your res is {1/res}")


"""Исходное решение с leetCode, которое не прошло такие тесты как:
    1)test_solution_ans_above_max
    2)test_solution_ans_below_min
    3)test_solution_base_above_max
    4)test_solution_base_below_min
    5)test_solution_base_zero_exp_negative
    6)test_solution_both_params_zero
    7)test_solution_exp_above_max
    8)test_solution_exp_below_min
    9)test_solution_float_exponent
    10)test_solution_wrong_type_base
    11)test_solution_float_exponent
    12)test_solution_symbol_exponent
    13)test_solution_bool_exponent
    14)test_solution_symbol_base   
    15)test_solution_bool_base
    16)test_solution_no_base
    17)test_solution_no_exp"""
    
    
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def helper(x, n):
#             if x == 0:
#                 return 0
#             if n == 0:
#                 return 1
#
#             res = helper(x * x, n // 2)
#             return x * res if n % 2 else res
#
#         res = helper(x, abs(n))
#         return res if n >= 0 else 1 / res