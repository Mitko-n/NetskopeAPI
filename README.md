Here’s the updated `README.md` with `NskBase` renamed to `NetskopeAPIBase`:

# Netskope API Client

This repository contains a Python client for interacting with the Netskope API. It includes a base class `NetskopeAPIBase` for making HTTP requests and two subclasses `Policy` and `Scim` for specific API functionalities related to policies and SCIM operations, respectively.

## Overview

- **`NetskopeAPIBase`**: The base class for making HTTP requests with automatic retry handling and consistent response structures.
- **`Policy`**: Provides methods for interacting with Netskope policy endpoints.
- **`Scim`**: Provides methods for interacting with SCIM endpoints related to users and groups.

## Installation

Ensure you have the `requests` library installed:

```bash
pip install requests
```

## Usage

### NetskopeAPIBase

The `NetskopeAPIBase` class provides a unified way to perform HTTP requests. It automatically handles retries for failed requests and provides a consistent response structure.

#### Example

```python
from nsk_client import NetskopeAPIBase, Policy, Scim

# Initialize NetskopeAPIBase
base_url = "https://api.example.com"
headers = {"Authorization": "Bearer YOUR_API_TOKEN"}

client = NetskopeAPIBase(base_url, headers=headers)

# Perform a GET request
response = client.get("some/endpoint")
print(response)

# Close the session when done
client.close()
```

### Policy

The `Policy` class extends `NetskopeAPIBase` and provides methods for managing policy-related resources.

#### Example

```python
from nsk_client import Policy

# Initialize Policy client
policy_client = Policy(base_url, auth_token="YOUR_API_TOKEN")

# Get all domain fronting exceptions
response = policy_client.get_domain_fronting_exceptions()
print(response)

# Create a new domain fronting exception
data = {"some": "data"}
response = policy_client.create_domain_fronting_exception(data)
print(response)

# Delete a domain fronting exception by ID
response = policy_client.delete_domain_fronting_exception_by_id(id="12345")
print(response)
```

### Scim

The `Scim` class extends `NetskopeAPIBase` and provides methods for managing SCIM resources such as users and groups.

#### Example

```python
from nsk_client import Scim

# Initialize Scim client
scim_client = Scim(base_url, auth_token="YOUR_API_TOKEN")

# Get a list of users
response = scim_client.get_users()
print(response)

# Create a new user
user_data = {"name": "John Doe", "email": "john.doe@example.com"}
response = scim_client.create_user(user_data)
print(response)

# Delete a user by ID
response = scim_client.delete_user(id_value="12345")
print(response)
```

## Methods

### `NetskopeAPIBase`

- **`get(endpoint, params=None, headers=None, display_output=False)`**: Perform a GET request.
- **`post(endpoint, data=None, headers=None, files=None, display_output=False)`**: Perform a POST request.
- **`put(endpoint, data=None, headers=None, display_output=False)`**: Perform a PUT request.
- **`delete(endpoint, display_output=False)`**: Perform a DELETE request.
- **`patch(endpoint, data=None, headers=None, display_output=False)`**: Perform a PATCH request.
- **`close()`**: Close the session.

### `Policy`

- **`get_domain_fronting_exceptions(display_output=False)`**
- **`get_domain_fronting_exception_by_id(id, display_output=False)`**
- **`create_domain_fronting_exception(data, display_output=False)`**
- **`update_domain_fronting_exception(id, data, display_output=False)`**
- **`delete_domain_fronting_exception_by_id(id, display_output=False)`**
- **`get_npa_policies(display_output=False)`**
- **`get_npa_policy(id, display_output=False)`**
- **`create_npa_policy(data, display_output=False)`**
- **`patch_npa_policy(id, data, display_output=False)`**
- **`delete_npa_policy(id, display_output=False)`**
- **`get_all_url_lists(display_output=False)`**
- **`get_url_list_by_id(id, display_output=False)`**
- **`create_url_list(data, display_output=False)`**
- **`upload_url_list_config(file_path, display_output=False)`**
- **`patch_url_list(id, action, data=None, display_output=False)`**
- **`replace_url_list(id, data, display_output=False)`**
- **`delete_url_list(id, display_output=False)`**
- **`apply_pending_url_changes(display_output=False)`**

### `Scim`

- **`get_users(display_output=False)`**
- **`get_user(id_value, display_output=False)`**
- **`create_user(data, display_output=False)`**
- **`replace_user(id_value, data, display_output=False)`**
- **`update_user(id_value, data, display_output=False)`**
- **`delete_user(id_value, display_output=False)`**
- **`get_groups(display_output=False)`**
- **`get_group(id_value, display_output=False)`**
- **`create_group(data, display_output=False)`**
- **`replace_group(id_value, data, display_output=False)`**
- **`update_group(id_value, data, display_output=False)`**
- **`delete_group(id_value, display_output=False)`**
- **`get_resource_types(display_output=False)`**
- **`get_resource_type(id_value, display_output=False)`**
- **`get_schemas(display_output=False)`**

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `"YOUR_API_TOKEN"` and `"https://api.example.com"` with your actual values as needed. Adjust the `import` statements based on your module structure.