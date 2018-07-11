FROM python:3.7.0-stretch

RUN pip install --no-cache-dir --upgrade setuptools pip

RUN pip install --no-cache-dir pipenv

RUN pipenv lock

RUN pipenv install --dev --system --deploy

WORKDIR /code

COPY ../../ .

CMD python /code/app.py
