from django.core.management.base import BaseCommand, CommandError

from news_portal.models import Post


class Command(BaseCommand):
    help = 'Удаление всех постов'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Вы действительно хотите удалить все публикации на сайте? yes/no')
        answer = input()

        if answer == 'yes':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Все публикации удалены!'))
            return

        self.stdout.write(self.style.ERROR('Нет доступа!'))