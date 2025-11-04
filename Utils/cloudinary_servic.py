import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import uuid

cloudinary.config(
    cloud_name="dxrn8ww6t",
    api_key="114153943665445",
    api_secret="gXdjPjywc3WMJkJCOq6NRlNAgW0",
    secure=True
)

def upload_to_cloudinary(file, folder="students/documents"):
    try:
        unique_filename = str(uuid.uuid4())
        public_id = f"{folder}/{unique_filename}"
        upload_result = cloudinary.uploader.upload(
            file,
            public_id=public_id,
            overwrite=False,
            resource_type="auto"
        )
        print(f"Archivo subido a cloud: {upload_result['secure_url']} ({public_id})")
        return upload_result["secure_url"]
    except Exception as e:
        print(f"[ERROR] Error al subir a Cloudinary: {e}")
        return None