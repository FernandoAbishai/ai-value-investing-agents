#!/bin/bash
# Record user prompts in a local JSONL log.
# Called by the user_prompt_submit hook; stdin contains the submitted prompt.

LOG_DIR="$HOME/ai-value-investing-agents/logs"
LOG_FILE="$LOG_DIR/command-log.jsonl"
COUNTER_FILE="$LOG_DIR/.counter"

mkdir -p "$LOG_DIR"

PROMPT=$(cat)

# Ignore empty input.
[ -z "$PROMPT" ] && exit 0

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Keep only the first 200 characters and normalize newlines/quotes for JSONL logging.
PROMPT_SHORT=$(echo "$PROMPT" | head -c 200 | tr '\n' ' ' | tr '"' "'")

echo "{\"time\":\"$TIMESTAMP\",\"prompt\":\"$PROMPT_SHORT\"}" >> "$LOG_FILE"

if [ -f "$COUNTER_FILE" ]; then
    COUNT=$(cat "$COUNTER_FILE")
else
    COUNT=0
fi
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"

# Every 10 prompts, emit a lightweight reminder through the hook output.
if [ $((COUNT % 10)) -eq 0 ]; then
    TOTAL=$(wc -l < "$LOG_FILE" | tr -d ' ')
    echo "[Command log] ${TOTAL} prompts recorded. Consider running /command-log to summarize recent context."
fi
