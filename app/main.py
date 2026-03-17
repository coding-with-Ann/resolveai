from fastapi import FastAPI 

app = FastAPI(title="ResolveAI API")

@app.get('/')
def root():
    return{"message":"Welcome to ResolveAI API"}


@app.get('/health')
def health():
    return{"Status": "ok"}


