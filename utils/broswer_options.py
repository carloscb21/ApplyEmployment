from selenium.webdriver.chrome.options import Options
from sys import platform
from utils import properties


class UnsupportedPlatform(Exception):
    pass


class BrowserSetup:
    options: Options
    web_home_path: str
    driver_path: str


def get_basic_setup() -> BrowserSetup:
    browser_setup = BrowserSetup()
    if properties.OS_LINUX in platform:
        print(properties.OS_LINUX)
        options = Options()
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        browser_setup.options = options
        # browser_setup.web_home_path = "/static/index.html"
        browser_setup.driver_path = properties.DRIVER_LINUX_PATH
    elif properties.OS_MAC in platform:
        print(properties.OS_MAC)
        options = Options()
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        browser_setup.options = options
        # browser_setup.web_home_path = "/static/index.html"
        browser_setup.driver_path = properties.DRIVER_MAC_PATH
    elif properties.OS_WINDOW in platform:
        print(properties.OS_WINDOW)
        options = Options()
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        options.add_argument(properties.USER_DATA_DIR)
        browser_setup.options = options
        # browser_setup.web_home_path = "\\static\\index.html"
        browser_setup.driver_path = properties.DRIVER_WINDOWS_PATH
    else:
        raise UnsupportedPlatform

    return browser_setup
