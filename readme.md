

# Script running djanggo
python manage.py migrate
python manage.py runserver

# add user
python manage.py createsuperuser --username admin --email admin@example.com


# running sudi without password
sudo visudo -f /etc/sudoers.d/zeekctl