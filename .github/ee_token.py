import os

ee_token = os.environ["EARTHENGINE_TOKEN"]
credential = '{"client_id": "454402516203-a4v7q5aadogq560rc4g6npruv9m39lto.apps.googleusercontent.com", "client_secret": "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", "refresh_token": "%s", "scopes": ["https://www.googleapis.com/auth/earthengine", "https://www.googleapis.com/auth/devstorage.full_control"]}' % ee_token
credential_file_path = os.path.expanduser("~/.config/earthengine/")
os.makedirs(credential_file_path, exist_ok=True)
with open(credential_file_path + "credentials", "w") as file:
    file.write(credential)
