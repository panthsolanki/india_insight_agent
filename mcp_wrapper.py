from fastmcp import Client

MCP_URL = "https://mcp.mospi.gov.in/mcp"
client = Client(MCP_URL)


class MCPWrapper:
    def __init__(self):
        self.datasets_cache = None

    # ---- STEP 1: Fetch datasets ----
    def get_datasets(self):
        if not self.datasets_cache:
            self.datasets_cache = client.call("get_datasets", {})
        return self.datasets_cache

    # ---- STEP 2: Smart dataset selection ----
    def select_dataset(self, user_query: str):
        datasets = self.get_datasets()

        query = user_query.lower()

        # Keyword mapping (fallback logic)
        keyword_map = {
            "inflation": "CPI",
            "price": "CPI",
            "cost": "CPI",
            "gdp": "GDP",
            "growth": "GDP",
            "economy": "GDP",
            "job": "PLFS",
            "employment": "PLFS",
            "unemployment": "PLFS"
        }

        # First: keyword match
        for key, dataset in keyword_map.items():
            if key in query:
                return dataset

        # Second: dynamic matching from MCP datasets
        if isinstance(datasets, list):
            for ds in datasets:
                name = str(ds).lower()
                if any(word in name for word in query.split()):
                    return ds

        # Fallback
        return "CPI"

    # ---- STEP 3: Explore indicators (optional but powerful) ----
    def get_indicators(self, dataset):
        try:
            return client.call("get_indicators", {"dataset": dataset})
        except:
            return []

    # ---- STEP 4: Query data safely ----
    def fetch_data(self, dataset):
        try:
            return client.call("get_data", {"dataset": dataset})
        except Exception as e:
            return {"error": str(e)}

    # ---- MAIN FLOW ----
    def query(self, user_query: str):
        try:
            dataset = self.select_dataset(user_query)

            # Optional: explore indicators
            indicators = self.get_indicators(dataset)

            data = self.fetch_data(dataset)

            return {
                "selected_dataset": dataset,
                "available_indicators": indicators[:5] if isinstance(indicators, list) else indicators,
                "data": data
            }

        except Exception as e:
            return {"error": str(e)}


# Singleton
mcp_wrapper = MCPWrapper()