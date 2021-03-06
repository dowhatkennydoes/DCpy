# Import the required library
import requests

# Get the zip file
response = requests.get('https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip')

# Print the status code
print(response.status_code)

# Save the file locally (more about open() in the next lesson)
local_path = f"tmp/data/source/downloaded_at=2021-02-01/PPR-ALL.zip"
with open(local_path, "wb") as f:
    f.write(response.content)