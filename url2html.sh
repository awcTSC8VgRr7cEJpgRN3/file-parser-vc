#!/bin/bash

for file in "$@"; do
  for filename in "$(ls "$file")"; do
    # Check the file type
    if grep -q "^URL=" "$filename"; then
        url=$(grep -oP '(?<=^URL=).*' "$filename")
    elif grep -q "<string>.*</string>$" "$filename"; then
        url=$(grep -oP '(?<=<string>).*?(?=</string>)' "$filename")
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
