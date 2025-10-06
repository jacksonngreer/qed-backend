from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import generativeai as genai
from google.generativeai import types
from dotenv import load_dotenv
import os

load_dotenv()

# API_KEY = os.getenv("GOOGLE_API_KEY") #API key environment var for security
# if not API_KEY:
#     raise ValueError("Missing GOOGLE_API_KEY in environment")


# genai.configure(api_key=API_KEY)


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://jacksonngreer.github.io"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    demo_url = "https://jacksonngreer.github.io/assets/qed-demo.mp4"
#     user_input = request.text

#     # Full prompt with user input inserted
#     prompt = f"""You are a concise, unbiased fact-checking assistant.

# Your task is to:
# - Analyze the following user-submitted text.
# - Identify and fact-check key claims using reputable sources.
# - Note any obvious bias or misleading framing.
# - Keep your response short, clear, and easy to understand.

# Format your response like this:

# Summary:
# [A concise 1-2 sentence summary of what the user is claiming.]

# Verdict:
# [Overall assessment: True, False, Misleading, or Mixed — and why, in 1-2 sentences.]

# Number of True claims formatted as 
# # True

# Number of Misleading claims formatted as 
# # Misleading

# Number of False claims formatted as 
# # False

# Details:
# - "[Claim 1]" 
# ↳ [Verdict] – [1 short sentence explanation]

# - "[Claim 2]" 
# ↳ [Verdict] – [1 short sentence explanation]

# Sources:
# Include a list of sources, NOT links
# Include short, direct links to reputable sources (such as .gov, .org, or major news outlets) that support your analysis.
# Use the format:
# - Source 1, Source 2
# When citing sources:
# - Only give the source name (e.g., "EPA report", "CDC study", "NYT 2021 article").
# - Do NOT invent or guess URLs.

# Analyze this:
# ---
# {user_input}
# ---
# """

#     model = genai.GenerativeModel("models/gemini-2.5-flash")

#     response = model.generate_content(prompt)
#     return { "result": response.text }

    return {
        "result": (
            "QED is temporarily unavailable to prioritize resources for other projects."
            f"<br><br><a href='{demo_url}' target='_blank' style='color:#60a5fa;'>"
            "Watch the demo video here</a>."
        )
    }
