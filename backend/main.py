import os
from pathlib import Path
from dotenv import load_dotenv

# Load from the root .env file specifically
root_env = Path(__file__).resolve().parent.parent / '.env'
print(f"DEBUG: Attempting to load .env from {root_env}")
if root_env.exists():
    load_dotenv(dotenv_path=root_env)
    print("DEBUG: .env file found and loaded.")
else:
    print("DEBUG: .env file NOT FOUND at expected path!")
    load_dotenv() # Fallback

print(f"DEBUG: AWS_ACCESS_KEY_ID is {'SET' if os.getenv('AWS_ACCESS_KEY_ID') else 'MISSING'}", flush=True)
print(f"DEBUG: AWS_SECRET_ACCESS_KEY is {'SET' if os.getenv('AWS_SECRET_ACCESS_KEY') else 'MISSING'}", flush=True)

print("DEBUG: Importing routes.py...", flush=True)
from backend.routes import router
print("DEBUG: routes.py imported successfully.", flush=True)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TraceAI - AI Mentor for Debugging")

# Add middleware for Streamlit frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8001, reload=True)
