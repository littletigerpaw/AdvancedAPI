# Mechanic Shop API - BackendP2

Flask API for managing customers, mechanics, and service tickets with Render deployment support and a GitHub Actions CI/CD pipeline.

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variables in `.env`.
4. Run the app.

   ```bash
   gunicorn flask_app:app
   ```

## Deployment Notes

- `flask_app.py` is the production entry point.
- `ProductionConfig` reads `SECRET_KEY` and `DATABASE_URL` from the environment with `os.getenv`.
- Add `SECRET_KEY` and `DATABASE_URL` in Render when creating the web service.
- After deployment, update `swagger.json`:
  - change `host` from `127.0.0.1:5000` to your Render base URL without `https://`
  - change `schemes` from `http` to `https`

## CI/CD

The workflow in `.github/workflows/main.yaml` runs:

1. Build: installs dependencies and compiles the project.
2. Test: runs `pytest`.
3. Deploy: triggers a Render deploy only after the test job passes.

Store these GitHub repository secrets before enabling the deploy job:

- `RENDER_SERVICE_ID`
- `RENDER_API_KEY`

## API Endpoints

Customers

- `POST /customers/`
- `GET /customers/`
- `GET /customers/<int:customer_id>`
- `PUT /customers/<int:customer_id>`
- `DELETE /customers/<int:customer_id>`

Mechanics

- `POST /mechanics/`
- `GET /mechanics/`
- `PUT /mechanics/<int:id>`
- `DELETE /mechanics/<int:id>`

Service Tickets

- `POST /service-tickets/`
- `GET /service-tickets/`
- `PUT /service-tickets/<int:ticket_id>/assign-mechanic/<int:mechanic_id>`
- `PUT /service-tickets/<int:ticket_id>/remove-mechanic/<int:mechanic_id>`
