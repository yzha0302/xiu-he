# Slide Layout Components

Reusable CSS + HTML patterns for common slide types. Copy and customize.

## Base Slide Structure

All slides share this foundation:

```css
.slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: none;
    opacity: 0;
    transition: opacity 0.5s ease;
}

.slide.active {
    display: flex;
    opacity: 1;
}
```

---

## 1. Hero / Title Slide

Full-screen title with background image overlay.

```html
<div class="slide slide-hero active" data-slide="1">
    <div class="hero-content">
        <p class="overline">CATEGORY OR DATE</p>
        <h1>Main Title Here</h1>
        <p class="subtitle">Subtitle or tagline goes here</p>
        <div class="divider"></div>
        <p class="meta">Additional context</p>
    </div>
</div>
```

```css
.slide-hero {
    background: linear-gradient(135deg, rgba(28,28,28,0.9), rgba(20,20,20,0.95)),
                url('path/to/image.jpg');
    background-size: cover;
    background-position: center;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 60px;
}

.hero-content {
    position: relative;
    z-index: 1;
}

.overline {
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 30px;
}

.slide-hero h1 {
    font-family: var(--font-display);
    font-size: 5rem;
    font-weight: 600;
    margin-bottom: 25px;
}

.subtitle {
    font-family: var(--font-display);
    font-size: 1.6rem;
    font-style: italic;
    opacity: 0.9;
    max-width: 700px;
    margin: 0 auto 50px;
}

.divider {
    width: 120px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
    margin: 0 auto 30px;
}
```

---

## 2. Text + Image (Split)

Content on left, image on right.

```html
<div class="slide slide-split" data-slide="2">
    <div class="slide-header">
        <span class="number">01</span>
        <h2>Section Title</h2>
    </div>
    <div class="split-content">
        <div class="text-side">
            <p>Main paragraph content here.</p>
            <p class="highlight">Key takeaway or question</p>
        </div>
        <div class="image-side">
            <img src="image.jpg" alt="Description">
        </div>
    </div>
</div>
```

```css
.slide-split {
    flex-direction: column;
    padding: 50px 60px;
}

.slide-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 35px;
}

.slide-header .number {
    font-family: var(--font-display);
    font-size: 3.5rem;
    font-weight: 300;
    color: var(--primary);
    opacity: 0.4;
}

.slide-header h2 {
    font-family: var(--font-display);
    font-size: 2.6rem;
    font-weight: 500;
}

.split-content {
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    align-items: center;
}

.text-side p {
    font-size: 1.35rem;
    line-height: 1.8;
    margin-bottom: 25px;
}

.text-side .highlight {
    font-family: var(--font-display);
    font-size: 2rem;
    font-style: italic;
    color: var(--primary);
}

.image-side img {
    width: 100%;
    height: auto;
    max-height: 60vh;
    object-fit: cover;
    border-radius: 8px;
}
```

---

## 3. Timeline

Horizontal timeline with events.

```html
<div class="slide slide-timeline" data-slide="3">
    <div class="slide-header">
        <span class="number">02</span>
        <h2>Historical Timeline</h2>
    </div>
    <div class="timeline-container">
        <p class="timeline-intro">How did we get here?</p>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-year">1990</div>
                <div class="timeline-content">
                    <h4>Event Title</h4>
                    <p>Brief description of event</p>
                </div>
            </div>
            <!-- Repeat for more items -->
        </div>
        <p class="timeline-note">Concluding observation</p>
    </div>
</div>
```

```css
.slide-timeline {
    flex-direction: column;
    padding: 50px 60px;
}

.timeline-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.timeline-intro {
    text-align: center;
    font-size: 1.4rem;
    margin-bottom: 50px;
    opacity: 0.8;
}

.timeline {
    display: flex;
    justify-content: center;
    gap: 30px;
    position: relative;
}

.timeline::before {
    content: '';
    position: absolute;
    top: 45px;
    left: 15%;
    right: 15%;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
}

.timeline-item {
    flex: 1;
    max-width: 280px;
    text-align: center;
}

.timeline-year {
    font-family: var(--font-display);
    font-size: 3rem;
    font-weight: 600;
    color: var(--primary);
    margin-bottom: 25px;
    position: relative;
}

.timeline-year::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 50%;
    transform: translateX(-50%);
    width: 12px;
    height: 12px;
    background: var(--primary);
    border-radius: 50%;
}

.timeline-content {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 25px 20px;
    margin-top: 20px;
}

.timeline-content h4 {
    font-family: var(--font-display);
    font-size: 1.3rem;
    color: var(--primary-light);
    margin-bottom: 12px;
}

.timeline-note {
    text-align: center;
    margin-top: 50px;
    font-size: 1.1rem;
    opacity: 0.4;
    font-style: italic;
}
```

