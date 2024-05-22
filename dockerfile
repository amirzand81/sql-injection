FROM python:3.10.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
       default-libmysqlclient-dev \
       pkg-config \
       gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requierments.txt /app/

RUN pip install --no-cache-dir -r requierments.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
