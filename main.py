"""
Manage an EPE project's planning, changes, steps, and execution.
"""

# Standard library imports
import logging
import http.client as http_client

# 3rd Party imports
import ipdb
import yaml

# Local imports
from northstar import NorthstarHelper


def main():
    """Main execution block."""

    # debug all HTTP operations
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    # create project object, passing in YAML file objects
    x = NorthstarHelper(server=epe["server"], project=epe["project"])

    ipdb.set_trace(context=5)

    # execute the creation of our project
    # x.create_project()

    # wait 5 seconds and then create the changes for our newly created plan
    # time.sleep(5)
    # x.create_changes(epe["changes"])
    # x.create_steps(epe["steps"])
    # x.execute(epe["execution"])

    return x


if __name__ == "__main__":

    # load contents of our config.yaml file into an object named `epe`
    with open("config.yaml", "r", encoding="utf-8") as file:
        epe = yaml.safe_load(file)

    main()
