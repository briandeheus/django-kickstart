#!/bin/bash
set -e

APP="core"
CONCURRENCY=1
LOGLEVEL="info"

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --concurrency=*)
      CONCURRENCY="${1#*=}"
      shift
      ;;
    --concurrency)
      CONCURRENCY="$2"
      shift 2
      ;;
    --loglevel=*)
      LOGLEVEL="${1#*=}"
      shift
      ;;
    --loglevel)
      LOGLEVEL="$2"
      shift 2
      ;;
    -h|--help)
      echo "Usage: $0 [--concurrency=N] [--loglevel=debug|info|warning|error]"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

# Basic sanity check
if [ ! -f "manage.py" ]; then
    echo "Error: Must run from Django project root (manage.py not found)"
    exit 1
fi

exec celery -A "$APP" worker -B -l "$LOGLEVEL" -c "$CONCURRENCY"
