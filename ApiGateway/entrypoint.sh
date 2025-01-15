#tail -f /dev/null

python manage.py migrate
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('facturedtest', 'facturedtest@example.com', 'facturedtest')" | python manage.py shell
python manage.py shell < authseeder.py
python manage.py runserver 0.0.0.0:8000
