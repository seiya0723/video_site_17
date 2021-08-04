from rest_framework import serializers

from .models import Video,VideoComment,VideoCommentReply,VideoCommentReplyToReply,MyList,History,GoodVideo
from users.models import CustomUser,FollowUser,BlockUser

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Video
        fields =["title","description","category","movie","thumbnail","user",]

class VideoEditSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Video
        fields =[ "title","description","category", ]


class VideoCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model  = VideoComment
        fields = ["content","target","user",]

class VideoCommentEditSerializer(serializers.ModelSerializer):

    class Meta:
        model  = VideoComment
        fields = [ "content","target","user",]

class VideoCommentReplyEditSerializer(serializers.ModelSerializer):

    class Meta:
        model  = VideoCommentReply
        fields = [ "content","target","user",]

#TIPS:フィールド名はVideoCommentSerializerと全く同じだが、外部キーで繋がっているものが全く違うので、リプライのバリデーションにVideoCommentSerializerを流用してはならない
class VideoCommentReplySerializer(serializers.ModelSerializer):

    class Meta:
        model  = VideoCommentReply
        fields = ["content","target","user",]

class VideoCommentReplyToReplySerializer(serializers.ModelSerializer):

    class Meta:
        model  = VideoCommentReplyToReply
        fields = ["content","target","user",]


class MyListSerializer(serializers.ModelSerializer):

    class Meta:
        model   = MyList
        fields  = ["target","user",]

class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model   = History
        fields  = ["target","user",]

class RateSerializer(serializers.Serializer):

    flag    = serializers.BooleanField()

class GoodSerializer(serializers.ModelSerializer):

    class Meta:
        model   = GoodVideo
        fields  = [ "target","user",]


class IconSerializer(serializers.ModelSerializer):

    class Meta:
        model  = CustomUser
        fields = ["usericon",]

class FollowUserSerializer(serializers.ModelSerializer):

    class Meta:
        model  = FollowUser
        fields =[ "from_user","to_user" ]

class BlockUserSerializer(serializers.ModelSerializer):

    class Meta:
        model  = BlockUser
        fields =[ "from_user","to_user" ]


class UserInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model  = CustomUser
        fields =[ "handle_name","self_introduction" ]