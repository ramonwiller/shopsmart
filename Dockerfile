FROM python:3.11.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache nginx

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /usr/src/shopsmart

COPY ./requirements.txt entrypoint.sh /usr/src/shopsmart
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /usr/src/shopsmart

RUN python manage.py migrate --no-input
RUN python manage.py collectstatic --noinput
RUN chown -R nginx:nginx /usr/src/shopsmart

EXPOSE 8000

ENTRYPOINT ["sh", "/usr/src/shopsmart/entrypoint.sh"]