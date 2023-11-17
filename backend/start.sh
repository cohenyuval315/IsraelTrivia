docker compose build
docker compose up -d 
docker exec backend-backend-1 python scripts/insert_data.py
docker logs backend-backend-1
