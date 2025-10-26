# LaTeX Spacing Codes for Overleaf

## 📝 Quick Reference - Adding Spacing After Paragraphs

### Option 1: Global Paragraph Spacing (Recommended)
Add this in the preamble (after `\usepackage{balance}`):

```latex
\setlength{\parskip}{0.5em}  % 0.5em spacing between paragraphs
```

**Or for more spacing:**
```latex
\setlength{\parskip}{1em}  % 1em spacing (larger gap)
```

---

### Option 2: Manual Spacing Commands

#### Small Spacing
```latex
\smallskip  % Adds small vertical space
```

#### Medium Spacing
```latex
\medskip  % Adds medium vertical space
```

#### Large Spacing
```latex
\bigskip  % Adds large vertical space
```

#### Custom Spacing
```latex
\vspace{0.5cm}  % Adds 0.5cm of space
\vspace{1em}    % Adds 1em of space
\vspace{12pt}   % Adds 12pt of space
```

---

### Option 3: Line Breaks and Empty Lines

```latex
\\        % Single line break
\\[0.5em] % Line break with 0.5em extra space
\\[1em]   % Line break with 1em extra space
```

```latex
% Two blank lines in source = one paragraph break
Your text here.


Next paragraph starts here.
```

---

### Option 4: Inline Spacing

```latex
\paragraph{}   % Forces paragraph break
\noindent       % Removes indent for next paragraph
```

---

## 🎯 Recommended Code for Your Paper

### For IEEE Format (Your Paper)

Add after `\usepackage{balance}` in your preamble:

```latex
% Increase paragraph spacing
\setlength{\parskip}{0.4em plus 0.1em minus 0.05em}
```

This adds 0.4em spacing with some flexibility for LaTeX to adjust.

### To Add Spacing After Specific Sections

**After a paragraph:**
```latex
Your paragraph text here.

\vspace{0.3em}  % Add 0.3em space before next paragraph
```

**After a section:**
```latex
\section{Your Section}
\vspace{0.2em}

Your content starts here.
```

---

## 📊 Common Spacing Values

| Command | Spacing | Use Case |
|---------|---------|----------|
| `\smallskip` | ~3pt | Between items in list |
| `\medskip` | ~6pt | Between paragraphs |
| `\bigskip` | ~12pt | Between sections |
| `\vspace{0.5em}` | 0.5em | Custom small |
| `\vspace{1em}` | 1em | Custom medium |
| `\setlength{\parskip}{0.5em}` | 0.5em | Global between paragraphs |

---

## 💡 How to Apply to Your Paper

### Method 1: Global Spacing (Easiest)

Replace line 6 in your paper with:

```latex
\usepackage{balance}
\setlength{\parskip}{0.5em}  % Add this line
```

### Method 2: Add After Specific Sections

Find where you want spacing and add `\vspace{0.5em}`:

```latex
Your paragraph ends here.

\vspace{0.5em}

Next paragraph starts here.
```

---

## ✨ Complete Example

```latex
\documentclass[conference]{IEEEtran}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{url}
\usepackage{balance}
\setlength{\parskip}{0.5em}  % ← Add this for paragraph spacing

\begin{document}
```

This will add consistent spacing between all paragraphs in your paper!

---

## 🎯 Quick Copy-Paste for Your Paper

Add this line **after line 6** in your `PAPER_CORRECTED.tex`:

```latex
\setlength{\parskip}{0.5em}  % Paragraph spacing
```

**Position in your file:**
```latex
\usepackage{balance}
\setlength{\parskip}{0.5em}  % ← ADD THIS LINE

\begin{document}
```

---

## 📝 Spacing Units Explained

- `em` - Relative to font size (1em = current font size)
- `cm` - Centimeters  
- `pt` - Points (1in = 72.27pt)
- `ex` - Height of letter 'x'
- `in` - Inches

**For IEEE papers, recommended:**
- Between paragraphs: 0.4em to 0.6em
- Between sections: 0.5em to 1em

