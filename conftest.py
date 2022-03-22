import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1360, 860)

    # Return browser instance to test case:
    yield browser
