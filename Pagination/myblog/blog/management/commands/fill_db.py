from django.core.management.base import BaseCommand
from myblog.blog.models import Post
from faker import Faker

class Command(BaseCommand):
    help = 'Fills the database with test posts'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):  # количество постов
            Post.objects.create(
                title=fake.sentence(),
                content=fake.paragraph(),
            )
        self.stdout.write(self.style.SUCCESS('Successfully filled the database with 100 posts'))
