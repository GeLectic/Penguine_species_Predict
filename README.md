# Penguin Species Predictor

## Overview
The Penguin Species Predictor is a machine learning project designed to classify penguins into their respective species based on physical attributes such as bill length, bill depth, flipper length, body mass, and island information. This project uses a logistic regression model that achieves an accuracy of **98%**.

## Files in the Repository
- **logistic.pkl**: Pre-trained logistic regression model saved in a pickle file.
- **run_.py**: Python script for making predictions using the trained model.
- **notebook.ipynb**: Jupyter Notebook containing the model training and evaluation process.
- **requirements.txt**: List of Python dependencies required for the project.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/penguin-species-predictor.git
   cd penguin-species-predictor
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Making Predictions

1. Use the provided `run_.py` script to make predictions:
   ```bash
   python run_.py --bill_length <value> --bill_depth <value> --flipper_length <value> --body_mass <value> --island <value>
   ```
   Replace `<value>` with actual measurements of the penguin.

2. The script will output the predicted species (Adelie, Chinstrap, or Gentoo).

### Exploring the Notebook
Open the `notebook.ipynb` file to:
- Understand the data preprocessing steps.
- Explore the training and evaluation process of the logistic regression model.

## Model Details
- **Algorithm**: Logistic Regression
- **Accuracy**: 98%
- **Input Features**: Bill length, bill depth, flipper length, body mass, and island

 
## Link of the deployed Model 
https://penquine0species.streamlit.app/

