from fastapi import FastAPI, Form, Query,Body, Response
from typing import Union, Annotated, Any
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse
from model import Item, ModelName,Roll,User, fake_items_db, UserIn,Image,UserOut,Uzer,New_UZer


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"key1":"value1"}

@app.get("/{path_param}") # shows how to recieve/send path and query variable parameters
async def key_return(path_param, query_param: str | None = None):
    return {"path param":path_param,"query param":query_param}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

'''
@app.get("/items/{item_id}")  # path parameter=item_id  query param q
def read_item_get(item_id: int, q: Union[str, None] = None):
    return {"item_id":item_id, "Q":q}


@app.put("/items/{item_id}")  # data sent in the request BODY not the url for this request
def update_item_put(item_id: int, item: Item):
    #return {"item_name": item.name, "item_id": item_id}
    return {"item_id": item_id, **item.dict()}


@app.post("/items/{item_id}")
async def create_item_post(item_id: int, name: str, price: float, is_offer: bool):
    item = {"item_id": item_id, "name": name, "price": price, "is_offer": is_offer}
    # Here you can process the received data as per your requirement
    return item
'''

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
    results = {"item_id": item_id, "item": item, "user": user,"import":importance}
    return results


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
     
    return item_dict
   


@app.get("/models/{model_name}") # use enum to define parameters 
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/")   # all the stuff you can do with query and annotated
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            regex="^fixedquery$",
            deprecated=True,
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/postit/", response_model= Item)
async def create_item(item: Item) -> Any:
    return item

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) ->Any:
    return user

@app.post("/new/")
async def new_user(uzer: New_UZer) -> Uzer:
    return uzer
    
@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})