def success(data=None, message="Success"):
    return {
        "success": True,
        "data": data,
        "message": message,
    }


def error(message="Error"):
    return {
        "success": False,
        "data": None,
        "message": message,
    }
