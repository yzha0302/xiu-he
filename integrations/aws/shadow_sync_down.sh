#!/bin/bash

# ========================================================
# 🌘 Shadow Sync [DOWN] | AWS Cloud -> Local
# ========================================================
# Usage: bash integrations/aws/shadow_sync_down.sh <AWS_IP> <SSH_KEY_PATH>

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <AWS_IP> <SSH_KEY_PATH>"
  exit 1
fi

AWS_IP=$1
SSH_KEY=$2
REMOTE_USER="ubuntu"
REMOTE_DIR="~/xiu-he"

echo "🚀 Starting Shadow Sync [DOWN]..."
echo "⬇️ Pulling PRIVATE assets from AWS ($AWS_IP)..."

# Sync back from server to local
rsync -avz --relative -e "ssh -i $SSH_KEY" \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/.env . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/Asher_Source_Profile_v1/03_Inventory_Assets/SECRET_Key_Vault.md . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/Asher_Source_Profile_v1/03_Inventory_Assets/3.4_Document_Vault . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/Asher_Source_Profile_v1/03_Inventory_Assets/3.3_Financial_Assets.md . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/Asher_Source_Profile_v1/03_Inventory_Assets/3.5_Relationship_Database.md . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/integrations/discord-bot/user_data.json . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/vibe-kanban/dev_assets/config.json . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/vibe-kanban/dev_assets/profiles.json . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/Asher_Source_Profile_v1/04_Strategy_Models/ . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/Asher_Source_Profile_v1/05_Protocols/ . \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR/Asher_Source_Profile_v1/06_Consciousness_Stream/ .

echo "✅ Shadow Sync [DOWN] Complete!"
