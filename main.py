from fastapi import FastAPI , Request
import index,json
import variables
app = FastAPI()


@app.get("/")
def runAutomation():
    return {"msg":"Successfull"}

@app.post("/runall")
async def getInformation(info : Request):
    req_info = await info.json()
    with open('Data/test3.json', 'w') as f:
        f.write(req_info)
    
    index.main()