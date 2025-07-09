#!/bin/bash
find . -name "*.mojo" | entr -r pixi run mojo run main.mojo