---

## 4. Stats / Data

Large numbers with labels.

```html
<div class="slide slide-stats" data-slide="4">
    <div class="slide-header">
        <span class="number">03</span>
        <h2>Key Statistics</h2>
    </div>
    <div class="stats-grid">
        <div class="stat-card">
            <span class="stat-number">1,100+</span>
            <h4>Primary Label</h4>
            <p>Supporting detail</p>
        </div>
        <!-- Repeat for more stats -->
    </div>
</div>
```

```css
.slide-stats {
    flex-direction: column;
    padding: 50px 60px;
}

.stats-grid {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    align-items: center;
    padding: 40px 0;
}

.stat-card {
    text-align: center;
    padding: 40px 30px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
}

.stat-number {
    font-family: var(--font-display);
    font-size: 4rem;
    font-weight: 600;
    color: var(--primary);
    display: block;
    margin-bottom: 15px;
}

.stat-card h4 {
    font-size: 1.2rem;
    margin-bottom: 8px;
}

.stat-card p {
    font-size: 0.95rem;
    opacity: 0.6;
}
```

---

## 5. Two-Column Comparison

Side-by-side comparison cards.

```html
<div class="slide slide-comparison" data-slide="5">
    <div class="slide-header">
        <span class="number">04</span>
        <h2>Comparison Title</h2>
    </div>
    <div class="comparison-grid">
        <div class="comparison-card">
            <div class="card-image">
                <img src="image1.jpg" alt="">
            </div>
            <div class="card-content">
                <h3>Option A</h3>
                <p class="card-label">"Their Perspective"</p>
                <p>Description text here.</p>
            </div>
        </div>
        <div class="comparison-card highlight">
            <div class="card-image">
                <img src="image2.jpg" alt="">
            </div>
            <div class="card-content">
                <h3>Option B</h3>
                <p class="card-label">"Alternative View"</p>
                <p>Description text here.</p>
            </div>
        </div>
    </div>
    <div class="comparison-conclusion">
        <p>Concluding insight about the comparison.</p>
    </div>
</div>
```

```css
.slide-comparison {
    flex-direction: column;
    padding: 50px 60px;
}

.comparison-grid {
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    margin: 20px 0;
}

.comparison-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    overflow: hidden;
}

.comparison-card.highlight {
    border-color: rgba(var(--primary-rgb), 0.4);
    background: rgba(var(--primary-rgb), 0.05);
}

.comparison-card .card-image {
    height: 200px;
    overflow: hidden;
}

.comparison-card .card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.comparison-card .card-content {
    padding: 30px;
}

.comparison-card h3 {
    font-family: var(--font-display);
    font-size: 1.5rem;
    color: var(--primary);
    margin-bottom: 15px;
}

.comparison-card .card-label {
    font-family: var(--font-display);
    font-size: 1.6rem;
    font-style: italic;
    margin-bottom: 15px;
}

.comparison-conclusion {
    text-align: center;
    padding: 25px;
    background: rgba(var(--primary-rgb), 0.08);
    border-radius: 12px;
}
```

---

## 6. Quote

Centered blockquote with attribution.

```html
<div class="slide slide-quote" data-slide="6">
    <p class="quote-label">Key Insight</p>
    <h2>Concept Name</h2>
    <div class="quote-block">
        <blockquote>
            The quoted text goes here, usually a significant statement that supports your argument.
        </blockquote>
        <p class="quote-author">Author Name — <span>Source Title (Year)</span></p>
    </div>
    <div class="quote-context">
        <p>Additional context or explanation below the quote.</p>
    </div>
</div>
```

```css
.slide-quote {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 60px 100px;
    text-align: center;
}

.quote-label {
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 15px;
}

.slide-quote h2 {
    font-family: var(--font-display);
    font-size: 3rem;
    margin-bottom: 50px;
}

.quote-block {
    max-width: 900px;
}

.quote-block blockquote {
    font-family: var(--font-display);
    font-size: 1.9rem;
    font-style: italic;
    line-height: 1.7;
    position: relative;
    padding: 0 50px;
}

.quote-block blockquote::before {
    content: '"';
    font-size: 6rem;
    position: absolute;
    left: -20px;
    top: -30px;
    color: var(--primary);
    opacity: 0.3;
}

.quote-author {
    margin-top: 30px;
    font-size: 1.1rem;
    color: var(--primary);
}

.quote-author span {
    opacity: 0.6;
    font-style: italic;
}

.quote-context {
    max-width: 800px;
    margin-top: 50px;
    padding-top: 40px;
    border-top: 1px solid rgba(var(--primary-rgb), 0.2);
}
```

---

## 7. Conclusion / Centered

Final slide with centered message.

