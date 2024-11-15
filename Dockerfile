# Use official Node.js image as base
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Copy the SSL certificates into the container (from the local Certificates folder)
COPY certs/server.key /app/wisecow/server.key
COPY certs/server.crt /app/wisecow/server.crt

# Expose the port your app runs on
EXPOSE 4499

# Command to start the application
CMD ["npm", "start"]
