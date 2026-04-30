from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def home():
    return {"message": "service is running"}


url_map = {}
counter = 1


@app.post("/shorten")
def shorten_url(long_url: str):
    global counter
    short_code = str(counter)
    url_map[short_code] = long_url
    counter += 1
    return {"short_url": f"https://localhost:8000/{short_code}"}


@app.get("/short_code")
def redirect(short_code: str):
    long_url = url_map.get(short_code)
    if long_url:
        return RedirectResponse(long_url)
    else:
        return {"error": "Url not found"}
