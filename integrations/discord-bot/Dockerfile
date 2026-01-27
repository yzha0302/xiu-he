
# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (none needed for basic bot, but good practice)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy local code to container
COPY . /app

# Install Python requirements
RUN pip install --no-cache-dir -r integrations/discord-bot/requirements.txt

# Environment variables should be passed at runtime (AWS Console / .env file)
# ENV DISCORD_TOKEN=... 

# Command to run the bot
CMD ["python", "integrations/discord-bot/bot.py"]
