from django.forms import ModelForm
from .models import WifiCode, LinkCode, SocialCode
class WifiForm(ModelForm):
    class Meta:
        model = WifiCode
        fields = ['wifi_name', 'encryiption', 'password']


class LinkForm(ModelForm):
    class Meta:
        model = LinkCode
        fields = ['link']


class SocialForm(ModelForm):
    class Meta:
        model = SocialCode
        fields = ['username']




