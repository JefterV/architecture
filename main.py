# EXTERNAL IMPORTS
import uvicorn

# NATIVE IMPORTS

# INTERNAL IMPORTS
from src.api import CreateAPP
from src.infrastructures.settings.infrastructure import SettingsInfrastructure

settings = SettingsInfrastructure.get_settings()
app = CreateAPP().get_app()

if __name__ == "__main__":
    params = {"host": "0.0.0.0", "port": 8000}
    if settings.ENVIRONMENT == "prd":
        params["root_path"] = "/pixer"
    uvicorn.run(app, **params)
