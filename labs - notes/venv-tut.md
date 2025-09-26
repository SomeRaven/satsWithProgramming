# How to make python venv work in vscode 
## If you're already in VS Code:
1. **Open the integrated terminal: Terminal → New Terminal (or Cmd + backtick)**
2. **The terminal should already be in your project folder**
3. this: deactivate
rm -rf venv
python3 -m venv venv
4. **Activate the virtual environment:** source venv/bin/activate
5. **install all packages:** python -m pip install pandas numpy matplotlib seaborn

# imports for each assignment
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns