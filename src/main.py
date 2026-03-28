import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    
    # Use 'agents_dir' (PLURAL)
    # This points to the parent folder of your agent packages
    current_dir = os.path.dirname(os.path.abspath(__file__))
    agents_root = os.path.join(current_dir, "agent") 

    app = get_fast_api_app(
        agents_dir=agents_root, 
        web=True
    )

    uvicorn.run(app, host="0.0.0.0", port=port)