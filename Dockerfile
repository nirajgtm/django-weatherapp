FROM alpine
COPY . /src
WORKDIR /src
RUN apk add python3 \
    py-pip \
    && pip3 install django \
    && pip3 install requests \
    && apk add git \
    && git clone https://github.com/nirajgtm/django-weatherapp.git \
    && cd django-weatherapp
EXPOSE 8000
CMD [ "python3", "./manage.py runserver 0.0.0.0:8000" ]
