# 📧 SMS Spam Detection using Machine Learning

This project is an end-to-end **Machine Learning** application that classifies SMS or Email messages as **Spam** or **Not Spam (Ham)** using **Natural Language Processing (NLP)** and **Multinomial Naïve Bayes**.

## 📌 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- TF-IDF Feature Extraction
- Multiple Machine Learning Models
- Model Evaluation
- Streamlit Web Application

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

## 🤖 Models Used

- Gaussian Naïve Bayes
- Bernoulli Naïve Bayes
- **Multinomial Naïve Bayes (Selected Model)**
- Support Vector Machine (SVM)
- Random Forest

## 📊 Results

- **Accuracy:** 97.10%
- **Precision:** **100%**
- Selected **Multinomial Naïve Bayes** because it achieved the highest precision, making it well-suited for the imbalanced dataset.

## 🚀 How to Run

1. Clone the repository
```bash
git clone https://github.com/BilalWazir033/Ai-Lab/tree/main/Semester_Project_DS(L)
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app
```bash
streamlit run app.py
```

## 📂 Project Structure

```
SMS-Spam-Detection/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── spam.csv
│── SMS_Spam_Detection.ipynb
│── requirements.txt
└── README.md
```

## 👨‍💻 Author

**Hazrat Bilal**
**Haroon Ur Rashid**
**Khalida Afghan**
**Ilham Raza**  
Introduction to Data Science
BS Computer Science 
University of Engineering & Technology (UET), Peshawar

---
⭐ If you found this project helpful, consider giving it a star!