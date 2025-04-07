FROM python:3.9-slim
# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . /app

# Expose the port
EXPOSE 8004

ENV PYTHONPATH=/app


# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8004"]
