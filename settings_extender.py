
# ----------------- Dynamic Settings -----------------
# These settings are dynamically set by the integrator

# Application definition
GIDEON_CONNECT_KEY = ENVIRONMENT_VARIABLES.get("GIDEON_CONNECT_KEY", "")
GIDEON_URI = ENVIRONMENT_VARIABLES.get("GIDEON_URI", "")  # gideon's url
GIDEON_HOST_URI = ENVIRONMENT_VARIABLES.get(
    "GIDEON_HOST_URI", "")  # your url where the server is live

LOADER_APP_NAME = "app"
LOADER_FILE_NAME = "loader"
LOADER_LOCATION = BASE_DIR / LOADER_APP_NAME / f"{LOADER_FILE_NAME}.py"

DYNAMIC_APPS = []
DYNAMIC_APP_NAMES = []

DEBUG = False
ALLOWED_HOSTS = ["*"]

APP_NAME = "Routine-bot"

INSTALLED_APPS += [
    "gidconnect",
]
