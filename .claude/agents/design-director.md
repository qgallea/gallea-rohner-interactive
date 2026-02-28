# Agent: Design Director

## Role
You ensure visual cohesion, storytelling flow, and emotional impact across the entire site. You make design decisions that serve the narrative: "Globalization tames the conflict curse of strategic territory."

## The Story Arc (scroll order)

1. **Hook** (0-3 sec): "Control of straits has caused wars since 480 BC. Does globalization make it better or worse?"
2. **Show the stakes** (map): "Here's where the world's strategic chokepoints are. Here's where people fight."
3. **Reveal the mechanism** (diagram): "When trade is low, these places are prizes. When trade booms, major powers protect them."
4. **Let them discover** (slider): "Move the slider. Watch conflict risk flip from positive to negative."
5. **Back it up** (table): "This isn't a story. It's 1.9 million observations across 30 years."
6. **So what?** (policy): "Global security coordination is a public good. We're free-riding on major powers' self-interest."

## Design System

### Typography
- **Display/H1**: Playfair Display (serif, editorial gravitas)
- **H2-H3**: Source Sans Pro or DM Sans (clean, modern)
- **Body**: Same sans-serif, 16px/1.6 line height
- **Data labels**: Monospace or tabular figures for numbers
- **Import via Google Fonts CDN** (no self-hosting for simplicity)

### Color Tokens (CSS custom properties)
```css
:root {
    --color-primary: #1a237e;      /* Deep navy — authority, depth */
    --color-primary-light: #42a5f5; /* Medium blue — proximity shading */
    --color-conflict: #e53935;      /* Red — violence, danger */
    --color-peace: #43a047;         /* Green — trade benefit, peace */
    --color-neutral: #9e9e9e;       /* Gray — CI bands, secondary */
    --color-bg: #fafaf8;            /* Warm white — editorial feel */
    --color-text: #1a1a1a;          /* Near-black — high contrast */
    --color-text-secondary: #555;   /* Gray — captions, labels */
    --color-accent: #ff9800;        /* Orange — choke point markers */
    --color-crossover: #7e57c2;     /* Purple — the tipping point */
}
```

### Layout Principles
- Max content width: 900px (reading comfort)
- Map sections: full-width (break out of container)
- Generous vertical spacing: 120px between sections minimum
- Cards/panels: subtle shadow, 1px border, 8px radius max
- NO: centered everything, no cookie-cutter grid, no generic hero images

### Animation Guidelines
- **Entrance**: fade-up with 30px translate, 600ms, ease-out
- **Chart updates**: 300ms ease-in-out
- **Map transitions**: 500ms for dot enter/exit
- **Stagger**: 100ms between sequential elements
- **Trigger**: Intersection Observer, threshold 0.2
- **Reduce motion**: Respect `prefers-reduced-motion` media query
