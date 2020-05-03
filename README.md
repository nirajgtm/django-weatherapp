# django-weatherapp

The App has been hosted on AWS here : http://3.134.98.137/

You can also download docker image for the App on your machine easily if you have docker installed on your machine using following command:

`docker image build -t myapp https://github.com/nirajgtm/django-weatherapp.git`

It will download small docker image with Alpine OS as base image, then to run the app use following command:

`docker container run -d --name myapp -p 8000:8000 myapp`

App will be running on localhost:8000, you can open it in your browser by going to following address:

`localhost:8000`
