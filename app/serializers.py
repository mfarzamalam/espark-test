from .models import Team, Player
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TeamSerializer(serializers.ModelSerializer):
   class Meta:
       model = Team
       fields = ('name', )


class PLayerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Player
       fields = ('i_team', 'i_user')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        print("validated_data:", validated_data)
        username = validated_data['email']
        user_obj = User.objects.create(
            username=username,
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        print("user_obj:", user_obj)
        user_obj.set_password(validated_data['password'])
        user_obj.save()
        return user_obj
