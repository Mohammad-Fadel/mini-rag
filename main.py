from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def root():
    return {'message': 'welcome home'}