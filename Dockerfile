FROM python:3

ENV APP /opt/imageproc/

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt && \
    mkdir $APP && \
    chgrp 0 -R $APP && chmod g=u -R $APP

WORKDIR $APP
COPY . $APP

USER 1001

EXPOSE 5000

CMD ["gunicorn", "-w 4", "run:app"]