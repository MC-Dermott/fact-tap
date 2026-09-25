# Fact Tap

A quick-fire "hit the button" game for key number facts. A question appears, and students tap the
matching answer from a grid of up to 12 buttons before the timer runs out (30, 60 or 90 seconds,
or no timer).

Open `index.html` in any browser. It's a single file, so there's no install or server.

## What's in it

- **Fractions, decimals & percentages**: halves and quarters, tenths, fifths, hundredths, eighths,
  thirds, and values of one and over. All six conversion directions can be switched on or off.
- **Squares, cubes & roots**
- **Number bonds**: pairs to 100, and decimal pairs to 1

Wrong answers are re-asked three questions later. The results screen lists the facts a student
got wrong, shown as full equivalences (e.g. ⅜ = 0.375 = 37.5%). Best scores are saved in the
browser for each combination of settings.

## Adding a new fact set

Add an object to the `PACKS` array in `index.html`. The comment above it describes the format:

```js
{
  id: 'doubles',
  name: 'Doubles & halves',
  blurb: 'Double and halve numbers to 100.',
  example: 'double 35 = 70',
  reps: { n: { label: 'number' }, d: { label: 'double' } },
  families: [{ id: 'to50', name: 'Up to 50', on: true }],
  directions: [
    { id: 'dbl', label: 'Double it', from: 'n', to: 'd', on: true,
      ask: 'Double it', prompt: it => it.n },
    { id: 'hlv', label: 'Halve it', from: 'd', to: 'n', on: true,
      ask: 'Halve it', prompt: it => it.d },
  ],
  items: [{ family: 'to50', n: '35', d: '70' } /* ... */],
  summary: it => `double ${it.n} = ${it.d}`,
}
```

- `families` are the "Include" chips. Wrong-answer buttons are taken from the same family first.
- `directions` are the "Question types" chips. `ask` and `prompt` can be strings or functions of
  the item. If you leave them out, the game shows "Find the <label>" and the `from` value.
- Give a rep `kind: 'frac'` to draw values like `3/8` as stacked fractions.
