#!/bin/bash

# Configuration
SKILLS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WAREHOUSE_DIR="$SKILLS_ROOT/.agents/skills"
TARGET_DIRS=(
  "$SKILLS_ROOT/.claude/skills"
  "$SKILLS_ROOT/.cursor/skills"
  "$SKILLS_ROOT/.agent/skills"
)

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

ensure_dirs() {
  for dir in "${TARGET_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
      log_info "Creating directory: $dir"
      mkdir -p "$dir"
    fi
  done
  mkdir -p "$WAREHOUSE_DIR"
}

link_skill() {
  local skill_name=$1
  local skill_path="$WAREHOUSE_DIR/$skill_name"

  if [ ! -d "$skill_path" ]; then
    log_error "Skill not found in warehouse: $skill_name"
    return 1
  fi

  for target_dir in "${TARGET_DIRS[@]}"; do
    local target_path="$target_dir/$skill_name"
    
    if [ -e "$target_path" ] || [ -L "$target_path" ]; then
        if [ -L "$target_path" ]; then
            local current_target=$(readlink "$target_path")
            if [[ "$current_target" == "$skill_path" ]]; then
                continue 
            fi
        fi
        rm -rf "$target_path"
    fi

    ln -s "$skill_path" "$target_path"
    # log_info "Linked $skill_name to $target_dir"
  done
}

sync_skills() {
  log_info "Syncing skills from warehouse..."
  ensure_dirs
  
  if [ ! "$(ls -A "$WAREHOUSE_DIR")" ]; then
    log_info "Warehouse is empty. Nothing to sync."
    return
  fi

  local count=0
  for skill_path in "$WAREHOUSE_DIR"/*; do
    if [ -d "$skill_path" ]; then
      local skill_name=$(basename "$skill_path")
      link_skill "$skill_name"
      ((count++))
    fi
  done
  
  log_success "Synced $count skills to all agent directories."
}

install_skill() {
  local repo=$1
  if [ -z "$repo" ]; then
    log_error "Usage: ./manage-skills.sh install <owner/repo>"
    exit 1
  fi

  log_info "Installing skill: $repo"
  cd "$SKILLS_ROOT"
  
  # Standard installation
  npx skills add "$repo"
  
  if [ $? -eq 0 ]; then
    log_success "Installation complete."
    sync_skills
  else
    log_error "Installation failed."
    exit 1
  fi
}

case "$1" in
  sync)
    sync_skills
    ;;
  install)
    install_skill "$2"
    ;;
  *)
    echo "Usage: $0 {sync|install <owner/repo>}"
    exit 1
    ;;
esac
