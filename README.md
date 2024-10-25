# 📉💡 Customer Churn Prediction using 🤖 Machine Learning

This 📂 repository contains a project focused on predicting customer churn 🔄 for a 📞 telecommunications company. The 📊 dataset contains customer info ℹ️, service details, and the outcome of whether the customer has churned. This project utilizes 🤖 machine learning techniques for data 🕵️ exploration, modeling, and feature importance analysis.

## 📁 Contents

- **LICENSE**: 📜 License file specifying the terms under which this project can be used.
- **ML\_Engineer\_Churn\_Prediction\_Final.ipynb**: The main 📝 Jupyter Notebook containing the entire analysis, from data loading 📥 to model evaluation 📊.
- **README.md**: This file 📄, providing an overview of the project and instructions for setup and usage.
- **Telco\_customer\_churn.xlsx**: The 📊 dataset used in this project, containing customer information.
- **lgbm\_churn\_model.pkl**: The saved 💾 LightGBM model used for predicting churn, allowing for easy reuse or deployment.

## 🌟 Project Overview

Customer churn 🔄 is a critical metric 📊 for subscription-based companies, and predicting it helps prevent customer losses by taking proactive actions 🚀. This project aims to leverage 🤖 machine learning to predict churn using a variety of features, including customer demographics 👥, service usage 📶, and payment behavior 💳.

The project follows these major steps:

1. **Data Loading and Initial Exploration**: Load the dataset 📥 and understand its structure, size 📏, and any missing values ❓.
2. **Data Cleaning**: Remove unnecessary columns 🗑️, handle missing values, and prepare the dataset for analysis 🧼.
3. **Feature Engineering**: Transform categorical variables 🔄 into numerical ones 🔢, and engineer features to enhance the predictive power of the model ⚡.
4. **Exploratory Data Analysis (EDA)**: Visualize 🔍 key relationships in the data to gain insights 💡 into customer behavior and identify patterns 🔄 related to churn.
5. **Model Training and Evaluation**: Train several machine learning models 🤖 to predict churn, including Random Forests 🌲 and XGBoost 🚀. Evaluate model performance using metrics such as accuracy ✔️, precision 🎯, recall 🔁, and F1-score 📊.
6. **Feature Importance Analysis**: Analyze which features are the most impactful 💥 in predicting churn, providing business insights for targeted interventions 🎯.
7. **Saving and Deploying the Model**: Save 💾 the best-performing model for future use and deployment 🌐.

## 📊 Dataset

The dataset used in this project is the Telco customer churn dataset, containing 7,043 entries 📈 with 33 features, including:

- **Customer demographics** (e.g., gender 👨‍👩‍, senior citizen status 👵👴)
- **Service usage** (e.g., internet service type 🌐, tenure ⏳)
- **Payment information** (e.g., payment method 💳, monthly charges 💵)

The target variable is `Churn Value`, indicating whether a customer has churned (1) or not (0).

## ⚙️ How to Use

### 📋 Prerequisites

To run this notebook, you need the following libraries 📚:

- `numpy` 📐
- `pandas` 🐼
- `seaborn` 📊
- `matplotlib` 📉
- `scikit-learn` 🤖
- `xgboost` 🚀
- `joblib` 💾

To install all dependencies, run:

```sh
pip install numpy pandas seaborn matplotlib scikit-learn xgboost joblib
```

### ▶️ Running the Project

1. **Clone the Repository**:

   ```sh
   git clone <repository_url>
   ```

   Replace `<repository_url>` with the actual URL 🔗 of this GitHub repository.

2. **Navigate to the Project Directory**:

   ```sh
   cd churn-prediction
   ```

3. **Open the Jupyter Notebook**:

   ```sh
   jupyter notebook ML_Engineer_Churn_Prediction_Final.ipynb
   ```

   Run all cells in the notebook to see the full analysis and model training 🤖.

## 📊 Results

- **Model Performance**: The final model achieved an accuracy of approximately 85% ✔️, with an F1-score of 0.85 for the churn class. The model effectively identifies customers who are likely to churn, allowing for targeted retention efforts 🔄.
- **Key Features**: The most important features influencing churn prediction include `Monthly Charges` 💵, `Contract Type` 📝, and `Tenure` ⏳. Customers with month-to-month contracts and higher charges are more likely to churn, while those with longer tenures are less likely to do so.

## 📈 Conclusion

This project demonstrates how 🤖 machine learning can be leveraged to predict customer churn 🔄, providing valuable insights 💡 for reducing customer attrition in a 📞 telecommunications company. The analysis highlights actionable factors, such as contract type 📝 and monthly charges 💵, that contribute significantly to customer churn.

## 📜 License

This project is licensed under the MIT License 📄 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

The dataset used in this project was provided by IBM as part of the Telco Customer Churn dataset 📊.

Feel free to fork 🍴 this repository, make your modifications ✏️, and contribute to improving this project 🚀!
