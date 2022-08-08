from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from model_bakery.recipe import Recipe, foreign_key
import faker

from blog.models import Category, Article
fake = faker.Faker()

class Command(BaseCommand):
    help = 'Populates the database with some testing data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Started database population...'))

        if User.objects.filter(username='idriss').exists():
            self.stdout.write(self.style.SUCESSS('Database has already been populated, Cancelling the operation'))
            return

        for k in range(10):
            user = Recipe(
                User,
                username=fake.unique.name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
            )
            category = Recipe(
                Category,
                name=fake.lexify(text='Category: ??'),
                description=fake.paragraph(nb_sentences=3)
            )
            article = Recipe(
                Article,
                title=fake.name(),
                author=foreign_key(user),
                type='TU',
                categories=foreign_key(category),
                content=fake.sentence()
            )
            user.make()
            category.make()
            article.make()
