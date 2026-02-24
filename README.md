# e-commerce-be
# structure
e-commerce-be/
    app/
        main.py
        controllers/
        models/
        routes/
        schemas/
        core/
    venv/
    requirements.txt
    .gitignore
    README.md

# Workflow
cd e-commerce-be
source venv/Scripts/activate
# freeze
python -m pip freeze > requirements.txt
# run project 
uvicorn app.main:app --reload --port 8001