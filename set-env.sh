source virt-env/bin/activate
export DJANGO_DB_NAME="api-projex"
export DJANGO_USERNAME="julio"
export DJANGO_PASSWORD="12345678"
export SECRET_KEY='&o0ff+%&_th__u0!7uu82h6wsq)ac%bkh&81$+l#@77)01v)fk'
docker run -p 6379:6379 -d redis:2.8