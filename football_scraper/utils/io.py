# Utility functions for input/output operations
# utils/io.py

import pandas as pd
import os
from utils.styles import Colors

def save_to_csv(matches, filepath):
    df = pd.DataFrame(matches)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False, encoding="utf-8-sig")
    print(f"{Colors.GRE}[*] Results saved to: {filepath}")

def save_to_excel(matches, filepath):
    df = pd.DataFrame(matches)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_excel(filepath, index=False)
    print(f"{Colors.GRE}[*] Results saved to: {filepath}")
