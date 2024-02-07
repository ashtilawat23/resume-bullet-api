from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Read the API description from README.md, skipping the first line
with open("README.md", "r") as file:
    next(file)  # Skip the first line
    api_description = file.read()

# Define API metadata
API_VERSION = "0.0.1"
API_TITLE = 'Resume Bullet API'
API_DESCRIPTION = api_description
DOCS_URL = '/'

# Initialize the FastAPI application with metadata
API = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
    docs_url=DOCS_URL,
)

# Configure CORS policy for the API to allow requests from any origin
API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow all origins
    allow_credentials=True,
    allow_methods=['*'],  # Allow all methods
    allow_headers=['*'], 
)

# Define an endpoint to get the API version
@API.get("/version", tags=["General"])
async def get_api_version():
    """Returns the current version of the API."""
    return API_VERSION

# Define an endpoint to return a dummy resume bullet point
@API.get("/resume-bullet", tags=["Resume"])
async def get_resume_bullet():
    """Returns a dummy resume bullet point."""
    return "Developed a RESTful API using FastAPI to serve resume bullet points from a database and deployed it to a cloud platform."