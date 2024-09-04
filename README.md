```
  ____             _    ____             _        _____           _     
 |___ \  _ __   __| |  | __ ) _ __ __ _ (_)_ __  |_   _|__   ___ | |___ 
   __) || '_ \ / _` |  |  _ \| '__/ _` || | '_ \   | |/ _ \ / _ \| / __|
  / __/ | | | | (_| |  | |_) | | | (_| || | | | |  | | (_) | (_) | \__ \
 |_____||_| |_|\__,_|  |____/|_|  \__,_||_|_| |_|  |_|\___/ \___/|_|___/

```
# 2nd Brain Tools

This repository contains a collection of Python scripts designed to help manage and analyse Obsidian vaults. These tools aim to enhance the organisation, connectivity, and metadata of notes, helping to build a more robust "second brain".

## Current Features

### 1. Vault Inventory Script
- **File**: `obsidian-inventory.py`
- **Function**: Creates a simple inventory of all notes in the Obsidian vault.
- **Output**: Provides a summary of total notes, word count, and unique tags.

### 2. Metadata Note Generator
- **File**: `obsidian-metadata-generator.py`
- **Function**: Generates a metadata note summarising the vault's contents and structure.
- **Output**: Creates or updates a 'Vault Metadata.md' file in the vault with the following information:
  - Total notes and words
  - Tag statistics
  - Longest notes
  - Notes without tags
  - Placeholders for recent modifications and connectivity

## Planned Features

### 1. Automated Backlinking
- **Goal**: Create a script to automatically generate backlinks between notes based on keywords in titles and content.
- **Planned Functionality**:
  - Analyse note titles and content for key terms
  - Identify potential connections between notes
  - Insert backlinks in relevant notes
  - Optionally add tags based on identified connections

### 2. Content Similarity Analysis
- **Goal**: Implement more advanced text analysis to suggest connections between conceptually similar notes.
- **Planned Functionality**:
  - Use NLP techniques to analyse note content
  - Calculate similarity scores between notes
  - Suggest potential connections for manual review

### 3. Vault Health Check
- **Goal**: Create a script to identify potential issues or areas for improvement in a vault.
- **Planned Functionality**:
  - Identify orphaned notes (no incoming or outgoing links)
  - Flag notes with missing metadata or tags
  - Suggest potential merges for very short, related notes
  - Identify duplicate or near-duplicate content

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Install required dependencies:
   ```
   pip install pyyaml
   ```
3. Clone this repository:
   ```
   git clone https://github.com/SeaOfWolf/obsidian-note-inventory.git
   ```
4. Navigate to the project directory:
   ```
   cd obsidian-vault-tools
   ```
5. Update the `vault_path` variable in the scripts with the path to your Obsidian vault.
6. Run the desired script:
   ```
   python obsidian_inventory.py
   ```
   or
   ```
   python obsidian_metadata_generator.py
   ```

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please open an issue or submit a pull request.

## Backup Your Vault

> [!CAUTION]
> Always back up your Obsidian vault before running any scripts that modify its contents. While these tools are designed to be non-destructive, it's always better to be safe.
