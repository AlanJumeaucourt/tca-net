FROM python:3.9
RUN apt-get update && apt-get -y install cron
WORKDIR /app

COPY .env .
COPY models.py .
COPY crawler.py .
COPY discordBot.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
RUN echo $PYTHONPATH
# run crond as main process of container
CMD ["cron", "-f"]