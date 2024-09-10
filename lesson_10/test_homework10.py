import unittest
from homework_10 import log_event

class MyTestCase(unittest.TestCase):

    def test_1_success_loging(self):
        name = "Success_name"
        status = "success"
        log_event(name, status)
        with open('login_system.log', 'r') as file:
            last_line = file.readlines()[-1]
        self.assertIn(f'Login event - Username: {name}, Status: {status}', last_line)  # add assertion here

    def test_2_expired_loging(self):
        name = "Expired_name"
        status = "expired"
        log_event(name, status)

        with open('login_system.log') as file:
            last_line = file.readlines()[-1]
        self.assertIn(f'Login event - Username: {name}, Status: {status}', last_line)  # add assertion here

    def test_3_failed_loging(self):
        name = "Failed_name"
        status = "failed"
        log_event(name, status)

        with open('login_system.log') as file:
            last_line = file.readlines()[-1]
        self.assertIn(f"Login event - Username: {name}, Status: {status}", last_line)  # add assertion here

if __name__ == '__main__':
    unittest.main()
