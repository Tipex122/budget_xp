#!/bin/bash
NAME="BudgetXP" #Name of the application (*) 
DJANGODIR=/media/DOBI/budget_xp # Django project directory (*) 
SOCKFILE=/media/DOBI/run/$NAME.sock # we will communicate using this unix socket (*)

#USER=nginx # the user to run as (*) 
#GROUP=webdata # the group to run as (*)

#USER=www-data
#GROUP=www-data

USER=pi
GROUP=pi

NUM_WORKERS=3 # how many worker processes should Gunicorn spawn (*) 
TIMEOUT=120

DJANGO_SETTINGS_MODULE=budget_xp.settings # which settings file should Django use (*) 
DJANGO_WSGI_MODULE=budget_xp.wsgi # WSGI module name (*) 

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
###cd $DJANGODIR source /media/DOBI/venv/bin/activate 
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE 
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE) 
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn Programs meant to be run under supervisor 
# should not daemonize themselves (do not use --daemon)

#exec rm $SOCKFILE
#exec /media/DOBI/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
#exec /media/DOBI/venv/bin/gunicorn \
exec gunicorn \
	--bind=unix:$SOCKFILE \
	--workers $NUM_WORKERS \
	--name $NAME \
	--user $USER \
        --timeout $TIMEOUT \
	budget_xp.wsgi:application 
#  --name $NAME \
#  --workers $NUM_WORKERS \
#  --user $USER \
#  --bind=unix:$SOCKFILE
#  --bind 127.0.0.1:8003

#exec /media/DOBI/venv/bin/gunicorn --workers $NUM_WORKERS --bind 127.0.0.1:8001 ourcase.wsgi:application

