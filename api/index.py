import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

milestone4_dir = os.path.join(BASE_DIR, "Milestone_4")
if os.path.exists(milestone4_dir) and milestone4_dir not in sys.path:
    sys.path.insert(0, milestone4_dir)

from backend.main import app

