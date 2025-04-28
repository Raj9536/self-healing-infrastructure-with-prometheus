FROM python:3.10-slim

# Install Ansible
RUN apt-get update && apt-get install -y ansible

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
