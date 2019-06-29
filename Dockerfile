FROM python:3.7-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=ankitemp/app.py

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]