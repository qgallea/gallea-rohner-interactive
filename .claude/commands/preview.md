# /preview

Start Quarto live preview for development.

## Usage
```
/preview
```

## Process
1. `cd site`
2. `quarto preview --port 4200 --no-browser`
3. Report the local URL to the user
4. Keep running — edits to `.qmd` files will auto-reload

## Notes
- If preview fails, check `quarto check` for missing dependencies
- OJS errors show in the browser console, not the terminal
- Python chunks require the Python environment to be set up
