FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt to the image
COPY requirements.txt ./

# Install dependencies with out caching
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code: (we used this step  below pip install build image faster)
COPY . .

# Expose the port PyWebIO runs on (for documentation)
EXPOSE 8080

# Set environment variable for backend (default fallback)
ENV BACKEND_URL=http://backend:5000

# Start the PyWebIO server
CMD ["python", "app.py"]