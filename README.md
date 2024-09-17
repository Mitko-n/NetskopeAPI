# Netskope API Client

This repository contains a Python client for interacting with Netskope's API. It includes two main classes, `Policy` and `Scim`, for handling different types of API interactions.

## Installation

Make sure you have `requests` library installed. You can install it using pip if you don't have it already:

```bash
pip install requests
```

## Usage

### Initialization

You need to load your API credentials from a JSON file and initialize the `Policy` or `Scim` client with the base URL and authentication token.

```python
import json
from NetskopeAPI import Policy, Scim

# Define constants for tenant, base URL, and authentication token
TENANT = "TENANT"
BASE_URL = f"https://{TENANT}.goskope.com/api/v2"
AUTH_TOKEN = "AUTH_TOKEN"
```

### Policy Class

The `Policy` class handles operations related to policies in the Netskope API.\

**THIS IS BAD EXAMPLES HAVE TO CHECK THEY DO NOT WORK**

#### Creating an instance

```python
from NetskopeAPI import Policy

policy_client = Policy(base_url=BASE_URL, auth_token=AUTH_TOKEN)
```

#### Example 1: Create a Domain Fronting Exception

```python
data = {
    "name": "example.com",
    "description": "Example domain",
}
response = policy_client.create_domain_fronting_exception(data)
print("Create Domain Fronting Exception Response:")
print(json.dumps(response, indent=4))
```

#### Example 2: Read All Domain Fronting Exceptions

```python
response = policy_client.read_domain_fronting_exceptions()
print("All Domain Fronting Exceptions:")
print(json.dumps(response, indent=4))
```

#### Example 3: Read a Domain Fronting Exception by ID

```python
exception_id = "example-id"
response = policy_client.read_domain_fronting_exception_by_id(exception_id)
print(f"Domain Fronting Exception {exception_id} Details:")
print(json.dumps(response, indent=4))
```

#### Example 4: Update a Domain Fronting Exception

```python
exception_id = "example-id"
data = {
    "description": "Updated description for domain",
}
response = policy_client.update_domain_fronting_exception(exception_id, data)
print(f"Update Domain Fronting Exception {exception_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 5: Delete a Domain Fronting Exception by ID

```python
exception_id = "example-id"
response = policy_client.delete_domain_fronting_exception_by_id(exception_id)
print(f"Delete Domain Fronting Exception {exception_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 6: Create an NPA Policy

```python
data = {
    "name": "Example NPA Policy",
    "rules": [
        # NPA policy rules here
    ],
}
response = policy_client.create_npa_policy(data)
print("Create NPA Policy Response:")
print(json.dumps(response, indent=4))
```

#### Example 7: Read All NPA Policies

```python
response = policy_client.read_npa_policies()
print("All NPA Policies:")
print(json.dumps(response, indent=4))
```

#### Example 8: Read a Specific NPA Policy

```python
npa_policy_id = "example-id"
response = policy_client.read_npa_policy(npa_policy_id)
print(f"NPA Policy {npa_policy_id} Details:")
print(json.dumps(response, indent=4))
```

#### Example 9: Update an NPA Policy

```python
npa_policy_id = "example-id"
data = {
    "rules": [
        # Updated NPA policy rules here
    ],
}
response = policy_client.update_npa_policy(npa_policy_id, data)
print(f"Update NPA Policy {npa_policy_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 10: Delete an NPA Policy

```python
npa_policy_id = "example-id"
response = policy_client.delete_npa_policy(npa_policy_id)
print(f"Delete NPA Policy {npa_policy_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 11: Create a URL List

```python
data = {
    "name": "Example URL List",
    "urls": [
        "http://example.com",
    ],
}
response = policy_client.create_url_list(data)
print("Create URL List Response:")
print(json.dumps(response, indent=4))
```

#### Example 12: Read All URL Lists

```python
response = policy_client.read_all_url_lists()
print("All URL Lists:")
print(json.dumps(response, indent=4))
```

#### Example 13: Read a URL List by ID

```python
url_list_id = "example-id"
response = policy_client.read_url_list_by_id(url_list_id)
print(f"URL List {url_list_id} Details:")
print(json.dumps(response, indent=4))
```

#### Example 14: Update a URL List

```python
url_list_id = "example-id"
data = {
    "urls": [
        "http://updated-example.com",
    ],
}
response = policy_client.update_url_list(url_list_id, "update", data)
print(f"Update URL List {url_list_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 15: Delete a URL List

```python
url_list_id = "example-id"
response = policy_client.delete_url_list(url_list_id)
print(f"Delete URL List {url_list_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 16: Replace a URL List

```python
url_list_id = "example-id"
data = {
    "name": "Replaced URL List",
    "urls": [
        "http://replaced-example.com",
    ],
}
response = policy_client.replace_url_list(url_list_id, data)
print(f"Replace URL List {url_list_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 17: Upload a URL List Configuration

```python
file_path = "./path/to/url_list_config.json"
response = policy_client.upload_url_list_config(file_path)
print("Upload URL List Configuration Response:")
print(json.dumps(response, indent=4))
```

#### Example 18: Apply Pending URL Changes

```python
response = policy_client.apply_pending_url_changes()
print("Apply Pending URL Changes Response:")
print(json.dumps(response, indent=4))
```

### Scim Class

The `Scim` class handles operations related to users and groups in the Netskope API.

#### Creating an instance

```python
from NetskopeAPI import Scim

scim_client = Scim(base_url=BASE_URL, auth_token=AUTH_TOKEN)
```

#### Example 1: Create a New User

```python
new_user_data = {
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "netskope.test.new@outlook.com",
    "name": {
        "familyName": "Netskope",
        "givenName": "Test",
    },
    "active": True,
    "emails": [
        {
            "value": "netskope.test.new@outlook.com",
            "primary": True,
        }
    ],
}
response = scim_client.create_user(data=new_user_data)
print("Create User Response:")
print(json.dumps(response, indent=4))
```

#### Example 2: Read All Users

```python
response = scim_client.read_users()
print("Read Users Response:")
print(json.dumps(response, indent=4))
```

#### Example 3: Read a Specific User

```python
user_id = response["data"][0]["id"]
response = scim_client.read_user(user_id)
print(f"Read User {user_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 4: Update a User

```python
updated_user_data = {
    "Operations": [
        {
            "op": "add",
            "path": "userName",
            "value": "new_upn"
        }
    ],
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    ]
}
response = scim_client.update_user(user_id, data=updated_user_data)
print(f"Update User {user_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 5: Delete a User

```python
response = scim_client.delete_user(user_id)
print(f"Delete User {user_id} Response:")
print(json.dumps(response, indent=4))
```

#### Example 6: Create a New Group

```python
new_group_data = {
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
    "displayName": "Test Group",
}
response = scim_client.create_group(data=new_group_data)
print("Create Group Response:")
print(json.dumps(response, indent=4))
```

#### Example 7: Read All Groups

```python
response = scim_client.read_groups()
print("Read Groups Response:")
print(json.dumps(response, indent=4))
```

#### Example 8: Read a Specific Group

```python
group_id = response["data"][0]["id"]
response = scim_client.read_group(group_id)
print(f"Read Group {group_id} Response:")
print(json.dumps(response, indent=4
```