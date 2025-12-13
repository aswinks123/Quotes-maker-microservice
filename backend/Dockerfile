# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend app
COPY . .

# Expose Flask default port
EXPOSE 5000

# Set environment variables for default Postgres (can override in Kubernetes or using helm later)
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=quotesdb
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432


# Start the Flask app
CMD ["python", "app.py"]

