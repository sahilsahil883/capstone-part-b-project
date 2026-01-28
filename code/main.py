from users import User
from training import access_module
from logger import log_event

# Create users
admin = User("admin01", "admin")
employee = User("user01", "user")

# User accesses training
module = access_module(employee, "phishing_awareness")
print(module)

# Log activity
log_event(employee.username, "Accessed phishing awareness module")

# Admin reviews logs
if admin.has_permission("view_logs"):
    print("Admin is authorised to review logs.")