from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/blog')
def get_all_blogs():
    return {"status": "success"}

@app.get('/blog/{blog_id}')
def get_blog_by_id(blog_id: int = Path(None, description="The Blog ID you want to view", ge=0)):
    return {"status": "success"}