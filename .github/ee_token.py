import os

ee_token = os.environ["EARTHENGINE_TOKEN"]
credential = {"client_id": "454402516203-a4v7q5aadogq560rc4g6npruv9m39lto.apps.googleusercontent.com", "client_secret": "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", "refresh_token": "1//0eVBUElFCewX-CgYIARAAGA4SNwF-L9IrQo1hbFHmkNF0OztAlBoXNdhitKSNiWJguJP7YqhPtsZu1obJEHP_5hM-wwdJPpW7sy0", "scopes": ["https://www.googleapis.com/auth/earthengine", "https://www.googleapis.com/auth/devstorage.full_control"]}
credential_file_path = os.path.expanduser("~/.config/earthengine/")
os.makedirs(credential_file_path, exist_ok=True)
with open(credential_file_path + "credentials", "w") as file:
    file.write(credential)
