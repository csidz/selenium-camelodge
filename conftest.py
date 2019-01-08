import pytest
from base.webDriverRoot import WebDriverRoot


@pytest.fixture(scope="class")
def one_time_setup(request, browser, base_url):
    print("Running one time setup")
    wdr = WebDriverRoot(browser=browser, base_url=base_url)
    driver = wdr.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


@pytest.fixture()
def set_up(one_time_setup):
    print("Running method level setup")
    yield
    print("Running method level teardown")


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox",
                     help="Input the browser Eg: firefox, chrome, safari, edge or browserless")
    parser.addoption("--OS_Type", help="Input the operating system Eg: Mac, Windows")
    parser.addoption("--base_url", default="http://camelodge.com/", help="Input the base url. Eg: http://camelodge.com")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--OS_Type")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


