from fastapi import APIRouter, HTTPException, status
import ollama


router = APIRouter(prefix="/analyze")

@router.get("/", tags=["analyze"])
async def get_photo_analysis(file: str):
    try:
        with open(file, "rb") as f:
            image = f.read()

        response = ollama.chat(
            model = "qwen2.5vl",
            messages = [{
                "role": "user",
                "content": "This is a page from a bullet journal notebook. It uses the standard notation for bullet journaling. Destructure the page into readable json. Break everything into it's own element.",
                "images": [image]
            }]
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong while trying to analyze your photo")

    if not response.get("message", None) or not response.get("message", None).get("content", None):
        raise Exception("Did not get anything back from qwen")
    return {"bujo": response["message"]["content"]}
