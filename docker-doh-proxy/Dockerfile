FROM python:3.6.9-alpine3.10
COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt
ENTRYPOINT ["doh-stub"]
