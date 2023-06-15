# Pursuit curves simulations using `manim`
## Why?
I didn't mean to. I was researching pursuit curves and got distracted.

## Prerequisits
Install `manim`. [They](https://docs.manim.community/en/latest/installation.html) can help you.

## Usage
The code consists of three classes:
 - The simulation of Bouguer's problem of the pirate and the merchant ships, `BouguerCurve`.
 - The simulation of Hathaway's problem of the dog and the duck in the pond, `HathawayCurve`.
 - A general class for pursuits, `pursuitCurves`.
In `pursuitCurves`, the speed of the pursued is given by the function `speed`, while the path is given by `parametricPath`. Once those are modified according to your purposes, you then run on the terminal:
```
manim -p Pursuit-simulations.py pursuitCurves --fps=60
```
The flag `--fps=60` is suggested since a greater frame rate generates a better numerical approximation of the curve.

