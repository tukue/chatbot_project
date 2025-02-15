import re

class ResponseValidator:
    def __init__(self):
        self.inappropriate_content_patterns = [
            re.compile(r'\b(?:inappropriate|offensive|prohibited)\b', re.IGNORECASE)
        ]

    def is_valid(self, response):
        # Check if the response is empty
        if not response.strip():
            return False
        
        # Check for inappropriate content
        for pattern in self.inappropriate_content_patterns:
            if pattern.search(response):
                return False
        
        return True