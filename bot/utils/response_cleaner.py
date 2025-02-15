class ResponseCleaner:
    def clean(self, response):
        # Remove extra whitespace
        response = " ".join(response.split())
        
        # Ensure proper capitalization
        response = response[0].upper() + response[1:]
        
        # Add period if missing
        if response and response[-1] not in ".!?":
            response += "."
            
        return response
