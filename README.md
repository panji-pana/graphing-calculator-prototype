# Graphing Calculator Prototype
3rd graphing calculator prototype

## Libraries used

1. *[numpy](https://numpy.org/)*- handles the mathematical side of the logic
2. *[matplotlib](https://matplotlib.org/)*- currently handles the animating of the graph (may update letter to use scipy)
3. *re*- this project handles identifying the style of formulae via regular expression (will make more robust later) i.e. identifies whether the typed equation follows a rearrangeable type (2x+y=2y-5x) and the aimed rearrangement (y=7x).

## General logic

The aim of this project is to design a graphing calculator that can take any input and make it into an understandable graph. Currently this only allows for linear, real graphing but the aim is to expand it to allow for non-linear graphs, transformations via matrices, co-ordinates, and vector calculations.
