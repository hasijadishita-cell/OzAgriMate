# OzAgriMate

OzAgriMate is a software architecture project developed for RMIT ISYS3459.

The project demonstrates a service-based architecture with event-driven IoT processing using Python FastAPI.

## Project Structure

- `farm-management-service` - manages farms, users, and farm settings
- `sensor-data-service` - receives and processes IoT sensor readings
- `farm-monitoring-service` - provides farm monitoring and condition data
- `irrigation-management-service` - manages irrigation schedules and commands
- `authentication-service` - handles authentication and access control
- `alert-service` - processes sensor events and creates alerts
- `ai-integration-service` - integrates with an external AI service
- `reporting-service` - handles compliance and water usage reporting

## Technology

- Python
- FastAPI
- Uvicorn
- In-memory data only

## Implementation Scope

Only the 8 REST API endpoints documented in the Assignment 4 API Design section are implemented.

The UI, API Gateway, message broker, databases, and deployment infrastructure are represented architecturally but are not required to be implemented.

## Running a Service

Example:

```bash
cd irrigation-management-service
uvicorn app.main:app --reload --port 8003