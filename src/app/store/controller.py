from fastapi import UploadFile
import io

class ExampleController:
    async def upload_image(self, image_file: UploadFile):
        image_data = image_file.file.read()
        ext = image_file.content_type[6:]
        print(image_file.filename)
        image_URL = f'static/{image_file.filename}'
        with open(image_URL, 'wb') as f:
            f.write(image_data)
        return image_URL
        # image_url = upload_image('bdprofilepics', f'{user_id}.{ext}', image_data, image_file.content_type)
        # return image_url

example_controller = ExampleController()