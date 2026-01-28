#!/bin/bash

# Configuration
PROJECT_DIR="/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/Projects/vibe-kanban"
FRONTEND_PORT=3005

echo "🚀 Starting Vibe Kanban..."
echo "📂 Project Directory: $PROJECT_DIR"
echo "🌐 Port: $FRONTEND_PORT"

# Navigate to project directory
cd "$PROJECT_DIR" || { echo "❌ Failed to find project directory!"; exit 1; }

# Set Port and Launch
export PORT=$FRONTEND_PORT
npm run dev
