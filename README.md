# sigma-rules
Project for collecting and displaying sigma rules.

*Python Version used: 3.10.2*
## Python Development Setup
This part lists  all the tutorials, which were used to setup the python developer environment.
* **[VS Code- Getting Started](https://code.visualstudio.com/docs/python/python-tutorial)**

* **[Virtual Enviroment Setup](https://code.visualstudio.com/docs/python/environments#_global-virtual-and-conda-environments)**

    * [Python Docs](https://docs.python.org/3/library/venv.html) 
    * Command used to install a virtual environment with the chosen python version 
        * ``` C:/Users/"USERNAME HERE"/AppData/Local/Programs/Python/Python310/python -m venv ./.venv ```
    * `"terminal.integrated.inheritEnv": false,` → needs to be added to the settings.json of vs code. So it doesn't use the Python environment of the current system.
    * Package Management
        * `python -m pip install boto3` → install packages
        * `pip freeze > requirements.txt` → to get a list of all installed packages
        * `pip install -r requirements.txt` → to install all needed packages
        * `python -m pip install pip-autoremove` → must have packge
        * `python ./comment-crawler/.venv/Scripts/pip_autoremove.py boto3` → to remove a package and all of its dependencies 

* **YouTube Data API v3**
    * This [Guide](https://developers.google.com/youtube/v3/getting-started#intro) for getting started with the Google Cloud Platform, setting up a project there and the generating an API key 
    * Installed [Google API Python Client](https://github.com/googleapis/google-api-python-client) for easier API usage (**cmd:** `pip install google-api-python-client`)
