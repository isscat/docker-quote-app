# Use an official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app/

# Create logs directory
RUN mkdir /logs
# Switch to non-root user
USER user-inside-container
# Set permissions for the logs directory
RUN chown -R user-inside-container:user-inside-container /logs

# Expose port for Flask app
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
