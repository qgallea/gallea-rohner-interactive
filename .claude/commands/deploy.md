# /deploy

Build and deploy the site to GitHub Pages.

## Usage
```
/deploy [--dry-run]
```

## Process
1. Verify all pages render: `cd site && quarto render`
2. Check for errors in the build output
3. If `--dry-run`: stop here, report build status
4. Run pre-deploy checks:
   - [ ] All data files present in `site/data/`
   - [ ] No broken `FileAttachment()` references
   - [ ] Slider math verified: ME at trade=0.40 = 0.00372
   - [ ] Citation visible in footer
   - [ ] Total output size < 10 MB
5. Commit any uncommitted changes: `git add -A && git commit -m "Update site"`
6. Deploy: `cd site && quarto publish gh-pages --no-prompt`
7. Report the live URL: `https://qgallea.github.io/gallea-rohner-interactive/`

## First-Time Setup
If the repo doesn't have a `gh-pages` branch yet:
```bash
git checkout --orphan gh-pages
git reset --hard
git commit --allow-empty -m "Init gh-pages"
git push origin gh-pages
git checkout main
```

## Troubleshooting
- "fatal: not a git repository" → run `git init` and add remote
- "gh-pages branch not found" → run the first-time setup above
- Large file errors → check that `raw_data/` is in `.gitignore`
- OJS errors only visible in browser → open the deployed URL and check console
