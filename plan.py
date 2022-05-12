"""Data class for Northstar EPE Planner API."""

# Standard library
from typing import Optional
import json

# Third Party
from pydantic import BaseModel
import requests


class Plan(BaseModel):
    """Data class object for Northstar EPE Planner Project."""

    name: str
    project_index: Optional[int] = 0
    baseurl = "https://northstar.net:8086/epe-plan"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "userID": "python",
    }

    def create_project(self):
        """Create a new project."""

        try:
            response = requests.request(
                "POST",
                self.baseurl,
                headers=self.headers,
                data=json.dumps({"name": self.name}),
            )
            response.raise_for_status()

            if response.status_code == 202:
                index = response.json()
                self.project_index = index["projectIndex"]

                return response

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error

    def create_changes(self, changes):
        """Changes for our project."""

        try:
            response = requests.request(
                "POST",
                self.baseurl + f"/{self.project_index}/plan-changes",
                headers=self.headers,
                data=json.dumps(changes),
            )
            response.raise_for_status()
            if response.status_code == 202:
                return response

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error

    def create_steps(self, steps):
        """Create steps for our changes."""

        try:
            response = requests.request(
                "POST",
                self.baseurl + f"/{self.project_index}/plan-changes/0/steps",
                headers=self.headers,
                data=json.dumps(steps),
            )
            response.raise_for_status()
            if response.status_code == 201:
                return response

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error

    def delete_project(self, project_id):
        """Delete a project."""

        try:
            response = requests.request(
                "DELETE",
                self.baseurl + f"/{project_id}",
                headers=self.headers,
            )
            response.raise_for_status()
            self.project_index = 0

            return response

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error

    def execute(self, execution):
        """Execute our changes."""

        try:
            response = requests.request(
                "POST",
                self.baseurl + f"/{self.project_index}/plan-changes/0/exec",
                headers=self.headers,
                data=json.dumps(execution),
            )
            response.raise_for_status()
            if response.status_code == 202:
                return response

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error

    def get_projects(self):
        """Get all projects."""

        try:
            response = requests.request(
                "GET",
                self.baseurl,
                headers=self.headers,
            )
            response.raise_for_status()
            projects = response.json()

            return projects

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error

    def get_project_id(self, project_id):
        """Get project by ID."""

        try:
            response = requests.request(
                "GET",
                self.baseurl + f"/{self.project_index}/{project_id}",
                headers=self.headers,
            )
            response.raise_for_status()
            project = response.json()

            return project

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error

    def select_network(self, network_id):
        """Update our settings to select a specific network."""

        try:
            response = requests.request(
                "PUT",
                self.baseurl + "/settings",
                headers=self.headers,
                data=json.dumps({"simulateNorthstarNetworkName": network_id}),
            )
            response.raise_for_status()

            return f"Project has selected the network {network_id}"

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error
