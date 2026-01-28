#!/bin/bash

# ========================================================
# 🌒 Shadow Sync [UP] | Local -> AWS Cloud
# ========================================================
# Usage: bash integrations/aws/shadow_sync_up.sh <AWS_IP> <SSH_KEY_PATH>
# Example: bash integrations/aws/shadow_sync_up.sh 1.2.3.4 ~/.ssh/lightsail.pem

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <AWS_IP> <SSH_KEY_PATH>"
  exit 1
fi

AWS_IP=$1
SSH_KEY=$2
REMOTE_USER="ubuntu"
REMOTE_DIR="~/xiu-he"

echo "🚀 Starting Shadow Sync [UP]..."
echo "📦 Sending PRIVATE assets to AWS ($AWS_IP)..."

# Use rsync to sync specific ignored files/folders
# --relative keeps the directory structure intact
rsync -avz --relative -e "ssh -i $SSH_KEY" \
  .env \
  Asher_Source_Profile_v1/03_Inventory_Assets/SECRET_Key_Vault.md \
  Asher_Source_Profile_v1/03_Inventory_Assets/3.4_Document_Vault \
  Asher_Source_Profile_v1/03_Inventory_Assets/3.3_Financial_Assets.md \
  Asher_Source_Profile_v1/03_Inventory_Assets/3.5_Relationship_Database.md \
  integrations/discord-bot/user_data.json \
  vibe-kanban/dev_assets/config.json \
  vibe-kanban/dev_assets/profiles.json \
  Asher_Source_Profile_v1/04_Strategy_Models/ \
  Asher_Source_Profile_v1/05_Protocols/ \
  Asher_Source_Profile_v1/06_Consciousness_Stream/ \
  $REMOTE_USER@$AWS_IP:$REMOTE_DIR

echo "✅ Shadow Sync [UP] Complete!"
