class ModelConfig:
    def __init__(self):
        self.model_name = "google/flan-t5-small"
        self.max_input_length = 512
        
        self.generation_params = {
            "max_length": 150,
            "min_length": 20,
            "num_return_sequences": 1,
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
            "no_repeat_ngram_size": 2,
            "early_stopping": True,
            "do_sample": True,
            "length_penalty": 1.0,
            "repetition_penalty": 1.2
        }

    def get_help_message(self):
        return """
Tips:
- Ask clear, specific questions
- Add context to your questions
- Use 'explain', 'compare', or 'list' for better responses
"""
