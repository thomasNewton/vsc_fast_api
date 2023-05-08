from fastapi import FastAPI,Request,Form 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import User, spell_number,Roll,save_to_file
from pydantic import EmailStr
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)  # html response for docs
async def root(request: Request):
    myData ="This string is the myData variable passed into the template from python"
    return templates.TemplateResponse("main.html",{"request":request,"myData":myData})


@app.post("/new/")
async def new_user(user: User) -> User:
    return user

@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.get("/user")
def new_user(request: Request):
    result = "New User Form Requested"
    return templates.TemplateResponse('user2.html', context={'request': request, 'result': result})


@app.post("/user")
def new_user(request: Request,firstName: str = Form(...),lastName:str = Form(...),
           password:str = Form(...), username:str = Form(...), roll:Roll =Form(...),
           email:EmailStr = Form(...)):
    usr={'username':username,'roll':roll,'first':firstName,
         'last':lastName,'user_id':3,'password':password, 'email':email}
    user = User(**usr)
    flag=save_to_file(usr)
    return flag
    
    """
    

class User(BaseModel):
    roll: Roll
    username: str
    first: str
    last: str
    user_id: int
    password: str

    """