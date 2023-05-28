import pytest
import math
from lib.apiwrapper import *
import requests


class TestClass:
    """Юнит тесты в новой оболочке"""
    """Connection tests"""

    def test_get_form_http_status(self):
        assert get_form().status_code == 200

    def test_post_form_http_status(self):
        assert post_form(1, 2).status_code == 200

    """Different values tests"""

    @pytest.mark.parametrize("x, n, expected", [(-12.4, -1, -0.08064516129), (-12.4, 0, 1), (-12, 1, -12),
                                                (0, 3, 0), (9.2, -1, 0.1086956521), (9.2, 0, 1), (9.2, 3, 778.688)])
    def test_simple_enumeration(self, x, n, expected):
        assert math.isclose(float(post_form(x, n).text), float(str(expected))) is True

    def test_solution_base_zero_exp_negative(self):
        assert post_form(0, -4).status_code == 400

    def test_solution_both_params_zero(self):
        assert post_form(0, 0).status_code == 400

    """border values tests"""

    @pytest.mark.parametrize("x, n, expected", [(-99.9999, 2, 9999.9800), (99.9999, 2, 9999.9800),
                                                (1.0, -2 ** 31, 1), (1, -2 ** 31 + 1, 1),
                                                (1.000000001, 2 ** 31 - 2, 8.56328),
                                                (1.000000001, 2 ** 31 - 1, 8.56328), (-21, 3, -9261), (21, 3, 9261)])
    def test_correct_border_values(self, x, n, expected):
        assert math.isclose(float(post_form(x, n).text), float(str(expected)), abs_tol=0.0001) is True

    @pytest.mark.parametrize("x, n", [(-100.01, 2), (100.001, 1), (1.0, -2 ** 31 - 1), (1, 2 ** 31), (-22, 3), (22, 3)])
    def test_over_border_values(self, x, n):
        assert post_form(x, n).status_code == 400

    """incorrect data types (str, bool, none) w8 4 400code"""

    @pytest.mark.parametrize("x, n", [(10, 2.1), (2, "qwert123"), (False, 2), ("abra", 2),
                                      (2, False), ("", 2), (16.4, "")])
    def test_incorrect_data_types(self, x, n):
        assert post_form(x, n).status_code == 400

    """Конец юнит тестов. 40 строк вместо примерно 120 строк юнит тестов из test_main.py"""

    def test_solution_without_base(self):
        response = requests.post(BASE_URL, data={"n": 3})
        assert response.status_code == 400

    def test_solution_with_extra_fields_without_error(self):
        response = requests.post(BASE_URL, data={"x": 4, "n": 3, "test": 123})
        assert response.status_code == 200

    def test_solution_with_extra_fields_returns_result(self):
        response = requests.post(BASE_URL, data={"x": 4, "n": 3, "test": 123})
        assert float(response.text) == 64

    def test_solution_non_existent_endpoint(self):
        response = requests.get(f"{BASE_URL}safadwqe")
        assert response.status_code == 404

    def test_solution_patch_request(self):
        response = requests.patch(BASE_URL)
        assert response.status_code == 405

    def test_solution_delete_request(self):
        response = requests.delete(BASE_URL)
        assert response.status_code == 405

    def test_solution_put_request(self):
        response = requests.put(BASE_URL)
        assert response.status_code == 405

    def test_solution_post_with_jwt_no_error(self):
        data = {"x": 4, "n": 3}
        response = requests.post(BASE_URL, data=data, headers={"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
                                                                                "eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4Z"
                                                                                "jItOGZhYi1jZWYzOTA0NjYwYmQifQ.-xN_h82"
                                                                                "PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM"})
        assert response.status_code == 200

    def test_solution_post_with_jwt_returns_result(self):
        data = {"x": 4, "n": 3}
        response = requests.post(BASE_URL, data=data, headers={"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
                                                                                "eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4Z"
                                                                                "jItOGZhYi1jZWYzOTA0NjYwYmQifQ.-xN_h82"
                                                                                "PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM"})
        assert float(response.text) == 64

    def test_solution_get_form_content_type(self):
        assert get_form().headers["Content-type"] == "text/html; charset=utf-8"

    def test_solution_post_form_content_type(self):
        assert post_form(x= 4, n= 3).headers["Content-type"] == "text/html; charset=utf-8"

