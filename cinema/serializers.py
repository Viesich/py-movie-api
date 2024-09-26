from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(read_only=False, max_length=1000)
    duration = serializers.CharField(read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> None:
        instance.title = validated_data.get("title", instance.title)
        instance.description = (
            validated_data.get("description", instance.description)
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()

    class Meta:
        model = Movie
        fields = ("id", "description", "duration")
