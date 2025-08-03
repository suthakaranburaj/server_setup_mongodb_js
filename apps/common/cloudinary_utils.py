import cloudinary
import cloudinary.uploader
from django.conf import settings
import os

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET
)

def upload_to_cloudinary(file_path):
    """Upload file to Cloudinary and return secure URL"""
    try:
        if not file_path or not os.path.exists(file_path):
            return None
        
        response = cloudinary.uploader.upload(
            file_path,
            resource_type="auto"
        )
        
        # Clean up local file
        if os.path.exists(file_path):
            os.remove(file_path)
        
        return response.get('secure_url')
    
    except Exception as e:
        # Clean up local file on error
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
        raise Exception(f"Failed to upload file to Cloudinary: {str(e)}")

def delete_from_cloudinary(public_id):
    """Delete file from Cloudinary"""
    if not public_id:
        raise Exception("Public ID is missing for deletion")
    
    try:
        response = cloudinary.uploader.destroy(public_id)
        
        if response.get('result') not in ['ok', 'not found']:
            raise Exception("Error while deleting the image from Cloudinary")
        
        return response
    
    except Exception as e:
        raise Exception(f"Failed to delete image on Cloudinary: {str(e)}")