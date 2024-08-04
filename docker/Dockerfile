# Set the working directory in the container
WORKDIR /app

# Copy backend code into the container
COPY ./backend /app/backend

# Copy frontend build directory into the container if you are serving it via Python
COPY ./frontend/build /app/frontend

# Install Python dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Expose the port the app runs on
EXPOSE 8000
