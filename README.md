# Robro's Page - Blog Template

A simple and elegant blog template based on the Striped theme by HTML5 UP, modified for easy content management through markdown files.

## Directory Structure

```
BlogTemplate/
├── index.html          # Main blog page
├── posts/             # Directory containing all blog posts
│   └── YYYY-MM-DD/    # Date-based directories for posts
│       ├── index.md   # Post content in markdown
│       └── images/    # Images for this post
├── assets/            # CSS, JS, and other assets
└── images/           # Global images used across the site
```

## How to Add a New Blog Post

1. Create a new directory in the `posts` folder with the date format `YYYY-MM-DD`
2. Inside this directory, create an `index.md` file with your post content
3. Add any images for the post in an `images` subdirectory

### Post Format

Each `index.md` should start with YAML front matter:

```yaml
---
title: Your Post Title
subtitle: Optional subtitle
date: YYYY-MM-DD
featured_image: images/your-image.jpg
---

Your post content here in markdown format...
```

## Local Development

1. Clone this repository
2. Make your changes
3. Test locally by opening `index.html` in a browser

## Deployment

1. Push changes to your GitHub repository
2. Enable GitHub Pages in your repository settings
3. Your blog will be available at `https://[username].github.io/[repository-name]`

## Credits

- Original template: [Striped by HTML5 UP](https://html5up.net/striped)
- Modified for easy blog management
- License: Creative Commons Attribution 3.0 Unported (CC BY 3.0)
