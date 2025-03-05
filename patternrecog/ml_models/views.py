import os
import joblib
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from django.views import View
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

from .forms import HeartDiseaseForm

model_path = os.path.join(settings.BASE_DIR, 'models', 'DecisionTree_Model.joblib')

model = joblib.load(model_path)

class PredictModelView(View):
    form_class = HeartDiseaseForm
    template_name = 'model_prediction.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            
            feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                         'restecg', 'thalachh', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
            features_df = pd.DataFrame([form_data.values()], columns=feature_names)

            try:
                prediction = model.predict(features_df)[0]
                return render(request, self.template_name, {'form': form, 'prediction': prediction})
            except Exception as e:
                return render(request, self.template_name, {'form': form, 'error': f"Prediction error: {e}"})
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Invalid data'})