FROM python:3.6-alpine
COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt
ENTRYPOINT ["doh-stub"]
