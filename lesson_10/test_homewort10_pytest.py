import pytest
from assertpy import assert_that
from homework_10 import log_event_for_test

def read_log_file():
    with open('login_system.log', 'r') as file:
        last_line = file.readlines()[-1]
        finding_line = last_line[(last_line.find("Login event - Username:")):-1]
        return finding_line

class TestHomework10:
    def test_01_success(self):
        name = "Olga"
        status = "success"
        log_event_for_test(name, status)

        actual = read_log_file()
        expected = f"Login event - Username: {name}, Status: {status}"
        assert actual == expected
