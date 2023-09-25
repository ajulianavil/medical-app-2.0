from django import forms
from users.models import Appuser
from main.models import *
from django.contrib.auth.hashers import make_password


class UploadFileForm(forms.Form):
    file = forms.FileField()


class CreateUserForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico",max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}) )
    password = forms.CharField(label="Contraseña",required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'}) )
    repassword = forms.CharField(label="Repetir contraseña", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Repetir contraseña'}) )
    is_superuser = forms.BooleanField(label="Hacer administrador", required=False)
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('repassword')

        if password1 and password2 and password1 != password2:
            self.add_error("repassword","Las contraseñas no coinciden")
            raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password'])
        user.is_superuser = self.cleaned_data['is_superuser']
        
        if commit:
            user.save()
        return user

    class Meta:
        model = Appuser
        fields = ['email', 'password', 'roles', 'is_superuser']

class RepositorioFilterForm(forms.ModelForm):
    ESTADOS = (
        ('1', 'Sano'),
        ('2', 'No sano'),
        # Add more choices as needed
    )
    
    DIAGNOSTICOS = (
        ('1', 'Macrocrania'),
        ('2', 'Microcefalia'),
        # Add more choices as needed
    )
    ga = forms.CharField(label="Edad gestacional (semanas)", max_length=4, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}) )
    state = forms.ChoiceField(choices=ESTADOS, label='Condición del feto', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}))
    medicion = forms.ModelChoiceField(queryset=Tipomedicion.objects.all(), label="Medición", required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    diagnosis = forms.ChoiceField(choices=DIAGNOSTICOS, label='Condición del feto', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}))
    fecha_inicial = forms.DateField(label='Fecha inicial', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': ' '}))
    fecha_final = forms.DateField(label='Fecha final', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': ' '}))
    
    def filter_results(self):
        # Retrieve the form data
        ga_data = self.cleaned_data['ga']
        state_data = self.cleaned_data['state']
        medicion_data = self.cleaned_data['medicion']
        diagnosis_data = self.cleaned_data['diagnosis']
        fecha_inicial_data = self.cleaned_data['fecha_inicial']
        fecha_final_data = self.cleaned_data['fecha_final']
        

        # Perform the query based on the form data
        # queryset1 = Table1.objects.filter(field1=field1_data)
        # queryset2 = Table2.objects.filter(field2=field2_data)

        # Return the filtered results
        return 'Hola'
    class Meta:
        model = Personalsalud
        fields = ['nombresmed', 'apellidosmed', 'cedulamed', 'telefonomed', 'direccionmed', 'hospitalid']
        
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['image_data']