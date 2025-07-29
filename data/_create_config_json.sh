PARAMS_FILE=$1
OUTPUT_FILE=$2

if [ -z "$PARAMS_FILE" ] || [ -z "$OUTPUT_FILE" ]; then
  echo "Usage: $0 <params_file> <output_file>"
  exit 1
fi

if [ ! -f "$PARAMS_FILE" ]; then
  echo "User parameters file '$PARAMS_FILE' does not exist"
  exit 1
fi

echo '{"parameters": ' > $OUTPUT_FILE
cat $PARAMS_FILE >> $OUTPUT_FILE
echo '}' >> $OUTPUT_FILE
