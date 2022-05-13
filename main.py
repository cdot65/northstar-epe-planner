"""
Manage an EPE project's planning, changes, steps, and execution.
"""

# Standard library imports
import time

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

    # create project object, passing in `project_name` as kwargs
    project = Plan(**epe["project_name"])

    # execute the creation of our project
    project.create_project()
    ipdb.set_trace(context=5)

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
