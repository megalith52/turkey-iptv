#!/bin/bash

output_file="playlist.m3u"
echo "#EXTM3U" > "$output_file"

for script in src/channels/*.py; do
    echo "Working: $script"
    output=$(python3 "$script" 2>/dev/null)
    
    if [[ $output =~ ^([^:]+):[[:space:]]*(https?://.+)$ ]]; then
        name="${BASH_REMATCH[1]}"
        url="${BASH_REMATCH[2]}"

        echo "#EXTINF:-1 tvg-logo=\"https://raw.githubusercontent.com/megalith52/turkey-iptv/refs/heads/main/src/resources/${name,,}.png\" group-title=\"Ulusal\",$name" >> "$output_file"
        echo "$url" >> "$output_file"
    else
        echo "Error: $output" >&2
    fi
done

echo "M3U file generated: $output_file"