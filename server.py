from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from chain import corrent_chain, summary_chain, optimized_chain
app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(app, corrent_chain, path="/correct", enabled_endpoints=["invoke", "stream_log"])
add_routes(app, summary_chain, path="/summary", enabled_endpoints=["invoke", "stream_log"])
add_routes(app, optimized_chain, path="/optimize", enabled_endpoints=["invoke", "stream_log"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)