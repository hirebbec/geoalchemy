from fastapi import APIRouter, Depends, File, UploadFile, status

from services.upload import UploadService

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/accidents", status_code=status.HTTP_200_OK)
async def upload_accidents(
    file: UploadFile = File(...), upload_service: UploadService = Depends()
) -> None:
    pass
    await upload_service.upload_accidents(file=file)
