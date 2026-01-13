import os
from imagekitio import ImageKit


def get_imagekit_client():
    return ImageKit()
        #public_key=os.environ.get("IMAGEKIT_PUBLIC_KEY"),
        #private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
        #url_endpoint=os.environ.get("IMAGEKIT_URL_ENDPOINT", "https://ik.imagekit.io/default")
    


def _get_watermark_transformation(username: str):
    return (
        "l-text,",
        f"i-{username},",
        "lfo-bottom_left,",
        "lx-10,ly-10,",
        "fs-32,",
        "co-FFFFFF,",
        "bg-00000060,",
        "pa-4_8,",
        "l-end"
    )


def get_optimized_video_url(base_url: str) -> str:
    if "?" in base_url:
        return f"{base_url}&tr=q-50,f-auto"
    return f"{base_url}?tr=q-50,f-auto"


def get_streaming_url(base_url: str) -> str:
    return f"{base_url}/ik-master.m3u8?tr=sr-240_360_480_720_1080"


def get_thumbnail_url(
        base_url: str, username: str = None
) -> str:
    transformations = "".join(_get_watermark_transformation(username))

    return f"{base_url}/ik-thumbnail.jpg?tr={transformations}"


def add_image_watermark(
        base_url: str, username: str = None
) -> str:
    transformations = "".join(_get_watermark_transformation(username))

    return f"{base_url}?tr={transformations}"


def upload_video(file_data: bytes, file_name: str, folder: str = "videos") -> dict:
    client = get_imagekit_client()
    
    response = imagekit.files.upload(
        file=file_data,
        file_name=file_name,
        folder=folder,
        use_unique_file_name=True,
    )
    
    return {
        "file_id": response.file_id,
        "url": response.url
    }


def upload_thumbnail(file_data: str, file_name: str, folder: str = "thumbnails") -> dict:
    import base64
    
    if file_data.startswith("data:"):
        base64_data = file_data.split(",", 1)[1]
        image_bytes = base64.b64decode(base64_data)
    else:
        image_bytes = base64.b64decode(file_data)

    client = get_imagekit_client()
    
    response = client.upload_file(
        file=image_bytes,
        file_name=file_name,
        options={
            "folder": folder,
            "use_unique_file_name": True,
        }
    )
    
    return {
        "file_id": response.file_id,
        "url": response.url
    }


def delete_video(file_id: str) -> bool:
    client = get_imagekit_client()
    imagekit.files.delete(file_id=file_id)
    return True
