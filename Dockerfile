# Use an official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create the user inside the container
RUN useradd -ms /bin/bash user-inside-container

# Create and set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app/

# Create logs directory
RUN mkdir /logs

# Set permissions for the logs directory
RUN chmod -R 777  .

# Switch to non-root user
USER user-inside-container
RUN echo $(whoami) >> user.txt

# Expose port for Flask app
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
