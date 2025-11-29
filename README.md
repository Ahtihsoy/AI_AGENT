# Product Recommendation AI Agent

## Live Demo Link
https://ahtihsoy-ai-agent-app-8q14s4.streamlit.app/

## Overview
The Product Recommendation AI Agent provides intelligent product suggestions based on user preferences such as category, price, and features.  
It uses a curated JSON product dataset, applies filtering, and generates recommendations using the Groq LLaMA 3.1 model.  
The interface is built with Streamlit for easy interaction.


## Features
- Natural language product search
- AI-powered recommendations using Groq LLaMA 3.1
- Multiple product categories supported
- Filters for category and maximum price
- Recent search history tracking
- Clean and responsive Streamlit user interface

---

## Architecture

User Input (Query + Filters)
        |
        v
Streamlit UI
        |
        v
Filtering Layer (from product_data.json)
        |
        v
Prompt Construction (User Query + Filtered Products)
        |
        v
Groq LLaMA 3.1 Model (API)
        |
        v
AI-Generated Product Recommendations
        |
        v
Streamlit Output (Results + History)

---

## Tech Stack
- Python
- Streamlit
- Groq LLaMA 3.1 API
- JSON dataset
- VS Code / VSCodium

## Project Structure
project/
│── app.py  
│── product_data.json  
│── requirements.txt  
│── README.md  

## How to Run Locally

### 1. Create Virtual Environment
python3 -m venv venv  
source venv/bin/activate

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Add Groq API Key (Important)
Create a file:

.streamlit/secrets.toml

Add:
GROQ_API_KEY = "your_groq_api_key_here"

### 4. Run the Application
streamlit run app.py

## Deployment Instructions (Streamlit Cloud)

1. Upload project to GitHub  
2. Go to https://streamlit.io/cloud  
3. Click "New App"  
4. Choose your repository and select app.py  
5. Add your API key in:
Settings → Secrets → Add:

GROQ_API_KEY = "your_groq_api_key_here"

6. Deploy the application


## Product Dataset
The dataset (product_data.json) contains:
- Product name  
- Category  
- Price  
- Features  

You can add more products easily.

## Limitations
- Uses static dataset (no live prices)  
- No images displayed currently  
- No authentication system  

## Future Enhancements
- Add product images
- Add PostgreSQL database
- Add real-time price scraping
- Add voice search support
- Improve UI with product cards
- Add user personalization

## Optional Video Demo
You may include a short 2–3 minute screen recording showing:
- Entering a query
- Applying filters
- Viewing recommendations
- How the system works



