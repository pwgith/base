
# Manage My Memberships
* Can remove self from orgs so that user is no longer a member
* Can confirm or delete invitations to Orgs
* Can create a new org - user will be admin

```mermaid
sequenceDiagram
    participant UI
    participant API Gateway
    participant Cognito
    participant Lambda
    participant DB
    participant Email Server

    UI->>API Gateway: Get my orgs
    API Gateway->>Cognito: Check token
    API Gateway->>Lambda: Get orgs user belongs to
    Lambda->>DB: Get orgs user belongs to
    UI->>API Gateway: Update my orgs
    API Gateway->>Cognito: Check token
    API Gateway->>Lambda: Update orgs user belongs to
    Lambda->>DB: Add org - Update orgs user belongs to
    Lambda->>Email Server: Send email to confirm
    Lambda->>Email Server: Notify org owner 
```

# Manage Organisation
* Must be an admin of the org
* Can send an invitation to a user to be a part of an organisation
* Can assign or unassign admin role to existing confirmed members
  * There must always be at least one admin
  * Can remove self as admin
* Can remove a member from an organisation
* Can delete an organisation

```mermaid
sequenceDiagram
    participant UI
    participant API Gateway
    participant Cognito
    participant Lambda
    participant DB
    participant Email Server

    UI->>API Gateway: Get memberships for orgs I'm an admin of
    API Gateway->>Cognito: Check token
    API Gateway->>Lambda: Get memberships for orgs
    Lambda->>Lambda: Check token authority
    Lambda->>DB: Get memberships for orgs
    UI->>API Gateway: Update org members
    API Gateway->>Cognito: Check token
    API Gateway->>Lambda: Update org members
    Lambda->>Lambda: Check token authority
    Lambda->>DB: Get impacted member
    Lambda->>Lambda: Check operation is valid
    Lambda->>DB: Update org members
    Lambda->>Email Server: Send email to each impacted user
```
