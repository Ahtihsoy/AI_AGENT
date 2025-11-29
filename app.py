import json
import streamlit as st
from groq import Groq

# -------------------- FIXED UI THEME --------------------
st.markdown("""
<style>

.stApp {
    background-color: #EAF4FF;   /* Light Blue Background */
}

/* AI Result Text */
div[data-testid="stMarkdownContainer"], div.stMarkdown, p, span {
    color: #003366 !important;
    font-size: 20px !important;
    line-height: 1.5;
}

/* Heading */
h1 {
    color: #002147 !important;
    font-weight: 900;
}

/* Text box styling */
.stTextInput > div > div > input {
    background-color: white !important;   /* White background */
    color: #002147 !important;            /* Dark blue text */
    border: 2px solid #4A90E2 !important; /* Light blue border */
    padding: 10px;
    border-radius: 8px;
}


/* SIDEBAR BACKGROUND – LIGHT GREY (VISIBLE) */
section[data-testid="stSidebar"] {
    background-color: #D3D3D3 !important;  /* Light grey */
}

/* SIDEBAR TEXT COLOR – DARK BLUE (VISIBLE) */
section[data-testid="stSidebar"] * {
    color: #002147 !important;
    font-size: 16px !important;
}

/* Buttons */
.stButton button {
    background-color: #4A90E2;
    color: white !important;
    border-radius: 8px;
    padding: 8px 16px;
    border: none;
    font-size: 16px;
}
.stButton button:hover {
    background-color: #357ABD;
}

</style>
""", unsafe_allow_html=True)



# ---------------------------------------------------------------

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def load_products():
    try:
        with open("product_data.json", "r") as f:
            return json.load(f)
    except:
        return []

products = load_products()

st.sidebar.title("🔍 Filters")

categories = [
    "All", "Mobile", "Audio", "TV", "Laptop",
    "Wearable", "Home Appliance", "Camera",
    "Gaming", "Accessories", "Tablet"
]

selected_category = st.sidebar.selectbox("Choose Category:", categories)
max_price = st.sidebar.slider("Maximum Price (INR):", 500, 150000, 60000)

filtered_products = [
    p for p in products
    if (selected_category == "All" or p["category"] == selected_category)
    and p["price"] <= max_price
]

catalog_json = json.dumps(filtered_products, indent=2)

st.markdown("<h1 style='text-align:center;'>🤖 AI Product Recommendation Engine</h1>", unsafe_allow_html=True)
st.write("Tell me what kind of product you want, and I’ll recommend the best options!")

user_query = st.text_input("What product are you looking for? (e.g., 'Laptop for coding under 40k', 'Good camera phone')")

if user_query:
    prompt = f"""
    Select the best 2 product recommendations from the catalog based on user needs.

    Product Catalog:
    {catalog_json}

    User Query:
    {user_query}

    Format:
    • Product Name
    • Why it matches
    • Price
    • Features (bullet points)
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("🛒 Recommended Products")
        st.write(response.choices[0].message.content)

        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(user_query)

    except Exception as e:
        st.error("Error generating response.")
        st.write(e)

if "history" in st.session_state:
    st.sidebar.subheader("📝 Recent Searches:")
    for query in st.session_state.history[-5:]:
        st.sidebar.write("• " + query)
