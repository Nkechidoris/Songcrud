from rest_framework import serializers
from .models import Lyric, Song

class SongSerializer(serializers.ModelSerializer):
    # to get lyric content in the song
    lyric = serializers.SerializerMethodField('get_lyric')
    artist_id = serializers.StringRelatedField(read_only=True)

    def get_lyric(self, instance):
        query = instance.lyric_set.all()
        lyric = LyricSerializer(query, many=True).data
        return lyric

    class Meta:
        model = Song
        fields = ['id', 'artist_id', 'title', 'date_released', 'likes', 'lyric']

class UpdateSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['title', 'date_released', 'artist_id']

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content']

