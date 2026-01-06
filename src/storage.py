import os
import json
class StorageManager:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    # serialization
    def save(self, data: list[dict]) -> None:
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except TypeError as e:
            print(f"Data Error: Some objects are not JSON serializable. {e}")
        except PermissionError:
            print(f"Permission Error: You do not have permission to write to this file.")
        except OSError as e:
            print(f"System Error: A disk or OS error occurred {e}.")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    # deserialization
    def load(self) -> list[dict]:
        if not os.path.exists(self.file_path):
            return []
        
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)            
        except FileNotFoundError:
            print(f"{self.file_path} is missing.")
            return []
        except json.JSONDecodeError:
            print(f"Warning: {self.file_path} is corrupted. Returning empty list.")
            return []
        except Exception as e:
            print(f"Unexpected Load Error: {e}")
            return []
        
