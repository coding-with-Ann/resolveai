# ResolveAI

ResolveAI is a beginner-to-production Applied AI project.

## Day 1
- Initialized FastAPI backend
- Added root endpoint
- Added health check endpoint


1. What is FastAPI?

FastAPI is a modern Python web framework used to build APIs quickly and cleanly. It is especially useful for backend services that need strong validation, automatic API documentation, and easy integration with AI/ML systems.

2. What is an API endpoint?

An API endpoint is a specific URL path in a backend service that performs a defined action or returns specific data.

Examples:

/ → root endpoint

/health → health check

/about → service metadata

/ping → quick connectivity test

3. What does @app.get() do?

@app.get() defines a GET route in FastAPI. It tells FastAPI that when a client sends a GET request to a specific path, the attached function should run and return a response.

4. Why are health endpoints important?

Health endpoints are used to quickly check whether the service is running correctly. In real systems, they are commonly used by:

monitoring tools

load balancers

deployment systems

container orchestration platforms like Kubernetes

5. Why is this relevant to Applied AI Engineering?

Applied AI systems are often deployed as APIs. Even if the core intelligence comes from an LLM or ML model, the model usually needs to be exposed through backend endpoints for real-world use. Learning FastAPI is the foundation for building production AI services.

Important Engineering Lesson

Every serious AI product needs a serving layer.
Models are not useful in production until they can be exposed through stable, testable, documented API endpoints.

Day 2 – Request Models, Response Models, POST Endpoints, and Validation
Key Concepts Learned
1. What is the difference between GET and POST?

GET is used to retrieve or fetch data from the server.

POST is used to send data to the server, often to create or process something.

Examples:

GET /health → fetch service status

POST /tickets/preview → send ticket data for processing

2. What does Pydantic do in FastAPI?

Pydantic is used for:

input validation

type enforcement

required field checking

data parsing into structured Python objects

It helps define clear API contracts between the client and the backend.

3. Why do we use response_model= in FastAPI?

response_model= tells FastAPI what response schema an endpoint should follow.

It helps with:

response validation

consistent output shape

automatic API documentation

serialization

catching mistakes early


Day 3 – Helper Functions, Conditionals, and Cleaner Backend Logic
Key Concepts Learned
1. Why are helper functions better than putting all logic directly inside endpoints?

Helper functions improve code reusability, readability, maintainability, and testability. They keep endpoints focused on handling requests and responses while moving business logic into reusable units that are easier to debug and test independently.

2. What does elif do?

elif means “else if.” It allows us to check another condition only if the previous if or elif conditions were false.

3. Why is classify_issue() useful beyond just one endpoint?

classify_issue() centralizes reusable business logic so multiple endpoints can use the same classification rules consistently without duplicating code. This is useful for tagging, triage, escalation, analytics, and routing.

4. In real Applied AI systems, what kinds of logic might move into helper functions?

Common examples include:

prompt construction

model routing

validation

output parsing

retry logic

fallback behavior

tool selection

confidence checks

response formatting



Day 4 – Modular Project Structure and Separation of Concerns
Key Concepts Learned
1. Why is splitting code into main.py, schemas.py, and logic.py better than keeping everything in one file?

Splitting code into separate modules improves readability, maintainability, reusability, and debugging. It separates API routing, data contracts, and business logic so the codebase scales more cleanly as the project grows.

2. What kind of code should go into schemas.py?

schemas.py should contain Pydantic request and response models that define the input and output contracts of the API.

3. What kind of code should go into logic.py?

logic.py should contain reusable business logic and helper functions, so endpoints stay focused on request handling and response construction.

4. Why is modular structure especially useful in Applied AI systems?

Modular structure is especially useful in Applied AI systems because AI applications quickly grow into multiple components such as schemas, prompt builders, model clients, retrieval logic, tool orchestration, evaluation code, and API routes. Separating these concerns makes the system easier to test, maintain, extend, and debug as complexity increases.

5. What does uvicorn app.main:app --reload mean?

uvicorn starts the ASGI server

app is the Python package/folder

main is the module/file

app after the colon is the FastAPI application object inside main.py

--reload automatically restarts the server whenever code changes are saved during development


Modularization is not just about cleanliness — it is about scalability.
As systems grow, clear separation between routing, schemas, and logic makes refactoring safer and future expansion much easier.


