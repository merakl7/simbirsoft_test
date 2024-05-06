import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Remote(command_executor="http://your_grid_url:4444/wd/hub", desired_capabilities={})
    request.cls.driver = driver
    yield
    driver.quit()
