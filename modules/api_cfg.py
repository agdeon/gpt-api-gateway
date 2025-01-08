import json
import os

class ApiCfg:
    CFG_FILEPATH = "cfg.json"

    def __init__(self):
        self.config_data = None
        self.model_options = None

        if self.cfg_exists():
            self.load_cfg()
        else:
            self.create_cfg()

    def cfg_exists(self):
        return os.path.exists(self.CFG_FILEPATH)

    def load_cfg(self):
        try:
            with open(self.CFG_FILEPATH, 'r') as f:
                data = json.load(f)

            for key, value in data.items():
                setattr(self, key, value)

            self.config_data = data

        except json.JSONDecodeError:
            print(f"Error reading JSON from file {self.CFG_FILEPATH}.")
        except Exception as e:
            print(f"Error: {e}")

    def create_cfg(self):
        data = { "model_options": ["gpt-4o-mini", "gpt-3.5-turbo"] }
        with open(self.CFG_FILEPATH, "w") as f:
            json.dump(data, f, indent=4)