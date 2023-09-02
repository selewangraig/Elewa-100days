# Variables
users = ["UserA", "UserB", "UserC"]
systems = ["SystemX", "SystemY", "SystemZ"]
permissions = {user: {system: "None" for system in systems} for user in users}

# Initialize permissions (sample permissions)
permissions["UserA"]["SystemX"] = "Read"
permissions["UserA"]["SystemZ"] = "Admin"
permissions["UserB"]["SystemY"] = "Write"
permissions["UserC"]["SystemX"] = "Read"

# Simulate a process to modify permissions (you can adapt this as needed)
def modify_permissions(user, system, new_permission):
    permissions[user][system] = new_permission
    print(f"Permission for {user} on {system} is now set to: {new_permission}")

# Nested for loops to manage permissions
for user in users:
    for system in systems:
        current_permission = permissions[user][system]
        
        # Simulate modifying permissions (you can replace this with your real process)
        if current_permission == "None":
            new_permission = "Read"
            modify_permissions(user, system, new_permission)
        elif current_permission == "Read":
            new_permission = "Write"
            modify_permissions(user, system, new_permission)
        elif current_permission == "Write":
            new_permission = "Admin"
            modify_permissions(user, system, new_permission)
        elif current_permission == "Admin":
            new_permission = "None"
            modify_permissions(user, system, new_permission)

# Display updated user permissions
print("\nUpdated User Permissions:")
for user, system_permissions in permissions.items():
    print(f"{user} Permissions:")
    for system, permission in system_permissions.items():
        print(f"- {system}: {permission}")