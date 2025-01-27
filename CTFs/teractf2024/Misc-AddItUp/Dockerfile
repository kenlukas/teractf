from python:3.12

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

#CMD ["python", "-i", "add_it_up.py"]
CMD ["python", "add_it_up.py"]
