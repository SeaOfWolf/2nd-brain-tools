import os
import yaml
from collections import defaultdict
from datetime import datetime

def extract_yaml_frontmatter(content):
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            frontmatter = content[3:end].strip()
            try:
                return yaml.safe_load(frontmatter)
            except yaml.YAMLError:
                return {}
    return {}

def extract_tags(content):
    return [word[1:] for word in content.split() if word.startswith('#')]

def inventory_notes(vault_path):
    inventory = defaultdict(list)
    
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                frontmatter = extract_yaml_frontmatter(content)
                tags = extract_tags(content)
                word_count = len(content.split())
                
                note_info = {
                    'title': os.path.splitext(file)[0],
                    'path': os.path.relpath(file_path, vault_path),
                    'tags': list(set(frontmatter.get('tags', []) + tags)),
                    'word_count': word_count,
                    'frontmatter': frontmatter
                }
                
                inventory['notes'].append(note_info)
    
    return inventory

def generate_metadata_note(inventory, vault_path):
    total_notes = len(inventory['notes'])
    total_words = sum(note['word_count'] for note in inventory['notes'])
    all_tags = [tag for note in inventory['notes'] for tag in note['tags']]
    tag_counts = defaultdict(int)
    for tag in all_tags:
        tag_counts[tag] += 1
    
    top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    metadata_content = f"""---
title: Vault Metadata
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
tags: [metadata, vault-summary]
---

# Vault Metadata

Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview
- Total notes: {total_notes}
- Total words: {total_words}
- Average words per note: {total_words // total_notes}

## Tag Statistics
- Unique tags: {len(tag_counts)}
- Top 10 tags:
{chr(10).join([f'  - #{tag}: {count}' for tag, count in top_tags])}

## Notes without tags: {sum(1 for note in inventory['notes'] if not note['tags'])}

## Longest notes (by word count):
{chr(10).join([f"1. [{note['title']}]({note['path']}) - {note['word_count']} words" for note in sorted(inventory['notes'], key=lambda x: x['word_count'], reverse=True)[:5]])}

## Most recently modified notes:
(This section requires additional file system access, which is not implemented in this script)

## Least connected notes:
(This section requires analysis of note connections, which is not implemented in this script)

---

This metadata note was automatically generated. To update it, run the metadata generation script again.
"""

    metadata_path = os.path.join(vault_path, 'Vault Metadata.md')
    with open(metadata_path, 'w', encoding='utf-8') as f:
        f.write(metadata_content)
    
    print(f"Metadata note has been created/updated at: {metadata_path}")

# Usage
vault_path = '/path/to/vault'
inventory = inventory_notes(vault_path)
generate_metadata_note(inventory, vault_path)
