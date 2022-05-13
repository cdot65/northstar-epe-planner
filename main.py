"""
Manage an EPE project's planning, changes, steps, and execution.
"""

# Standard library imports
import time
import logging
import http.client as http_client

# 3rd Party imports
import ipdb
import yaml

# Local imports
from plan import Plan
from northstar import Northstar


def login(credentials):
    """Receive API token for session."""
    authenticate = Northstar(**credentials)

    return authenticate.create_token()


def main():
    """Main execution block."""

    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    # insert authorization into headers
    headers = epe["northstar"]["headers"]
    headers["Authorization"] = f"Bearer {auth_token}"

    # create project object, passing in `project_name` as kwargs
    project = Plan(
        baseurl=epe["northstar"]["baseurl"],
        token=auth_token,
        headers=headers,
        project_info=epe["project"]
    )

    ipdb.set_trace(context=5)

    # execute the creation of our project
    project.create_project()

    # wait 5 seconds and then create the changes for our newly created plan
    time.sleep(5)
    project.create_changes(epe["changes"])
    project.create_steps(epe["steps"])
    project.execute(epe["execution"])


if __name__ == "__main__":

    # load contents of our config.yaml file into an object named `epe`
    with open('config.yaml', 'r', encoding="utf-8") as file:
        epe = yaml.safe_load(file)

    auth_token = login(epe["northstar"])
    main()
