import unittest
from unittest.mock import Mock, patch

def send_email(to, message):
    print(f"Email to {to}: {message}")
    return True

def notify_user(to, message):
    return send_email(to, message)

def get_user_name(user_id):
    return "Alice"

def reverse_string(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.fake_api = Mock()
        self.fake_api.get_data.return_value = {"temp": 25}

    # 1. NORMAL CASES
    def test_weather_api_with_mock_object(self):
        result = self.fake_api.get_data()
        self.assertEqual(result, {"temp": 25})

    def test_reverse_string_normal(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_divide_numbers_normal(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(9, 3), 3)
        self.assertEqual(divide_numbers(7, 2), 3.5)

    # 2. EDGE CASES
    def test_reverse_string_edge(self):
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("  "), "  ")
        self.assertEqual(reverse_string("!@#"), "#@!")

    def test_divide_numbers_edge(self):
        self.assertEqual(divide_numbers(0, 5), 0)
        self.assertEqual(divide_numbers(5, 1), 5)
        self.assertEqual(divide_numbers(-10, 2), -5)
        self.assertEqual(divide_numbers(10, -2), -5)
        self.assertAlmostEqual(divide_numbers(1, 3), 0.333333, places=6)

    # 3. ERROR CASES
    def test_divide_by_zero_error(self):
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)
        with self.assertRaises(ValueError) as context:
            divide_numbers(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_reverse_string_type_error(self):
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string(None)
        with self.assertRaises(TypeError):
            reverse_string([1, 2, 3])

    def test_get_user_name_real(self):
        result = get_user_name(123)
        self.assertEqual(result, "Alice")

    def test_mock_object_basics(self):
        mock_obj = Mock()
        mock_obj.get_data.return_value = {"temp": 25}
        result = mock_obj.get_data()
        self.assertEqual(result, {"temp": 25})
        mock_obj.get_data.assert_called_once()

    def test_mock_with_side_effect(self):
        mock_obj = Mock()
        mock_obj.process.side_effect = [1, 2, 3]

        self.assertEqual(mock_obj.process(), 1)
        self.assertEqual(mock_obj.process(), 2)
        self.assertEqual(mock_obj.process(), 3)

    def test_mock_assertions(self):
        mock_obj = Mock()
        mock_obj.calculate(5, 10)
        mock_obj.calculate.assert_called_once()
        mock_obj.calculate.assert_called_with(5, 10)
        self.assertEqual(mock_obj.calculate.call_count, 1)
    def test_mock_with_spec(self):
        class RealClass:
            def existing_method(self):
                return "real"
        mock_obj = Mock(spec=RealClass)
        mock_obj.existing_method.return_value = "mocked"
        self.assertEqual(mock_obj.existing_method(), "mocked")

if __name__ == '__main__':
    unittest.main(verbosity=2)