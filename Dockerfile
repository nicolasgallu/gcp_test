# Use an official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables if needed (optional)
# ENV WPP_TOKEN=your-token-here
# ENV WPP_ID=your-id-here

# Command to run your app
CMD ["python", "main.py"]
