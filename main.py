from fastapi import FastAPI , Request
import index,json
import variables
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def runAutomation():
    return {"msg":"Successfull"}

@app.post("/runall")
async def getInformation(info : Request):
    req_info = await info.json()
    with open('Data/test3.json', 'w') as f:
        f.write(req_info)
    
    index.main()
