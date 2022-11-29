FROM python:3
USER root

RUN mkdir -p /root/app
COPY requirements.txt /root
WORKDIR /root

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
