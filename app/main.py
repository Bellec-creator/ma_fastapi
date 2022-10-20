from fastapi import FastAPI

from app.routes.test import router_test

app = FastAPI()

@app.get("/")
def list_all_routes():
    url_list = [{"path": route.path, "name": route.name}
        for route in app.routes]
    return url_list


app.include_router(router_test, tags=['test'], prefix='/test')
