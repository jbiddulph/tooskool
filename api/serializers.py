from rest_framework import serializers
from schools.models import School, Review
from users.models import Profile, Child, Message

class SchoolSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = School
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

class ProfileSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = '__all__'

    def get_children(self, obj):
        children = obj.children.all()
        serializer = ChildSerializer(children, many=True)
        return serializer.data

    def get_messages(self, obj):
        messages = obj.message_set.all()
        serializer = MessageSerializer(messages, many=True)
        return serializer.data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'