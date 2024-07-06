import json

class ResponseData:
    def __init__(self, is_success=True, message="success", error_message="", detail=""):
        self.is_success = is_success
        self.message = message
        self.error_message = error_message
        self.detail = detail

    def to_dict(self):
        return {
            "is_success": self.is_success,
            "message": self.message,
            "error_message": self.error_message,
            "detail": self.detail
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return (f"ResponseData(is_success={self.is_success}, message={self.message}, "
                f"error_message={self.error_message}, detail={self.detail})")
