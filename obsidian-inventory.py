import os
import yaml
from collections import defaultdict

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

# Usage
vault_path = '/path/to/vault'
inventory = inventory_notes(vault_path)

# Print summary
print(f"Total notes: {len(inventory['notes'])}")
print(f"Total words: {sum(note['word_count'] for note in inventory['notes'])}")
print(f"Unique tags: {len(set(tag for note in inventory['notes'] for tag in note['tags']))}")

# You can now process 'inventory' further or save it to a file
