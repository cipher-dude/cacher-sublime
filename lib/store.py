store = {
    "logged_in": False,
    "personal_library": None,
    "teams": [],
    "snippets": []
}


def get_val(key):
    return store[key]


def set_val(key, val):
    store[key] = val
