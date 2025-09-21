import streamlit as st
import pickle 

with open("expense_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_category(description):
    desc_tfidf = vectorizer.transform([description.lower()])
    category = model.predict(desc_tfidf)[0]
    return category


# ui 
st.title("💸 Smart Expense Categorizer")

desc = st.text_input("Enter your expense description:")

if st.button("Predict Category"):
    if desc.strip() != "":
        category = predict_category(desc)
        st.success(f"Predicted Category: {category}")
    else:
        st.warning("Please enter a description first.")