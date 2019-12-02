import gemini
import os
from datetime import datetime

class GeminiClient:
    def __init__(self, api_key, api_secret, sandbox=False):
        self._auditor_api_key = api_key
        self._auditor_api_secret = api_secret
        self.public_client = gemini.PublicClient()
        self.private_client = gemini.PrivateClient(self._auditor_api_key, self._auditor_api_secret)
    
    def timestamp_to_datetime(self, timestamp):
        datetime.fromtimestamp(timestamp)