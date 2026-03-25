# Sentiment Analysis of E-commerce Reviews using NLP

Automatically classifies customer reviews into **Positive, Neutral, or Negative** using Natural Language Processing techniques.

## Features

* Predicts sentiment from user input text
* Classifies into **Positive / Neutral / Negative**
* Displays **probability distribution**
* Visualizes results using graphs
* Clean and interactive **Streamlit UI**

## Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib

## Live Demo

👉 https://sentiment-analysis-of-e-commerce-using.onrender.com

## Screenshot

![Sentiment Analysis App](./app_preview.png)

## Sample Output

* Review: *“This product is amazing and works perfectly!”* → **Positive**
* Review: *“It’s okay, not great but not bad.”* → **Neutral**
* Review: *“Worst experience, very disappointed.”* → **Negative**

## How It Works

* Takes user input (review text)
* Applies text preprocessing (cleaning, tokenization)
* Converts text into vectors using **TF-IDF**
* Uses a machine learning model to predict sentiment
* Displays prediction along with probability distribution

## Project Structure

* `app.py` → main Streamlit application
* `requirements.txt` → dependencies
* `README.md` → documentation

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

* Use advanced models like **BERT / Transformers**
* Improve accuracy with larger datasets
* Add real-time data scraping
* Enhance UI/UX design
