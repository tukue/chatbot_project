class PromptHandler:
    def __init__(self):
        self.task_prefixes = {
            "explanation": "Please provide a detailed explanation: ",
            "comparison": "Compare and contrast: ",
            "list": "Provide a comprehensive list: ",
            "default": "Respond to this: "
        }

    def format_prompt(self, text):
        # Detect question type
        if "?" in text:
            if any(word in text.lower() for word in ["what", "why", "how", "explain"]):
                prefix = self.task_prefixes["explanation"]
            elif any(word in text.lower() for word in ["compare", "difference", "versus"]):
                prefix = self.task_prefixes["comparison"]
            elif any(word in text.lower() for word in ["list", "what are"]):
                prefix = self.task_prefixes["list"]
            else:
                prefix = self.task_prefixes["default"]
        else:
            prefix = self.task_prefixes["default"]

        return f"{prefix}{text}"
