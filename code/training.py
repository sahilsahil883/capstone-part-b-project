training_modules = {
    "phishing_awareness": {
        "title": "Phishing Awareness",
        "content": "Learn how to identify fake emails and malicious links."
    }
}

def access_module(user, module_name):
    if user.has_permission("view_modules"):
        return training_modules.get(module_name, "Module not found")
    else:
        return "Access denied"