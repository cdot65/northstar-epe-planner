# northstar-epe-planner

Python library to interface with Northstar's REST API to plan out egress-path-engineering of segment routing LSPs

## Configuration file

Northstar configuration is to be passed as a YAML file on your system.

`example.yaml`

```yaml
---
project:
    meta:
        name: "SparklingLincoln"
    changes:
        freeTrafficTest:
            type: "congestedPeerLink"
            minUseRatio: 0.1
        timeLimit: 10

    steps:
        type: "peerLink"
        asbrIndex: 5
        peerLinkIndex: 0

    execution:
        oustadingTrafficChangeLimit: 10
        timeLimit: 10
        progressInterval: 1

server:
    baseurl: "10.0.1.2:8443"
    validate_certs: False
    headers: 
        Authorization: "Basic base64sumOfUserPass="
        Content-Type: "application/json"
    auth:
        grant_type: "password"
        username: "admin"
        password: "jnpr!123"
```

## Execution

Pass your YAML file into your Python script arguments

`example.py`

```python
"""
Manage an EPE project's planning, changes, steps, and execution.
"""

# Standard library imports
import argparse
import time

# 3rd Party imports
import yaml

# Local imports
from northstar_epe_planner import NorthstarHelper


def main():
    """Main execution block."""

    # create project object, passing in YAML file objects
    x = NorthstarHelper(server=epe["server"], project=epe["project"])

    # execute the creation of our project
    x.create_project()

    # wait 5 seconds and then create the changes for our newly created plan
    time.sleep(5)
    x.create_changes(epe["changes"])
    x.create_steps(epe["steps"])
    x.execute(epe["execution"])

    return x


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Configuration Parameters")
    parser.add_argument(
        "--config", dest="config", type=str, help="path to configuration file"
    )
    args = parser.parse_args()

    # load contents of our config.yaml file into an object named `epe`
    with open(args.config, "r", encoding="utf-8") as file:
        epe = yaml.safe_load(file)

    main()
```
