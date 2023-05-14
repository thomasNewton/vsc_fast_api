from fastapi import FastAPI,Request,Form 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import User, spell_number,Roll,save_to_file, read_data
from pydantic import EmailStr
from jinja2 import Template


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
    
    
@app.get("/list_users")
def list_users(request: Request):
    #f = open("users.json")
    #data=f.read()
    #f.close()
    #print(type(data))
    data = read_data("users.json")
    return templates.TemplateResponse('list_users.html', context={'request': request,"data":data})



@app.get("/x")
def test(request: Request):
    data = read_data("users.json")
    print (data)
    print(type(data))


    return templates.TemplateResponse("userJin.html", context={'request': request,"data":data})


@app.get("/y", response_class=HTMLResponse)
def test2(request: Request):
    data = read_data("users.json")
    f = open("templates/sres.html")
    template_string =f.read()
    template = Template(template_string)
    output = template.render(data=data)
    return output


"""
    

class User(BaseModel):
    roll: Roll
    username: str
    first: str
    last: str
    user_id: int
    password: str

    """