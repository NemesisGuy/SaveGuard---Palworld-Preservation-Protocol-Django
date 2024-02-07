# saveguard_app/forms.py

from django import forms

class BackupSettingsForm(forms.Form):
    FREQUENCY_CHOICES = [
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),  # Add daily frequency option
        ('weekly', 'Weekly'),  # Add weekly frequency option
    ]
    
    frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES)
    save_data_path = forms.CharField(max_length=1000, label='Save Data Path')
    backup_path = forms.CharField(max_length=1000, label='Backup Path')
    # Add more fields as needed for other backup settings
