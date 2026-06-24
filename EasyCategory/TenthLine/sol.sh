count=0
while IFS= read -r line; do
  ((count++))
  if [[ $count -eq 10 ]]; then
    echo "$line"
    exit 0
  fi
done < file.txt
