import pytest
import requests

def test_response():
	response = requests.get('d3uktgftytucdw.cloudfront.net/index.html')
	assert response.status_code == 200