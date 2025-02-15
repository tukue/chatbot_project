import os
import sys
import logging

# Add project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from bot.bot import TunedFlanBot  # Changed from LightFlanBot to TunedFlanBot

# Setup logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/chat.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    try:
        bot = TunedFlanBot()  # Changed from LightFlanBot to TunedFlanBot
        bot.run()
    except Exception as e:
        logging.error(f"Failed to initialize bot: {str(e)}")
        print(f"Failed to start the chatbot: {str(e)}")

if __name__ == "__main__":
    main()
