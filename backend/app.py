from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    id: int
    title: str
    description: str
    user_id: int

@app.get('/blog')
def get_all_blogs():
    return {"status": "success"}

@app.get('/blog/{blog_id}')
def get_blog_by_id(blog_id: int = Path(None, description="The Blog ID you want to view", ge=0)):
    return {"status": "success"}

@app.post('/create-blog/{user_id}')
def create_blog(blog: Blog):
    return blog

@app.put('/edit-blog/{user_id}/{blog_id}')
def edit_blog(user_id: int, blog_id: int):
    return user_id, blog_id

@app.delete('/delete-blog/{user_id}/{blog_id}')
def delete_blog(user_id: int, blog_id: int):
    return {"status": "deleted"}

@app.delete('/delete-all-blogs/{user_id}')
def delete_blog(user_id: int):
    return {"status": "deleted"}