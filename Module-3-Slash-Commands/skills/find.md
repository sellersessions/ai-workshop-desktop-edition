# Find Skill

Find files in your project using plain English descriptions instead of exact file names.

## How It Works

When the user says "find [something]", search the project for matching files using:
- File names and paths
- File contents
- File type (spreadsheet, document, image, etc.)
- Approximate dates if mentioned

## Instructions

1. Search the current project folder recursively
2. Match against the user's description -- be generous with matching
3. Show results as a list with file paths
4. If multiple matches, rank by relevance
5. If no matches, suggest what to search for instead

## Examples

- "find the supplier spreadsheet" -- search for .xlsx/.csv files with "supplier" in name or content
- "find the report from last week" -- search for recently modified documents
- "find all the product images" -- search for .jpg/.png/.webp files

## Output Format

For each match:
```
[file path] -- [brief description of what's in it]
```

Keep it scannable. No paragraphs.
