import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Remote(command_executor="http://localhost:4444/", desired_capabilities={})
    request.cls.driver = driver
    yield
    driver.quit()
