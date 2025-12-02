# CareerRaah — Mobile Home Page Notes

This file contains notes, implementation details and testing steps for the Mobile Home Page (`home.py`). Keep this as a living document for future improvements.

---

## Purpose

Create a mobile-first Home Page for the CareerRaah app using Streamlit and CSS. The page must look and feel like a native mobile screen (background gradient, compact header, horizontal trending chips, bottom navigation bar).

## Files

- `home.py` — Mobile Home Page implementation.
- `app.py` — Main application (existing). Keep `home.py` separate so it's easy to run and iterate on the mobile UI.

## Key Implementation Details

1. Page config
   - Title: `CareerRaah | Home`
   - Layout: `centered` to keep content readable on mobile

2. Background & layout
   - Full-screen gradient applied to `.stApp` so the entire viewport uses the gradient.
   - CSS uses `background-attachment: fixed` so the gradient stays steady while scrolling.
   - `.block-container` padding-top set to `0` so content starts higher on the viewport (mobile friendly).

3. Trending Questions
   - Visual chips are rendered as a horizontally scrollable HTML `div` (`.chips-container`) with child `.chip` elements.
   - For accessibility and interaction we also render the same questions as functional Streamlit `st.button` controls in two columns below the chips.
   - This preserves the visual horizontal layout while providing Python callbacks when a user taps a question.

4. Bottom Navigation
   - Since Streamlit does not have a native bottom bar, we implement a visual bottom nav using a fixed HTML `div` (`.bottom-nav`).
   - This is primarily visual — to make the nav actionable we'd wire buttons or use `st.button` in a container and then use CSS to position that container fixed to the bottom if needed.

5. Logo handling
   - `home.py` attempts to load `logo/careerRaah-logo.png` from the project directory. If missing, we fall back to a simple text title.

6. Touch targets and spacing
   - Chips and buttons are sized to be thumb-friendly (padding and minimum height).
   - Buttons styled with subtle shadows to appear tappable.

## Styling Notes

- Colors:
  - Light Blue: `#E0F7FA`
  - Soft Orange: `#FFE0B2`
  - Cream: `#FFF3E0`
  - Brand blue: `#1A3C8D`

- Fonts:
  - Keep font-family minimal for mobile. Using heavy external fonts hurts load performance on weak mobile networks.

- Breakpoints:
  - `max-width: 767px` treated as mobile. Slightly larger screens use slightly bigger chips.

## Accessibility & Performance

- Avoid loading heavy web fonts on first load; use system fonts where possible.
- Use `alt` text for images if adding images via `st.image`.
- Ensure all interactive elements (buttons) are reachable and large enough for touch (approx 44–48px height).

## Testing Checklist

- [ ] Open `home.py` on real mobile device using `streamlit run home.py` and point device browser to `http://<dev-machine-ip>:8501`.
- [ ] Verify gradient covers entire screen and doesn't produce horizontal scroll.
- [ ] Check that `.chip` elements scroll horizontally and are readable.
- [ ] Test that the functional buttons below the chips respond (info toasts appear).
- [ ] Ensure the bottom nav does not cover important content (main content should have `padding-bottom: 90px` to leave room).

## Future Improvements

- Make the bottom nav interactive by using `st.session_state` and `st.button` inside a container whose CSS is adjusted to be fixed at the bottom.
- Add animation or micro-interactions for chip taps (ripple effect) using small SVG or CSS keyframes.
- Replace local logo with CDN-hosted asset where appropriate for production.
- Add A/B testing to try different chip sizes, spacing, and nav iconography.

---

Created: 2025-12-02
