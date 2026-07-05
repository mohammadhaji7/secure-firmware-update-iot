users = {
    "admin": {
        "role": "Administrator"
    },
    "operator": {
        "role": "Operator"
    },
    "viewer": {
        "role": "Viewer"
    }
}

permissions = {
    "Administrator": [
        "upload firmware",
        "approve update",
        "view logs",
        "manage users"
    ],

    "Operator": [
        "schedule updates",
        "view logs"
    ],

    "Viewer": [
        "view logs"
    ]
}

username = input("Enter username: ")

if username in users:

    role = users[username]["role"]

    print(f"\nUser: {username}")
    print(f"Assigned Role: {role}")

    print("\nAllowed Permissions:")

    for permission in permissions[role]:
        print(f"- {permission}")

else:
    print("\nAccess Denied.")
    print("Unknown user.")
