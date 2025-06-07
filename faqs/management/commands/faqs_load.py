import json
from django.core.management.base import BaseCommand
from faqs.models import FAQ


class Command(BaseCommand):
    help = 'Load FAQs from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, help='The file path to the JSON file.'
        )

    def handle(self, *args, **kwargs):
        # Defines the path to the JSON file
        # Specific JSON filepath should be used
        # when running the management command
        file_path = kwargs['file_path']

        # Opens and reads the JSON with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                FAQ.objects.create(
                    question=item['question'],
                    answer=item['answer'],
                    category=item['category'],
                )

        self.stdout.write(self.style.SUCCESS('Loaded successfully'))
