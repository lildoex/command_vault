#!/bin/bash

echo "Starting CommandVault..."

# Sestaví obraz (pokud byly změny)
docker build -t command-vault .

# Spustí kontejner na pozadí (-d jako detached mode)
# --rm zajistí, že se po vypnutí kontejner sám uklidí
docker run -d -p 5000:5000 --name my_vault -v $(pwd):/app --rm command-vault

echo "Application is running at http://localhost:5000"
echo "To stop it, run: docker stop my_vault"