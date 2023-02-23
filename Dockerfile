FROM python:3.10.10-slim 

RUN mkdir -p /home/app

COPY ./app /home/app

WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1


RUN pip install --upgrade pip \
&& pip install -r /home/app/requirements.txt \
&& pip freeze > revisarInstalados.txt

EXPOSE 8000/tcp

VOLUME /home/app

ADD ./app_build.sh /home/app
RUN chmod +x app_build.sh

ENTRYPOINT ["/home/app/app_build.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
