"""The common module contains common functions and classes used by the other modules.
"""

import os
import ee

def ee_initilization(token_name = 'EARTHENGINE_TOKEN'):
    """Authentication Earth Engine and initialize an Earth Engine session"""
    if ee.data._credentials is None:
        try:
            ee_token = os.environ.get(token_name)
            if ee_token is not None:
                credential_file_path = os.path.expanduser('~/.config/earthengine/')
                if not os.path.exists(credential_file_path):
                    credential = '{"refresh_token" : "%s"}' % ee_token
                    os.makedirs(credential_file_path, exist_ok=True)
                    with open(credential_file_path+"cerdentials", 'w') as file:
                        file.write(credential)

            ee.Initialize()
        except Exception:
            ee.Authenticate()
            ee.Initialize()