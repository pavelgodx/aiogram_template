
This is a ready-to-use Telegram bot template with a clean project structure. You can customize it however you like. Follow these steps to get it running:
---
1. **Clone this repository**  
Clone the current repo to your local machine.

2. **Create a `.env` file**  
In the root directory, create a `.env` file and add the following variables:
```
API_BOT_KEY=123456789:AaBbCcDdEeFf  # your bot token from @BotFather  
ADMINS=[7777777777,6666666666]                  # your telegram user ID
```

4. **Set up a virtual environment**  
Run this command in the root folder:
`python3 -m venv venv`

5. **Activate the virtual environment**  
- `source venv/bin/activate` (macOS/Linux) / `venv\Scripts\activate` (Windows)

7. **Install the dependencies**  
Use pip to install the required libraries:
`pip3 install -r requirements.txt`

8. **Run the bot**  
Launch the bot with:
`python3 main.py`
