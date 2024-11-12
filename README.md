# COS 397 IW 02 - Machine Learning and Data Science 
Github Repo for an Independent Work Seminar at Princeton

## Predicting Pokémon Type and Generation Using Machine Learning Techniques - Work in Progress
This project focuses on predicting Pokemon types and generations using various machine learning models. So far I have implemented and compared several algorithms to classify Pokemon based on their stats and characteristics.
### Project Overview
Data: I am using a dataset of Pokemon with features like HP, Attack, Defense, Special Attack, Special Defense, Speed, Height, and Weight. The dataset is scraped from https://pokemondb.net/pokedex/all. 

#### Prediction Tasks:
- Primary Type Prediction
- Both Types Prediction (Multi-label classification)
- Generation Prediction

### Models Implemented
I have experimented with several machine learning models so far:
1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Random Forests
4. Support Vector Machines (SVM) - both linear and RBF kernels
5. Gradient Boosting (XGBoost)

### Methodology
For each model, the general implementation steps are as follows:
1. Data preprocessing and splitting
2. Initial model training without cross-validation
3. Cross-validation and hyperparameter tuning
4. Performance evaluation using metrics like accuracy, Hamming loss, and classification reports
5. Feature importance analysis

### Work in progress for CNN
The approach is to develop an advanced multi-modal, multi-output classification model for predicting both Pokémon type and generation. This novel approach integrates convolutional neural networks (CNNs) for image processing with dense layers for analyzing tabular data, specifically the Pokémon's basic statistics. The model's architecture is designed to produce two distinct outputs: one for Pokémon type classification and another for generation prediction.

