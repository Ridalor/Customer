FROM python:3

WORKDIR /usr/src

COPY . /usr/src

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "run.py" ]
