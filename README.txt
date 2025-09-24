# Text Sentiment Prediction

This project contains two main components:

1. **Model Training (`model.ipynb`)**  
   - Loads and preprocesses a dataset (`Sentiment.csv`).  
   - Trains a **TF-IDF + Logistic Regression** pipeline for sentiment classification.  
   - Exports the trained model with `joblib`.

2. **Streamlit App (`app.ipynb`)**  
   - Loads the trained model.  
   - Provides a simple **web interface** where users can input text.  
   - Displays sentiment prediction and confidence score.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create Virtual Environment
It’s recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
Install required Python libraries:
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can install manually:
```bash
pip install streamlit scikit-learn pandas numpy matplotlib seaborn nltk joblib
```

### 4. Download NLTK Resources
The model notebook uses VADER from `nltk`:
```python
import nltk
nltk.download('vader_lexicon')
```

### 5. Train the Model
Open and run **`model.ipynb`** to:
- Load dataset (`Sentiment.csv`)
- Train the classifier
- Save the model (e.g., `baseline_logreg_tfidf.joblib`)

```bash
jupyter notebook model.ipynb
```

The trained model will be stored (update the path in `app.ipynb` if necessary).

### 6. Run the Streamlit App
Launch the web app:
```bash
streamlit run app.ipynb
```

Streamlit usually runs from `.py` files, not `.ipynb`.  
To convert, run:
```bash
jupyter nbconvert --to script app.ipynb
mv app.py app.py
streamlit run app.py
```

---

## Project Structure
```
.
├── app.ipynb               # Streamlit app
├── model.ipynb             # Model training notebook
├── Sentiment.csv           # Dataset (required for training)
├── baseline_logreg_tfidf.joblib  # Saved trained model (after training)
├── requirements.txt        # Python dependencies (recommended)
└── README.md               # Project documentation
```

---

## Usage
1. Open the Streamlit app in your browser.  
2. Enter any text in the input box.  
3. Click **Predict** to see sentiment (Positive/Negative/etc.) and confidence score.
