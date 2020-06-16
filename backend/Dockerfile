# Pull base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /runestone/

# Install Dependencies
COPY Pipfile Pipfile.lock /runestone/
RUN pip install pipenv && pipenv install --system

# Copy Project
COPY . /runestone/