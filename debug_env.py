import os
from dotenv import load_dotenv

# Load from .env
load_dotenv(verbose=True)

print("=" * 60)
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("TAVILY_API_KEY:", os.getenv("TAVILY_API_KEY"))
print("=" * 60)

# Check file directly
print("\nDirect file read:")
with open('.env', 'r') as f:
    for line in f:
        if '=' in line:
            key, val = line.split('=', 1)
            print(f"{key.strip()}: {val.strip()[:30]}...")
