from typing import List

import uvicorn
import ast
from fastapi import FastAPI, File, UploadFile,Form
from visualization import create_graphs, create_bar_chart
from code_quality_checker import analyze_code

app = FastAPI()


@app.post("/analyze")
async def analyze(files: List[UploadFile] = File(...)):
    results = {}
    for file in files:
        content = await file.read()
        analysis_result = analyze_code(content.decode('utf-8'))
        results[file.filename] = len(analysis_result[0])
        create_graphs(analysis_result[0], analysis_result[1], file.filename)

    create_bar_chart(results)

    return {"results": results}

@app.post("/alerts")
async def alerts(files: List[UploadFile] = File(...)):
    analysis_results = {}
    for file in files:
        content = await file.read()
        analysis_results[file.filename] = analyze_code(content.decode('utf-8'))

    alerts_only = {file: data[0] for file, data in analysis_results.items()}
    return {"alerts": alerts_only}

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000)