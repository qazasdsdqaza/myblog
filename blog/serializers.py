from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings


# class LoginSerializer(serializers.ModelSerializer):
#     pwd2 = serializers.CharField(max_length=20, label='确认密码')
#
#     class Meta:
#         model = ''
#         fields = '__all__'
#         extra_kwargs = {
#             'username': {
#                 'min_length': 5,
#                 'max_length': 20,
#                 'error_messages': {
#                     'min_length': '仅允许5-20个字符的用户名',
#                     'max_length': '仅允许5-20个字符的用户名',
#                 }
#             },
#             'password': {
#                 'write_only': True,
#                 'min_length': 8,
#                 'max_length': 20,
#                 'error_messages': {
#                     'min_length': '仅允许8-20个字符的密码',
#                     'max_length': '仅允许8-20个字符的密码',
#                 }
#             },
#             'token': {
#                 'read_only': True,
#                 'label': 'JWT_Token',
#             }
#         }
#
#     def validate(self, attrs):
#         username = attrs['username']
#         pwd = attrs['password']
#         pwd2 = attrs['pwd2']
#         if username and pwd and pwd2:
#             if pwd != pwd2:
#                 raise serializers.ValidationError('两次输入的密码不一样')
#         else:
#             raise serializers.ValidationError('请填写完整所有内容')
#         return attrs
#
#     def create(self, validated_data):
#         del validated_data['pwd2']
#         user = super().create(validated_data)
#         # user.set_password(validated_data['password'])
#         user.save()
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#         payload = jwt_payload_handler(user)
#         token = jwt_encode_handler(payload)
#         return user
#
#     def update(self, instance, validated_data):
#         return 'this is create -->%s' % validated_data


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
