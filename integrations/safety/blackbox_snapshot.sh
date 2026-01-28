#!/bin/bash

# --- BLACK BOX PROTOCOL ---
# Purpose: Create an "Insurance Snapshot" of critical assets BEFORE dangerous operations.
# Target: ../_XIUHE_BLACKBOX (External to Git Repo)

# 1. Configuration
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
BACKUP_ROOT="$PROJECT_ROOT/../_XIUHE_BLACKBOX"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
SNAPSHOT_DIR="$BACKUP_ROOT/$TIMESTAMP"

echo "🛡️  Initiating Black Box Snapshot..."
echo "📍  Project Root: $PROJECT_ROOT"
echo "📦  Backup Target: $SNAPSHOT_DIR"

# 2. Create Backup Directory
mkdir -p "$SNAPSHOT_DIR"

# 3. Critical Assets List
# Add files/folders here that MUST NEVER BE LOST
ASSETS=(
    "AI_Skills_Library"
    "SECRET_OPERATIONS_MANUAL.md"
    "Asher_Source_Profile_v1/03_Inventory_Assets/3.4_Document_Vault"
    "Asher_Source_Profile_v1/03_Inventory_Assets/3.5_Relationship_Database.md"
    "Asher_Source_Profile_v1/03_Inventory_Assets/3.3_Financial_Assets.md"
    "Asher_Source_Profile_v1/00_Archive"
)

# 4. Perform Backup
cd "$PROJECT_ROOT" || exit
for asset in "${ASSETS[@]}"; do
    if [ -e "$asset" ]; then
        echo "   -> Backing up: $asset"
        # Use cp -r for simple, browseable backup (easier to restore single files than tar)
        rsync -a --relative "$asset" "$SNAPSHOT_DIR/"
    else
        echo "   ⚠️  Warning: Asset not found: $asset"
    fi
done

# 5. Finalize
echo "✅  Black Box Snapshot Complete!"
echo "📂  Location: $SNAPSHOT_DIR"
echo "----------------------------------------"
