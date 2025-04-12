FROM python:3.11-slim as first

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && mkdir /deps \
 && pip install --no-cache-dir -r requirements.txt --target=/deps

FROM python:3.11-slim as final

WORKDIR /app

COPY --from=first /deps /usr/local/lib/python3.11/site-packages
COPY . .

EXPOSE 8000

CMD ["python", "run.py"]
