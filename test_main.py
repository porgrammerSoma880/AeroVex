

#unit test file for main.py





import unittest
from unittest.mock import patch, MagicMock
import os
import logging




# Import the function from your main.py file.
# If your main.py is in another directory or the function is not at top level, adjust the import as needed.

from main import check_air_quality





#-----------------------













class TestCheckAirQuality(unittest.TestCase):
    """
    Unit tests for the check_air_quality function in main.py.
    These tests use mocking to simulate API calls and environment variables.
    """



    #-------------------------


    def setUp(self):
        """Set up test environment before each test."""
        # Set a dummy API key environment variable
        os.environ["Air_Quality_API_Key"] = "dummy_api_key"
        # Lower logging level to avoid clutter in test output
        logging.disable(logging.CRITICAL)








    def tearDown(self):
        """Clean up after each test."""
        # Remove the dummy API key if present
        if "Air_Quality_API_Key" in os.environ:
            del os.environ["Air_Quality_API_Key"]
        # Re-enable logging
        logging.disable(logging.NOTSET)






    @patch("main.req.get")
    def test_valid_city_successful_api(self, mock_get):
        """
        Test successful API call with a valid city and proper response.
        """
        # Prepare a fake response object
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = (
            '{"overall_aqi":42,"CO":{"concentration":0.4,"aqi":12},'
            '"NO2":{"concentration":0.7,"aqi":16}}'
        )
        mock_get.return_value = mock_response

        # Test the function
        result = check_air_quality("Tawhid", "Bergen")
        self.assertTrue(result)
        mock_get.assert_called_once()








    @patch("main.req.get")
    def test_api_returns_bad_request(self, mock_get):
        """
        Test API returns 400 (bad request) when city is invalid.
        """
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        result = check_air_quality("Riyaad", "invalidcity@@")
        self.assertFalse(result)











    @patch("main.req.get")
    def test_api_returns_other_error(self, mock_get):
        """
        Test API returns other error code, e.g., 500.
        """
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        result = check_air_quality("Yousuf", "Tokyo")
        self.assertFalse(result)










    @patch("main.logging.error")
    def test_missing_api_key(self, mock_logging_error):
        """
        Test function handles missing API key properly.
        """
        if "Air_Quality_API_Key" in os.environ:
            del os.environ["Air_Quality_API_Key"]

        result = check_air_quality("Raisa", "New York")
        self.assertFalse(result)
        mock_logging_error.assert_called_once() 

        









    def test_malicious_city_input(self):
        """
        Test function returns False if city name contains banned characters.
        """
        os.environ["Air_Quality_API_Key"] = "dummy_api_key"
        with patch("main.req.get") as mock_get:
            result = check_air_quality("Raihan", "bad;city")
            self.assertFalse(result)
            mock_get.assert_not_called()










    @patch("main.req.get", side_effect=Exception("Timeout"))
    def test_api_call_exception(self, mock_get):
        """
        Test function handles exceptions raised during API call.
        """
        result = check_air_quality("Tahmid", "Dubai")
        self.assertFalse(result)










    @patch("main.req.get")
    def test_city_name_edge_cases(self, mock_get):
        """
        Test city name at the lower and upper bound of allowed length.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = (
            '{"overall_aqi":75,"CO":{"concentration":0.4,"aqi":12}}'
        )
        mock_get.return_value = mock_response


        # Minimum length (2 chars)
        self.assertTrue(check_air_quality("Sara", "ny"))
        # Maximum length (50 chars)
        city_50 = "a" * 50
        self.assertTrue(check_air_quality("Rini", city_50))





#-----------------------------





