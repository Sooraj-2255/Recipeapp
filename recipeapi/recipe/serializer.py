from rest_framework import serializers
from recipe.models import Recipe,RatingAndReview
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['name','ingredients','cuisine','meal_type','created_on','edited_at']


class ReviewSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]
    class Meta:
        model = RatingAndReview
        fields = ['name', 'user', 'rating', 'review', 'comment', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):  # after validation      (password Encrypted)
        u = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        u.save()

