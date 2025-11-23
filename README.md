💸 Smart Expense Categorizer – Machine Learning Web App

This project is a Streamlit-based machine learning web application that automatically categorizes user-entered expense descriptions into appropriate categories (e.g., Food, Travel, Shopping, Bills, etc.).

It uses a text classification model trained on TF-IDF features to understand and classify expenses.

📌 Features

* Simple and interactive Streamlit UI
* Classifies expenses based on short text descriptions(e.g., "Bought groceries" → Food)
* Uses a vectorizer (TF-IDF) to convert text into numerical features
* Predicts category using a pre-trained ML model
* Instant prediction with clean UI

🛠️ Technologies Used
| Component            | Technology        |
|---------------------|-------------------|
| Programming Language | Python            |
| Web App Framework    | Streamlit         |
| Model Storage        | Pickle            |
| Text Vectorization   | TF-IDF (Scikit-learn) |
| Classification Model | expense_model.pkl |
