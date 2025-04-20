import os
import json

# 루트 디렉토리 경로 (본인이 만든 폴더)
base_dir = r"C:\Users\공Dok2\OneDrive\설광석\깃데스크톱\Pandas_study"

# 폴더와 해당 폴더에 들어갈 ipynb 파일명 리스트
structure = {
    "00_setup": [],
    "01_basics": ["01_series.ipynb", "02_dataframe.ipynb", "03_indexing.ipynb"],
    "02_analysis": ["01_filtering.ipynb", "02_groupby.ipynb", "03_merge_join.ipynb", "04_pivot.ipynb"],
    "03_visualization": ["01_plotting.ipynb"],
    "04_projects/telecom_churn": [],
    "04_projects/uk_crime_analysis": [],
    "notes": [],
}

# .ipynb 파일의 기본 내용 (빈 Jupyter 노트북)
empty_notebook = {
    "cells": [],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 2
}

# 폴더 및 파일 생성
for folder, notebooks in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for notebook in notebooks:
        notebook_path = os.path.join(folder_path, notebook)
        if not os.path.exists(notebook_path):
            with open(notebook_path, "w", encoding="utf-8") as f:
                json.dump(empty_notebook, f)
            print

