FROM python:3.9-alpine

WORKDIR /app

# Install dependecies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application files
COPY . /app/

# Expose Port
EXPOSE 8189

# Run the application
ENTRYPOINT [ "python" ]
CMD ["app.py"]