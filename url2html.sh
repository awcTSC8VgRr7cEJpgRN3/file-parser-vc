#!/bin/bash

for file in "$@"; do
  # Check the file type
  for filename in "$(ls "$file")"; do
    # Windows
    if grep -q "^URL=" "$filename"; then
        url=$(grep -oP '(?<=^URL=).*' "$filename")
    # macOS
    elif grep -q "<string>.*</string>$" "$filename"; then
        url=$(grep -oP '(?<=<string>).*?(?=</string>)' "$filename")
    # XDG
    elif grep -q '^URL\[$e\]=' "$filename"; then
        url=$(grep -oP 'URL\[\$e\]=\K.*' "$filename")
    else
        echo "Unsupported file type: $filename"
        continue
    fi

    # Generate HTML file with redirect to URL
    cat <<EOT > "${filename}.html"
<html>
    <head>
        <meta http-equiv="refresh" content="0; url=${url}" />
    </head>
    <body> </body>
</html>
EOT

    echo "Generated ${filename}.html with URL: ${url}"
  done
done
