from rest_framework import serializers
from webapp.models import Account

class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['email','username','password','password2','first_name','last_name']
