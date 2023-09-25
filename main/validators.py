from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.utils.translation import gettext_lazy as _

class CustomCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user=None):
        super().validate(password, user)
        if password.lower() in self.passwords:
            raise ValidationError(
                _("La contraseña es demasiado común."),
                code='password_too_common',
            )
    def get_help_text(self):
        return _(
            "La contraseña es demasiado común. Por favor, elija una contraseña más segura."
        )

def val_cedulamed(cedulamed):
    if len(str(cedulamed)) < 4:
        raise ValidationError("El número de identificación debe ser mayor a 4 digitos") 
    if len(str(cedulamed)) > 10:
        raise ValidationError("El número de identificación no puede exceder los 10 dígitos") 
    
def val_cedulaext(cedulaext):
    if len(str(cedulaext)) < 4:
        raise ValidationError("El número de identificación debe ser mayor a 4 digitos") 
    if len(str(cedulaext)) > 10:
        raise ValidationError("El número de identificación no puede exceder los 10 dígitos") 

def val_cedulapac(cedulapac):
    if len(str(cedulapac)) < 4:
        raise ValidationError("El número de identificación debe ser mayor a 4 digitos") 
    if len(str(cedulapac)) > 10:
        raise ValidationError("El número de identificación no puede exceder los 10 dígitos") 

def validate_unique_user_identification(value):
    from main.models import Personalsalud, Usuarioexterno
    
    if Personalsalud.objects.filter(cedulamed=value).exists() or Usuarioexterno.objects.filter(cedulaext=value).exists():
        raise ValidationError('El usuario con este número de identificación ya posee una cuenta en el sistema.')
    
def validate_unique_phone(value):
    from main.models import Personalsalud, Usuarioexterno
    
    if Personalsalud.objects.filter(telefonomed=value).exists() or Usuarioexterno.objects.filter(telefonoext=value).exists():
        raise ValidationError('Un usuario con este número de celular ya posee una cuenta en el sistema.')