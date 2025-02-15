# Enhanced AI Chatbot

This project implements an enhanced AI chatbot using the `transformers` library from Hugging Face. The chatbot uses the FLAN-T5 model from Google for sequence-to-sequence language modeling.

## Flow

1. **User Input**: The user provides input through the chat interface.
2. **PromptHandler**: The input is formatted by the `PromptHandler` to guide the model.
3. **Tokenizer**: The formatted input is tokenized by the `Tokenizer`.
4. **Model**: The tokens are fed into the model to generate a response.
5. **ResponseCleaner**: The model's output is cleaned by the `ResponseCleaner`.
6. **Clean Response**: The cleaned response is presented to the user.

### Detailed Flow

1. **User Input**:
   - The user types a message in the chat interface.

2. **PromptHandler**:
   - The `PromptHandler` formats the input to provide context and guide the model.
   - Example: Adding prefixes like "User:" and "AI:" to structure the conversation.

3. **Tokenizer**:
   - The `Tokenizer` converts the formatted input into tokens that the model can understand.
   - It handles truncation, padding, and conversion to tensor format.

4. **Model**:
   - The tokens are fed into the FLAN-T5 model to generate a response.
   - The model uses the generation parameters defined in `ModelConfig` to produce the output.

5. **ResponseCleaner**:
   - The `ResponseCleaner` processes the model's output to remove extra whitespace, ensure proper capitalization, and add punctuation if needed.

6. **Clean Response**:
   - The cleaned response is displayed to the user in the chat interface.

## Benefits

- **Improved Response Quality**: The `PromptHandler` and `ResponseCleaner` enhance the quality and relevance of the responses.
- **Configurable**: The chatbot's behavior can be easily adjusted through the `ModelConfig` class.
- **Modular Design**: The code is organized into separate modules, making it easy to maintain and extend.
- **Logging**: Comprehensive logging helps in monitoring and debugging the chatbot's performance.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `transformers` library
- `torch` library

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/chatbot_project.git
   cd chatbot_project