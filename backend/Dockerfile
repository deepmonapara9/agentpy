# This is a Python version of the official Python 3 Dockerfile
FROM python:latest

# Creating Python virtual environment to isolate python from the system-level python
RUN python -m venv /opt/venv
# Making sure we use the virtualenv:
ENV PATH=/opt/venv/bin:$PATH

# This will be the directory where the app is mounted in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt

# This will install the dependencies and the app in the container
RUN pip install -r /tmp/requirements.txt

# 
COPY ./src .

CMD ["python", "-m", "http.server", "8000"]
