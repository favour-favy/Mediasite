from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from gallery.models import Category
import os

class Command(BaseCommand):
    help = 'Creates a superuser and default categories if they do not exist'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password=os.environ.get('ADMIN_PASSWORD', 'changeme123')
            )
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write('Superuser already exists')

        default_categories = ['personal', 'receipts', 'work']
        for name in default_categories:
            Category.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Categories created'))