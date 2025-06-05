from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import admin, job
from routes import candidate  # add this

app = FastAPI()

# CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify e.g., ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
app.include_router(admin.router, tags=["Admin"])
app.include_router(job.router, tags=["Job"])
app.include_router(candidate.router, tags=["Candidate"])


from apscheduler.schedulers.asyncio import AsyncIOScheduler
from routes.admin import router as admin_router

# Global scheduler
scheduler = AsyncIOScheduler()
scheduler.start()

# Add routers
app.include_router(admin_router)

# Provide scheduler to other modules
@app.on_event("startup")
async def startup_event():
    print("Scheduler started.")
