## SCIM

1. **User Methods**\
   **Create User**
     ```python
     data = {
         "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
         "userName": "upn1",
         "name": {
             "familyName": "last_name",
             "givenName": "first_name"
         },
         "active": True,
         "emails": [
             {
                 "value": "email1@netskope.local",
                 "primary": True
             }
         ],
         "externalId": "User-Ext_id",
         "meta": {
             "resourceType": "User"
         }
     }
     scim.create_user(data)
     ```

   **Read Users**
     ```python
     scim.read_users()
     ```

   **Read User**
     ```python
     scim.read_user(id_value)
     ```

   **Update User**
     ```python
     data = {
         "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
         "Operations": [
             {
                 "path": "userName",
                 "op": "add",
                 "value": {"value": "new_upn"}
             }
         ]
     }
     scim.update_user(id_value, data)
     ```

   **Delete User**
     ```python
     scim.delete_user(id_value)
     ```

   **Replace User**
     ```python
     data = {
         "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
         "userName": "upn1",
         "name": {
             "familyName": "last_name",
             "givenName": "first_name"
         },
         "active": True,
         "emails": [
             {
                 "value": "email1@netskope.local",
                 "primary": True
             }
         ],
         "externalId": "User-Ext_id",
         "meta": {
             "resourceType": "User"
         }
     }
     scim.replace_user(id_value, data)
     ```

2. **Group Methods**\
   **Create Group**
     ```python
     data = {
         "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
         "displayName": "sample_group1",
         "members": [
             {"value": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}
         ],
         "externalId": "Group-Ext_id",
         "meta": {"resourceType": "Group"}
     }
     scim.create_group(data)
     ```

   **Read Groups**
     ```python
     scim.read_groups()
     ```

   **Read Group**
     ```python
     scim.read_group(id_value)
     ```

   **Update Group**
     ```python
     data = {
         "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
         "Operations": [
             {
                 "path": "members",
                 "op": "add",
                 "value": {"value": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}
             }
         ]
     }
     scim.update_group(id_value, data)
     ```

   **Delete Group**
     ```python
     scim.delete_group(id_value)
     ```

   **Replace Group**
     ```python
     data = {
         "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
         "displayName": "sample_group1",
         "members": [
             {"value": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}
         ],
         "externalId": "Group-Ext_id",
         "meta": {"resourceType": "Group"}
     }
     scim.replace_group(id_value, data)
     ```
## Policy

1. **Domain Fronting Exception Methods** - `**NOT TESTED**`\
   **Create**
     ```python
     data = {
         "name": "my-exception",
         "description": "my domain fronting description",
         "lists": ["199", "1978"]
     }
     policy.create_domain_fronting_exception(data)
     ```

   **Read**
     ```python
     policy.read_domain_fronting_exceptions()
     policy.read_domain_fronting_exception(id)
     ```

   **Update**
     ```python
     data = {
         "name": "my-exception",
         "description": "my domain fronting description",
         "lists": ["199", "1978"]
     }
     policy.update_domain_fronting_exception(id, data)
     ```

   **Delete**
     ```python
     policy.delete_domain_fronting_exception(id)
     ```

   **Replace**
     ```python
     data = {
         "name": "my-exception",
         "description": "my domain fronting description",
         "lists": ["199", "1978"]
     }
     policy.replace_domain_fronting_exception(id, data)
     ```

2. **NPA Policy Methods**- `**NOT TESTED**`\
   **Create**
     ```python
     data = {
         "name": "my-exception",
         "description": "my domain fronting description",
         "lists": ["199", "1978"]
     }
     policy.create_npa_policy(data)
     ```

   **Read**
     ```python
     policy.read_npa_policies()
     policy.read_npa_policy(id)
     ```

   **Update**
     ```python
     data = {
         "rule_name": "vantest",
         "description": "any",
         "rule_data": {
             "users": ["vphan@netskope.com"],
             "excludedUsers": ["someone@netskope.com"],
             "userType": "user",
             "access_method": "Client",
             "policy_type": "private-app",
             "privateApps": ["app1", "app2"],
             "privateAppIds": ["100", "201"],
             "privateAppTags": ["tag1", "tag2"],
             "privateAppTagIds": ["1", "2"],
             "privateAppsWithActivities": [{
                 "appName": "[172.31.12.135]",
                 "activities": [{
                     "activity": "any",
                     "list_of_constraints": []
                 }]
             }],
             "match_criteria_action": {
                 "action_name": "allow"
             },
             "classification": "string",
             "show_dlp_profile_action_table": True,
             "external_dlp": True,
             "net_location_obj": ["190.123.150.10", "190.218.0.0/16"],
             "b_negateNetLocation": True,
             "srcCountries": ["US", "AF", "CN"],
             "b_negateSrcCountries": True,
             "json_version": 3,
             "version": 1
         },
         "rule_order": 1,
         "group_id": "1"
     }
     policy.update_npa_policy(id, data)
     ```

   **Delete**
     ```python
     policy.delete_npa_policy(id)
     ```

   **Replace**
     ```python
     data = {
         "name": "my-exception",
         "description": "my domain fronting description",
         "lists": ["199", "1978"]
     }
     policy.replace_npa_policy(id, data)
     ```

3. **URL List Methods**\
   **Create**
     ```python
     data = {
         "name": "string",
         "data": {
             "urls": ["www.test.com"],
             "type": "exact"
         }
     }
     policy.create_url_list(data)
     ```

   **Read**
     ```python
     policy.read_all_url_lists()
     policy.read_url_list(id)
     ```

   **Update**
     ```python
     data = {
         "name": "string",
         "data": {
             "urls": ["www.test.com"],
             "type": "exact"
         }
     }
     policy.update_url_list(id, action, data)
     ```

   **Delete**
     ```python
     policy.delete_url_list(id)
     ```

   **Replace**
     ```python
     data = {
         "name": "string",
         "data": {
             "urls": ["www.test.com"],
             "type": "exact"
         }
     }
     policy.replace_url_list(id, data)
     ```

4. **Upload URL List Config**
   ```python
   policy.upload_url_list_config(file_path)
   ```

5. **Apply Pending URL Changes**
   ```python
   policy.apply_pending_url_changes()
   ```

