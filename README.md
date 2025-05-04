# heart_disease_prediction

# Heart Disease Prediction

## Overview
This project focuses on building and evaluating machine learning models to predict the risk of heart disease. The primary goal was to develop a reliable predictive model that achieves an F1 score of at least 85%, ensuring both high precision and recall for heart disease classification.

## Models Developed and Compared

Four different models were developed and evaluated:
1. **Decision Tree Classifier**
2. **K-Nearest Neighbors (KNN) Classifier**
3. **Neural Network Model 1**
4. **Neural Network Model 2**

### Model Performance Summary

| Model                  | F1 Score | Accuracy |
|------------------------|----------|----------|
| Decision Tree          | **95%**  | **95%**  |
| KNN                    | 87%      | 86%      |
| Neural Network Model 2 | 70%      | 68%      |
| Neural Network Model 1 | 68%      | 52%      |

- The **Decision Tree Classifier** significantly outperformed the other models in both F1 score and accuracy.
- The **KNN Classifier** also met the minimum target F1 score.
- Both **Neural Network Models** underperformed, suggesting further tuning or architectural adjustments may be necessary.

## Model Recommendation

The **Decision Tree Classifier** is the recommended model due to its outstanding performance:
- Highest F1 score (95%)
- Best overall accuracy (95%)
- Strong ability to minimize false positives and negatives

## Conclusion

The project successfully achieved its objective of developing a reliable heart disease prediction model. The Decision Tree Classifier demonstrated excellent predictive performance, making it suitable for real-world implementation, particularly for early detection and risk stratification in clinical settings.

## Recommendations for Future Work

- **Improve Data Quality and Diversity**: Include more representative samples of different heart disease cases.
- **Enhance Neural Networks**: Perform hyperparameter tuning and explore alternative architectures.
- **Feature Engineering**: Investigate the addition of domain-specific features to improve model robustness.
- **Model Specialization**: Extend the study to identify specific types of heart diseases, enabling more targeted interventions.
- **Deployment**: Package the best-performing model into a deployable web or mobile app for real-time risk assessments.

---
