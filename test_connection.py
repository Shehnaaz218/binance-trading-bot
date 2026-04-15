from bot.client import get_client
import os
from dotenv import load_dotenv

load_dotenv()

print("API KEY:", os.getenv("API_KEY")[:10], "...")  # partial print

client = get_client()

try:
    balance = client.futures_account_balance()
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed:", str(e))