from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0)
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Male'), (1, 'Female')])
    cp = forms.ChoiceField(label='Chest Pain Type', choices=[(0, 'Typical Angina'), (1, 'Atypical Angina'), (2, 'Non-Anginal Pain'), (3, 'Asymptomatic')])
    trestbps = forms.IntegerField(label='Resting Blood Pressure', min_value=0)
    chol = forms.IntegerField(label='Serum Cholestoral', min_value=0)
    fbs = forms.ChoiceField(label='Fasting Blood Sugar', choices=[(0, 'Less than 120 mg/dl'), (1, 'Greater than 120 mg/dl')])
    restecg = forms.ChoiceField(label='Resting Electrocardiographic Results', choices=[(0, 'Normal'), (1, 'Having ST-T wave abnormality'), (2, 'Probable or definite left ventricular hypertrophy')])
    thalachh = forms.IntegerField(label='Maximum Heart Rate Achieved', min_value=0)
    exang = forms.ChoiceField(label='Exercise Induced Angina', choices=[(0, 'No'), (1, 'Yes')])
    oldpeak = forms.FloatField(label='ST Depression Induced by Exercise', min_value=0)
    slope = forms.ChoiceField(label='Slope of the Peak Exercise ST Segment', choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')])
    ca = forms.ChoiceField(label='Number of Major Vessels Colored by Fluoroscopy', choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three')])
    thal = forms.ChoiceField(label='Thalassemia', choices=[(0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect')])