```html
<div class="slide slide-conclusion" data-slide="7">
    <h2>Closing Question or Statement</h2>
    <div class="conclusion-text">
        <p>Primary message here.</p>
        <div class="keyword-row">
            <span>Word 1</span>
            <span>Word 2</span>
            <span>Word 3</span>
        </div>
        <p class="final-thought">The memorable final line that stays with the audience.</p>
    </div>
</div>
```

```css
.slide-conclusion {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 60px;
    background: radial-gradient(ellipse at center, var(--bg-medium) 0%, var(--bg-dark) 100%);
}

.slide-conclusion h2 {
    font-family: var(--font-display);
    font-size: 4rem;
    margin-bottom: 50px;
}

.conclusion-text p {
    font-size: 1.5rem;
    line-height: 1.9;
    margin-bottom: 15px;
}

.keyword-row {
    margin: 30px 0;
}

.keyword-row span {
    font-family: var(--font-display);
    font-size: 2rem;
    color: var(--primary);
    margin: 0 15px;
}

.final-thought {
    font-family: var(--font-display);
    font-size: 1.8rem;
    font-style: italic;
    max-width: 800px;
    margin-top: 50px;
    padding-top: 40px;
    border-top: 1px solid rgba(var(--primary-rgb), 0.3);
}
```

---

## 8. Image Grid (3-column)

Multiple images with captions.

```html
<div class="slide slide-grid" data-slide="8">
    <div class="slide-header">
        <span class="number">05</span>
        <h2>Image Gallery</h2>
    </div>
    <div class="image-grid">
        <div class="grid-card">
            <img src="img1.jpg" alt="">
            <div class="grid-overlay">
                <p class="grid-title">Item Name</p>
                <p class="grid-subtitle">Caption text</p>
            </div>
        </div>
        <!-- Repeat -->
    </div>
</div>
```

```css
.image-grid {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    padding: 20px 0;
}

.grid-card {
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    aspect-ratio: 3/4;
}

.grid-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.grid-card:hover img {
    transform: scale(1.05);
}

.grid-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 20px 15px;
    background: linear-gradient(transparent, rgba(0,0,0,0.9));
}

.grid-title {
    font-family: var(--font-display);
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 5px;
}

.grid-subtitle {
    font-size: 0.85rem;
    color: var(--primary);
}
```

---

## Navigation Component

Required for all presentations.

```html
<div class="nav">
    <button onclick="prevSlide()">← Previous</button>
    <button onclick="nextSlide()">Next →</button>
</div>
<div class="slide-counter">
    <span id="currentSlide">1</span> / <span id="totalSlides">12</span>
</div>
<div class="keyboard-hint">← → to navigate</div>
```

```css
.nav {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 12px;
    z-index: 100;
}

.nav button {
    background: transparent;
    border: 1px solid rgba(var(--primary-rgb), 0.4);
    color: var(--primary);
    padding: 12px 28px;
    font-size: 0.9rem;
    cursor: pointer;
    border-radius: 30px;
    transition: all 0.3s ease;
}

.nav button:hover {
    background: var(--primary);
    color: var(--bg-dark);
}

.slide-counter {
    position: fixed;
    bottom: 35px;
    right: 40px;
    font-size: 1rem;
    color: var(--text-muted);
}

.slide-counter #currentSlide {
    color: var(--primary);
}

.keyboard-hint {
    position: fixed;
    top: 20px;
    right: 25px;
    font-size: 0.8rem;
    color: var(--text-muted);
}
```

---

## Progress Bar

```html
<div class="progress-bar" id="progressBar"></div>
```

```css
.progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: var(--primary);
    transition: width 0.3s ease;
    z-index: 100;
}
```

---

## Navigation JavaScript

```javascript
let currentSlide = 1;
const totalSlides = document.querySelectorAll('.slide').length;

function updateProgress() {
    const progress = (currentSlide / totalSlides) * 100;
    document.getElementById('progressBar').style.width = progress + '%';
}

function showSlide(n) {
    const slides = document.querySelectorAll('.slide');
    if (n > totalSlides) currentSlide = 1;
    if (n < 1) currentSlide = totalSlides;

    slides.forEach(slide => slide.classList.remove('active'));
    document.querySelector(`[data-slide="${currentSlide}"]`).classList.add('active');
    document.getElementById('currentSlide').textContent = currentSlide;
    updateProgress();
}

function nextSlide() {
    currentSlide++;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide--;
    showSlide(currentSlide);
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ') {
        e.preventDefault();
        nextSlide();
    }
    if (e.key === 'ArrowLeft') {
        e.preventDefault();
        prevSlide();
    }
});

document.getElementById('totalSlides').textContent = totalSlides;
updateProgress();
```
