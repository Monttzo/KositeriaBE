from rest_framework import serializers
from kositeriaApp.models.user import user

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'nameUser', 'lastNameUser', 'username',
         'password', 'emailUser', 'dateBirthUser', 'appMode']
        
    def create(self, validated_data):
        userInstance = user.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        User = user.objects.get(id=obj.id)
        return {
            'id': User.id,
            'nameUser': User.nameUser,
            'lastNameUser': User.lastNameUser,
            'username': User.username,
            'password': User.password,
            'emailUser': User.emailUser,
            'dateBirthUser': User.dateBirthUser,
            'appMode': User.appMode
        }