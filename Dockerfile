FROM python:3.11

WORKDIR /code

#COPY . /code/
COPY src/fishregression/main.py /code/
COPY requirements.txt /code/

RUN pip install git+https://github.com/j25ng/fishregression.git@0.2.0/cli

# 모델서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
