from rest_framework import serializers

from book.models import Book



class BookSerializer(serializers.ModelSerializer):

    # def validate_connectivity(self, data):
    #     if data['pleasantness'] is True and data['connectivity'] is not None:
    #         raise serializers.ValidationError(
    #             "В связанные привычки могут попадать только "
    #             "привычки с признаком приятной привычки"
    #         )
    #     else:
    #         return data
    #
    # def validate_pleasantness(self, data):
    #     if (data['pleasantness'] is True and
    #             data['connectivity'] is not None and
    #             data['award']):
    #         raise serializers.ValidationError(
    #             "У приятной привычки не может "
    #             "быть вознаграждения или связанной привычки."
    #         )
    #     else:
    #         return data
    #
    # def validate_award(self, data):
    #     if data['connectivity'] is not None and data['award']:
    #         raise serializers.ValidationError(
    #             "Нельзя одновременно выбрать "
    #             "связанные привычки и указать вознаграждение."
    #         )
    #     else:
    #         return data

    class Meta:
        model = Book
        fields = "__all__"


