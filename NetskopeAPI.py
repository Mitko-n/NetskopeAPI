import json
import requests
from requests.adapters import Retry, HTTPAdapter
from requests.exceptions import RequestException


class Base:
    def __init__(self, base_url, headers=None, retries=5, backoff_factor=2):
        self._base_url = base_url
        self._headers = headers or {}
        self._session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(
            total=retries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
            backoff_factor=backoff_factor,
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._session.mount("https://", adapter)
        self._session.mount("http://", adapter)

    def _request(self, method, endpoint, headers=None, **kwargs):
        """Unified request method with consistent output structure."""
        status_messages = {
            200: "Request successful",
            201: "Resource created successfully.",
            204: "No content, action completed successfully.",
            400: "Bad request. Please check your input parameters.",
            401: "Unauthorized. Please check your authentication credentials.",
            403: "Forbidden. You don't have permission to access this resource.",
            404: "Resource not found. The specified resource could not be located.",
            405: "Method not allowed. Please check if the HTTP method is correct for this resource.",
            408: "Request timeout. The server took too long to respond.",
            409: "Conflict. There was a conflict with the request, such as a resource already existing.",
            413: "Payload too large. The request body exceeds the server's size limit.",
            414: "URI too long. The requested URI exceeds the server's length limit.",
            429: "Too many requests. Please slow down and try again later.",
        }

        try:
            headers = headers or self._headers
            response = self._session.request(method, f"{self._base_url}/{endpoint}", headers=headers, **kwargs)
            status_code = response.status_code

            if status_code in status_messages:
                if status_code == 204:
                    return {"status": "success", "message": status_messages[status_code], "data": None}
                else:
                    try:
                        json_response = response.json()
                        return {
                            "status": "success" if status_code == 200 or status_code == 201 else "error",
                            "message": status_messages.get(status_code, "Operation successful."),
                            "data": json_response,
                        }
                    except ValueError:
                        return {
                            "status": "error",
                            "message": "Response is not in JSON format.",
                            "data": response.content.decode("utf-8"),
                        }

            if 400 <= status_code < 500:
                try:
                    json_response = response.json()
                    return {
                        "status": "error",
                        "message": json_response.get("detail", status_messages.get(status_code, "Client error occurred.")),
                        "data": {"details": json_response.get("detail", "Client error occurred."), "schemas": json_response.get("schemas", []), "status": status_code},
                    }
                except ValueError:
                    return {
                        "status": "error",
                        "message": status_messages.get(status_code, "Client error occurred."),
                        "data": {"details": response.content.decode("utf-8"), "schemas": [], "status": status_code},
                    }

            return {
                "status": "error",
                "message": f"Unexpected response format (status code: {status_code}).",
                "data": response.content.decode("utf-8"),
            }

        except requests.HTTPError as http_err:
            return {"status": "error", "message": f"HTTP error occurred: {str(http_err)}", "data": None}
        except RequestException as req_err:
            return {"status": "error", "message": f"Request error occurred: {str(req_err)}", "data": None}
        except Exception as e:
            return {"status": "error", "message": f"An unexpected error occurred: {str(e)}", "data": None}

    def create(self, endpoint, data=None, headers=None, files=None):
        return self._request("POST", endpoint, headers=headers, json=data, files=files)

    def read(self, endpoint, params=None, headers=None):
        return self._request("GET", endpoint, headers=headers, params=params)

    def update(self, endpoint, data=None, headers=None):
        return self._request("PATCH", endpoint, headers=headers, json=data)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)

    def replace(self, endpoint, data=None, headers=None):
        return self._request("PUT", endpoint, headers=headers, json=data)

    def close(self):
        """Close the session."""
        if self._session:
            self._session.close()
            self._session = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


# Policy Class


class Policy(Base):
    def __init__(self, base_url, auth_token, headers=None):
        super().__init__(base_url, headers)
        self._headers.update({"Netskope-Api-Token": auth_token, "accept": "application/json"})

    # DOMAIN

    def create_domain_fronting_exception(self, data):
        return self.create("policy/domainfrontings", data=data)

    def read_domain_fronting_exceptions(self):
        return self.read("policy/domainfrontings")

    def read_domain_fronting_exception_by_id(self, id):
        return self.read(f"policy/domainfrontings/{id}")

    def update_domain_fronting_exception(self, id, data):
        return self.update(f"policy/domainfrontings/{id}", data=data)

    def delete_domain_fronting_exception_by_id(self, id):
        return self.delete(f"policy/domainfrontings/{id}")

    # NPA

    def create_npa_policy(self, data):
        return self.create("policy/npa/rules", data=data)

    def read_npa_policies(self):
        return self.read("policy/npa/rules")

    def read_npa_policy(self, id):
        return self.read(f"policy/npa/rules/{id}")

    def update_npa_policy(self, id, data):
        return self.update(f"policy/npa/rules/{id}", data=data)

    def delete_npa_policy(self, id):
        return self.delete(f"policy/npa/rules/{id}")

    # URL

    def create_url_list(self, data):
        return self.create("policy/urllist", data=data)

    def read_all_url_lists(self):
        return self.read("policy/urllist")

    def read_url_list_by_id(self, id):
        return self.read(f"policy/urllist/{id}")

    def update_url_list(self, id, action, data=None):
        return self.update(f"policy/urllist/{id}/{action}", data=data)

    def delete_url_list(self, id):
        return self.delete(f"policy/urllist/{id}")

    def replace_url_list(self, id, data):
        return self.replace(f"policy/urllist/{id}", data=data)

    def upload_url_list_config(self, file_path):
        with open(file_path, "rb") as file:
            return self.create("policy/urllist/file", files={"file": file})

    def apply_pending_url_changes(self):
        return self.create("policy/urllist/deploy")


# Scim Class


class Scim(Base):
    def __init__(self, base_url, auth_token, headers=None):
        super().__init__(base_url, headers)
        self._headers.update({"Netskope-Api-Token": auth_token, "Accept": "application/json"})

    # USER/S

    def create_user(self, data):
        return self.create("scim/Users", data=data)

    def read_users(self):
        return self.read("scim/Users")

    def read_user(self, id_value):
        return self.read(f"scim/Users/{id_value}")

    def update_user(self, id_value, data):
        return self.update(f"scim/Users/{id_value}", data=data)

    def delete_user(self, id_value):
        return self.delete(f"scim/Users/{id_value}")

    def replace_user(self, id_value, data):
        return self.replace(f"scim/Users/{id_value}", data=data)

    # GROUP/S

    def create_group(self, data):
        return self.create("scim/Groups", data=data)

    def read_groups(self):
        return self.read("scim/Groups")

    def read_group(self, id_value):
        return self.read(f"scim/Groups/{id_value}")

    def update_group(self, id_value, data):
        return self.update(f"scim/Groups/{id_value}", data=data)

    def delete_group(self, id_value):
        return self.delete(f"scim/Groups/{id_value}")

    def replace_group(self, id_value, data):
        return self.replace(f"scim/Groups/{id_value}", data=data)
