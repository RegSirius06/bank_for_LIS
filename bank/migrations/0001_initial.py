# Generated by Django 4.2.2 on 2023-09-04 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('balance', models.FloatField(default=0, verbose_name='Баланс:')),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный ID аккаунта.', primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='Not stated', max_length=40, verbose_name='Имя:')),
                ('middle_name', models.CharField(default='Not stated', max_length=40, verbose_name='Отчество:')),
                ('last_name', models.CharField(default='Not stated', max_length=40, verbose_name='Фамилия:')),
                ('user_group', models.CharField(choices=[('None', 'Другое'), ('Биология 1', 'Биология 1'), ('Биология 2', 'Биология 2'), ('Химия 1', 'Химия 1'), ('Химия 2', 'Химия 2'), ('Информатика', 'Информатика'), ('Физика 1', 'Физика 1'), ('Физика 2', 'Физика 2'), ('Физика 3', 'Физика 3'), ('Физика 4', 'Физика 4')], default='None', help_text='Группа обучения', max_length=40, verbose_name='Занятия:')),
                ('party', models.IntegerField(default=0, verbose_name='Отряд:')),
                ('theme_self', models.CharField(choices=[('default', 'По-умолчанию'), ('table-primary', 'Голубой'), ('table-secondary', 'Серый'), ('table-success', 'Зелёный'), ('table-danger', 'Красный'), ('table-warning', 'Жёлтый'), ('table-info', 'Светло-зелёный'), ('table-light', 'Светлая'), ('table-dark', 'Тёмная'), ('p-3 mb-2', 'По-умолчанию (аналог)'), ('p-3 mb-2 bg-primary text-white', 'Голубой (аналог)'), ('p-3 mb-2 bg-secondary text-white', 'Серый (аналог)'), ('p-3 mb-2 bg-success text-white', 'Зелёный (аналог)'), ('p-3 mb-2 bg-danger text-white', 'Красный (аналог)'), ('p-3 mb-2 bg-warning text-dark', 'Жёлтый (аналог)'), ('p-3 mb-2 bg-info text-dark', 'Светло-зелёный (аналог)'), ('p-3 mb-2 bg-light text-dark', 'Светлая (аналог)'), ('p-3 mb-2 bg-dark text-white', 'Тёмная (аналог)'), ('p-3 mb-2 bg-primary bg-gradient text-white', 'Голубой (аналог, градиент)'), ('p-3 mb-2 bg-secondary bg-gradient text-white', 'Серый (аналог, градиент)'), ('p-3 mb-2 bg-success bg-gradient text-white', 'Зелёный (аналог, градиент)'), ('p-3 mb-2 bg-danger bg-gradient text-white', 'Красный (аналог, градиент)'), ('p-3 mb-2 bg-warning bg-gradient text-dark', 'Жёлтый (аналог, градиент)'), ('p-3 mb-2 bg-info bg-gradient text-dark', 'Светло-зелёный (аналог, градиент)'), ('p-3 mb-2 bg-light bg-gradient text-dark', 'Светлая (аналог, градиент)'), ('p-3 mb-2 bg-dark bg-gradient text-white', 'Тёмная (аналог, градиент)')], default='default', help_text='Как это выглядит, можно посмотреть ниже.', max_length=50, verbose_name='Тема:')),
                ('account_status', models.CharField(blank=True, default='', max_length=100, verbose_name='Статус:')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь:')),
            ],
            options={
                'ordering': ['party', 'last_name'],
                'permissions': (('staff_', 'Принадлежность к персоналу'), ('transaction', 'Может создавать транзакции'), ('transaction_base', 'Может совершать переводы'), ('register', 'Может регистрировать пользователей'), ('edit_users', 'Может изменять пользователей'), ('ant_edit', 'Может изменять объявления'), ('meria', 'Мэрия в банке')),
            },
        ),
        migrations.CreateModel(
            name='daily_answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный ID.', primary_key=True, serialize=False)),
                ('name', models.TextField(default='none', max_length=500, verbose_name='Название задачи:')),
                ('text', models.TextField(max_length=1000, verbose_name='Условие задачи:')),
                ('cnt', models.FloatField(default=0, verbose_name='Награда:')),
                ('status', models.BooleanField(default=False, verbose_name='Это задача смены?')),
            ],
            options={
                'ordering': ['cnt'],
            },
        ),
        migrations.CreateModel(
            name='good',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный ID.', primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=250, verbose_name='Название:')),
                ('comment', models.CharField(default='', max_length=250, verbose_name='Комментарий:')),
                ('cost', models.FloatField(default=0, verbose_name='Цена:')),
            ],
            options={
                'ordering': ['-cost'],
            },
        ),
        migrations.CreateModel(
            name='plan',
            fields=[
                ('time', models.CharField(default='', max_length=250, verbose_name='Во сколько:')),
                ('comment', models.CharField(default='', max_length=250, verbose_name='Комментарий:')),
                ('number', models.IntegerField(default=0, verbose_name='Номер в списке: ')),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный ID.', primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='rools',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный ID.', primary_key=True, serialize=False)),
                ('num_type', models.CharField(choices=[('УкТ', 'Уголовный кодекс'), ('АкТ', 'Административный кодекс'), ('ТкТ', 'Трудовой кодекс'), ('КпТ', 'Кодекс премий')], default='УкТ', max_length=3, verbose_name='Раздел законов:')),
                ('num_pt1', models.IntegerField(default=1, help_text='Раздел кодекса')),
                ('num_pt2', models.IntegerField(default=0, help_text='Часть раздела')),
                ('comment', models.CharField(default='Не указано', max_length=250)),
                ('punishment', models.CharField(default='Не указано', max_length=100)),
            ],
            options={
                'ordering': ['num_type', 'num_pt1', 'num_pt2'],
            },
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('date', models.DateField(null=True)),
                ('comment', models.CharField(default='Не указано', max_length=70)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный ID транзакции.', primary_key=True, serialize=False)),
                ('counted', models.BooleanField(default=False, editable=False)),
                ('sign', models.CharField(choices=[('+', 'Начислить'), ('-', 'Оштрафовать')], default='+', max_length=1, verbose_name='Тип транзакции:')),
                ('cnt', models.FloatField(default=0, verbose_name='Количество:')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_trans', to='bank.account', verbose_name='Отправитель:')),
                ('history', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history_trans', to='bank.account', verbose_name='Создатель:')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_trans', to='bank.account', verbose_name='Получатель:')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
