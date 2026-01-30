#!/bin/bash
# 快捷部署脚本 - 调用实际的部署脚本
exec ./scripts/moltbot/deploy_to_aws.sh "$@"
