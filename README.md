# Lagos House Price Prediction Model 🏠

A machine learning model that predicts house prices in Lagos, Nigeria using property features and location data.

## 🎯 Project Overview

This project uses machine learning to predict house prices in Lagos State, Nigeria. The model is trained on real estate data from various locations across Lagos and achieves strong performance with an R² score of 0.48+.

## 📊 Model Performance

- **Best Model**: Random Forest Regressor
- **R² Score**: 0.48+ (48% variance explained)
- **RMSE**: ₦59M (Root Mean Square Error)
- **MAE**: ₦41M (Mean Absolute Error)
- **Cross-Validation**: 5-fold validation

## 🏗️ Project Structure

```
├── code.ipynb                 # Main Jupyter notebook with complete analysis
├── app.py                     # Standalone Gradio app
├── lagos_properties.csv       # Processed Lagos property data
├── huggingface_deployment/    # Deployment files for Hugging Face Spaces
│   ├── app.py                 # Production Gradio app
│   ├── best_model.pkl         # Trained model file
│   ├── feature_info.json      # Model metadata
│   ├── requirements.txt       # Python dependencies
│   ├── README.md             # Deployment documentation
│   └── sample_data.csv       # Sample training data
├── extracted1/               # Dataset 1 (Nigeria houses data)
├── extracted2/               # Dataset 2 (Nigeria houses data new)
├── extracted3/               # Dataset 3 (Nigerian properties cleaned)
├── archive.zip               # Original dataset 1
├── archive (1).zip           # Original dataset 2
└── archive3.zip              # Original dataset 3
```

## 🚀 Features

### Input Features
- **Property Details**: Bedrooms, bathrooms, toilets, parking spaces
- **Property Types**: 
  - Detached Bungalow
  - Detached Duplex
  - Semi Detached Bungalow
  - Semi Detached Duplex
  - Terraced Bungalow
  - Terraced Duplexes

### Location Coverage
The model covers 24 different areas in Lagos:
- Ajah, Alimosho, Amuwo Odofin, Gbagada
- Ibeju Lekki, Ifako-Ijaiye, Ikeja, Ikorodu
- Ikotun, Ikoyi, Ilupeju, Ipaja
- Isheri North, Isolo, Lekki, Magodo
- Maryland, Ogudu, Ojo, Ojodu
- Surulere, Victoria Island (VI), Yaba
- Others (for less common locations)

## 🛠️ Installation & Setup

### Prerequisites
```bash
pip install -r huggingface_deployment/requirements.txt
```

### Required Libraries
- pandas >= 1.5.0
- numpy >= 1.21.0
- scikit-learn >= 1.0.0
- xgboost >= 1.6.0
- gradio >= 4.0.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0

### Running the Notebook
```bash
jupyter notebook code.ipynb
```

### Running the Gradio App
```bash
python app.py
```

## 🎮 Usage

### Web Interface (Gradio)
1. Run the Gradio app: `python app.py`
2. Open the provided URL in your browser
3. Input property details:
   - Number of bedrooms, bathrooms, toilets
   - Parking spaces
   - Property type (select one)
   - Location in Lagos (select one)
4. Click "Predict House Price"
5. Get estimated price in Nigerian Naira

### Programmatic Usage
```python
import pickle
import pandas as pd

# Load the trained model
with open('huggingface_deployment/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Prepare input data
input_data = pd.DataFrame({
    'bedrooms': [3],
    'bathrooms': [2],
    'toilets': [3],
    'parking_space': [2],
    'title_Detached Bungalow': [0],
    'title_Detached Duplex': [0],
    # ... other features
})

# Make prediction
prediction = model.predict(input_data)
print(f"Predicted price: ₦{prediction[0]:,.2f}")
```

## 📈 Model Development Process

1. **Data Collection**: Multiple datasets from Nigerian real estate market
2. **Data Cleaning**: Removed duplicates, handled outliers, cleaned inconsistencies
3. **Feature Engineering**: One-hot encoding for categorical variables
4. **Model Training**: Compared Linear Regression, Random Forest, and XGBoost
5. **Model Evaluation**: Cross-validation and comprehensive metrics
6. **Deployment**: Gradio web interface for public use

## 🚀 Deployment

### Hugging Face Spaces
The model is ready for deployment on Hugging Face Spaces:
1. Go to [https://huggingface.co/spaces](https://huggingface.co/spaces)
2. Create a new Space (choose "Gradio" SDK)
3. Upload files from `huggingface_deployment/` folder
4. Your app will auto-deploy!

### Local Deployment
```bash
cd huggingface_deployment
python app.py
```

## 📊 Data Sources

- **Dataset 1**: Nigeria houses data (6,000+ properties)
- **Dataset 2**: Nigeria houses data new (additional properties)
- **Dataset 3**: Nigerian properties cleaned (preprocessed data)
- **Focus**: Lagos State properties only

## 🔍 Key Insights

- **Location Impact**: Victoria Island and Ikoyi command premium prices
- **Property Type**: Detached properties generally more expensive
- **Size Correlation**: Strong correlation between property size and price
- **Market Trends**: Prices vary significantly across Lagos locations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This model provides price estimates based on historical data and should not be used as the sole basis for financial decisions. Always consult with real estate professionals for accurate property valuations.

## 📧 Contact

For questions or feedback about this project, please open an issue in the GitHub repository.

---

**🎯 Built with ❤️ for the Lagos real estate market**
