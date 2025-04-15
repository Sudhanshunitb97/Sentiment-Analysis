🧠 TestiScore AI: NLP Engine for Review Rating & Revenue Impact

Convert unstructured student reviews into meaningful rating scores (0–10) to support marketing, satisfaction tracking, and real-world business decisions.

📌 Project Objective

To build a scalable NLP system that transforms free-text coaching reviews into continuous numerical ratings, enabling automated testimonial extraction and measurable marketing impact.

🔧 Tools & Libraries

Python

Pandas, NumPy

NLTK, Gensim

Scikit-learn

Streamlit

SymSpell

🗂️ Dataset Overview

Combined 3 CSV files (200,000+ reviews)

Included positive, mixed, and real-world coaching feedback

Each review was paired with a simulated rating (0–10)

🔁 Project Workflow

1. Data Preparation

Loaded & merged datasets using pandas

Expanded contractions using contractions.fix()

Removed emojis with regex

Applied spell correction using SymSpell + frequency dictionary

Cleaned text: removed punctuation, converted to lowercase

2. Text Processing

Tokenized reviews using NLTK

Removed stopwords

Applied lemmatization (WordNet Lemmatizer)

Joined words into cleaned sentences

3. Feature Engineering

TF-IDF Vectorization for term importance

Word2Vec Embeddings to capture semantic meaning

4. Model Training

Model 1: TF-IDF + Linear Regression (MSE = 4.46)

Model 2: Word2Vec + Linear Regression (MSE = 5.54)

Selected the TF-IDF model for deployment

5. Evaluation

MSE: 4.46 → RMSE ≈ 2.11

Accuracy within ±1 point: 42.6% of predictions

6. Deployment

Deployed real-time prediction tool via Streamlit

Input a review → Receive predicted rating instantly

💰 Business Impact Simulation

Testimonial-based campaigns estimated to add 3,400 new admissions

Revenue per admission: ₹20,000

Projected gain: ₹6.80 Cr

Adjusted for model accuracy (42.6% reliability):
→ Realistic revenue uplift = ₹2.90 Cr

✅ Results Summary

200K+ reviews processed

Ratings predicted with continuous output

Fully deployed Streamlit app

Quantified and adjusted business impact

🙋‍♂️ My Role & Learnings

Full ownership from data wrangling to deployment

Integrated NLP + regression with business use case

Learned importance of modeling reliability & ROI estimation

🚀 Demo

Add Streamlit app link here if deployed

