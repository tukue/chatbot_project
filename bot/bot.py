from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from bot.utils.prompt_handler import PromptHandler
from bot.utils.response_cleaner import ResponseCleaner
from bot.utils.response_validator import ResponseValidator
from config.model_config import ModelConfig
import logging
import gc

class TunedFlanBot:
    def __init__(self):
        try:
            logging.info("Loading model...")
            self.config = ModelConfig()
            self.prompt_handler = PromptHandler()
            self.response_cleaner = ResponseCleaner()
            self.response_validator = ResponseValidator()
            
            self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_name)
            
            logging.info("Model loaded successfully!")
            
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")
            raise

    def get_response(self, text):
        try:
            formatted_input = self.prompt_handler.format_prompt(text)
            
            inputs = self.tokenizer(
                formatted_input,
                return_tensors="pt",
                truncation=True,
                max_length=self.config.max_input_length,
                padding=True
            )
            
            outputs = self.model.generate(
                **inputs,
                **self.config.generation_params
            )
            
            response = self.tokenizer.decode(
                outputs[0],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True
            )
            
            gc.collect()
            cleaned_response = self.response_cleaner.clean(response)
            
            if not self.response_validator.is_valid(cleaned_response):
                logging.warning("Generated response did not meet guardrails.")
                return "I'm sorry, I cannot provide a response to that."
            
            return cleaned_response
            
        except Exception as e:
            logging.error(f"Error generating response: {str(e)}")
            return f"Error: {str(e)}"

    def run(self):
        logging.info("Starting chat session...")
        print("\nEnhanced AI Chat (type 'quit' to exit)")
        print(self.config.get_help_message())
        
        while True:
            try:
                text = input("You: ").strip()
                
                if text.lower() == 'quit':
                    logging.info("Ending chat session...")
                    print("End chat session!")
                    break
                
                if not text:
                    print("Please enter a question or statement.")
                    continue
                
                response = self.get_response(text)
                print("\nAI:", response, "\n")
                
            except KeyboardInterrupt:
                logging.info("Chat session interrupted by user")
                print("\nEnd chat session!")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {str(e)}")
                print(f"An error occurred: {str(e)}")