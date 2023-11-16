import requests
import json
import unittest
from ServerSide.server.json_manipulation import load_users_from_json, save_users_to_json
from ServerSide.server.route_classes import delete_user


def log_test_start(test_name):
    print(f"Running test: {test_name}")


def log_test_success(test_name):
    print(f"Test '{test_name}' succeeded.")


def log_test_failure(test_name, error_message):
    print(f"Test '{test_name}' failed: {error_message}")


class TestAppEndpoints(unittest.TestCase):
    base_url = "http://10.0.0.15:5000"
    cookie = ""

    def test_homepage(self):
        log_test_start("test_homepage")
        url = f"{self.base_url}/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "You have reached the server.")
        log_test_success("test_homepage")

    def test_invalid_login(self):
        log_test_start("test_invalid_login")
        url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "invalid_user",
            "password": "invalid_password"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 401)  # Ensure unauthorized status code
        log_test_success("test_invalid_login")

    def test_login(self):
        log_test_start("test_login")
        url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "user1",
            "password": "user1"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        log_test_success("test_login")

    def test_logout(self):
        log_test_start("test_logout")
        # Logout
        logout_url = f"{self.base_url}/logout"
        logout_response = requests.get(logout_url)
        self.assertEqual(logout_response.status_code, 200)
        log_test_success("test_logout")

    def test_admin_dashboard_failure(self):
        log_test_start("test_admin_dashboard_failure")
        # Login as a non-admin user
        login_url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "user1",
            "password": "user1"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        login_response = requests.post(login_url, headers=headers, data=payload)
        self.assertEqual(login_response.status_code, 200)

        # Attempt to access the admin dashboard
        url = f"{self.base_url}/admin"
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)

        # Logout
        logout_url = f"{self.base_url}/logout"
        logout_response = requests.get(logout_url)
        self.assertEqual(logout_response.status_code, 200)
        log_test_success("test_admin_dashboard_failure")

    def test_admin_dashboard_success(self):
        log_test_start("test_admin_dashboard_success")
        # Login as an admin user
        login_url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": "admin",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        login_response = requests.post(login_url, headers=headers, data=payload)
        self.assertEqual(login_response.status_code, 200)

        # Get the cookies from the login response
        cookies = login_response.cookies

        # Access the admin dashboard with the cookies
        url = f"{self.base_url}/admin"
        response = requests.get(url, cookies=cookies)  # Pass the cookies in the request
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "admin Dashboard")
        log_test_success("test_admin_dashboard")


class TestRegisterEndpoint(unittest.TestCase):
    base_url = "http://10.0.0.15:5000"

    def tearDown(self) -> None:
        # Clean up by deleting the test user
        delete_user("testuser")

    def test_register_success(self):
        # Test a successful user registration
        log_test_start("test_register_success")
        url = f"{self.base_url}/register"
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = requests.post(url, json=data)

        # Check the response status code and message
        if response.status_code == 201:
            print("Success: User registered successfully.")
        else:
            print(f"Failure: Unexpected status code ({response.status_code}).")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.text, 'User registered successfully.')

        # Check that the user was added to the database
        users = load_users_from_json()
        user = users.get("testuser")
        if user is not None:
            print("Success: User was added to the database.")
        else:
            print("Failure: User was not added to the database.")
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], "testuser")

    def test_register_missing_fields(self):
        # Test registration with missing fields
        log_test_start("test_register_missing_fields")
        url = f"{self.base_url}/register"
        data = {
            "password": "testpassword"
        }
        response = requests.post(url, json=data)

        # Check the response status code and message
        if response.status_code == 400:
            print("Success: Registration with missing fields correctly rejected.")
        else:
            print(f"Failure: Unexpected status code ({response.status_code}).")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, 'Username and password are required.')

    def test_register_existing_user(self):
        # Test registration with an existing username
        log_test_start("test_register_existing_user")
        url = f"{self.base_url}/register"
        data = {
            "username": "user1",
            "password": "user1"
        }

        response = requests.post(url, json=data)

        # Check the response status code and message
        if response.status_code == 400:
            print("Success: Registration with existing username correctly rejected.")
        else:
            print(f"Failure: Unexpected status code ({response.status_code}).")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, 'Username already exists.')


if __name__ == '__main__':
    unittest.main()
