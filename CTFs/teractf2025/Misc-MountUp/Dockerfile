FROM python:3.11-slim
RUN pip install --no-cache-dir flask==3.1.1

WORKDIR /app

COPY app .

RUN mv flag.txt /flag-$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1).txt && \
    chown -R nobody:nogroup /app

USER nobody

EXPOSE 5000

CMD ["python", "app.py"]
