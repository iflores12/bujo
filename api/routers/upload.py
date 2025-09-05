from fastapi import APIRouter, HTTPException, status, File, UploadFile
import uuid

router = APIRouter(prefix="/upload")


@router.post("/", tags=["upload"])
async def upload(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"

    try:
        contents = await file.read()
        with open(file.filename, "wb") as f:
            f.write(contents)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong while uploading file"
        )
    finally:
        file.file.close()

    return {"filename": file.filename}
