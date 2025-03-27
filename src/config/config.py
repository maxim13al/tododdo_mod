import os
from dotenv import load_dotenv


load_dotenv()

AUTOMATION_NAME = "uiautomator2"
PLATFORM_NAME = "Android"

BS_USER_NAME = os.getenv("BS_USER_NAME")
BS_ACCESS_KEY = os.getenv("BS_ACCESS_KEY")
BS_APP_ID = os.getenv("BS_APP_ID")

REAL_DEVICE_NAME = "Android"
EMULATOR_DEVICE_NAME = "emulator-5554"
EMULATOR_AVD = "Pixel_XL_API_30"

APP_PACKAGE = "com.mdev.tododo"
APP_ACTIVITY = "com.mdev.tododo.ui.MainActivity"

LOCAL_SERVER = "http://localhost:4723"
REMOTE_SERVER = "hub-cloud.browserstack.com/wd/hub"

BS_DEVICE_NAME = "Samsung Galaxy S21"
BS_OS_VERSION = 11
BS_PROJECT_NAME = "Tododo_project"
BS_BUILD_NAME = "Tododo_build"
BS_NAME = "New_auto_test"

NEW_COMMAND_TIMEOUT = 30
WAIT_FOR_IDLE_TIMEOUT = 1
