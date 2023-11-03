FROM 3.10-alpine3.17

WORKDIR /dunnhumby

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . /dunnhumby


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
