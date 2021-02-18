import pytest
import requests


def test_response():
	response = requests.get('https://manoloui.com')
	assert response.status_code == 200
