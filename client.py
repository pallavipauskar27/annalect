import requests

base_url = "http://127.0.0.1:8000"

# 1. Add a place
place_data = {
    "name": "Sample Place",
    "location_lat": 12.34,
    "location_long": 56.78,
    "description": "A description for the sample place",
    "type": "Type of the place"
}
response = requests.post(f"{base_url}/place/", json=place_data)
place_id = response.json()["id"]
print(f"Added place with ID: {place_id}")

# 2. Update the place
update_data = {
    "name": "Updated Sample Place"
}
response = requests.put(f"{base_url}/place/{place_id}/", json=update_data)
print("Updated place:", response.json())

# 3. Add a photo to the place
photo_data = {
    "url": "http://example.com/photo1.jpg"
}
response = requests.post(f"{base_url}/place/{place_id}/photo/", json=photo_data)
photo_id = response.json()["id"]
print(f"Added photo with ID: {photo_id} to place with ID: {place_id}")

# 4. Update the photo
photo_update_data = {
    "url": "http://example.com/photo1-updated.jpg"
}
response = requests.put(f"{base_url}/photo/{photo_id}/", json=photo_update_data)
print("Updated photo:", response.json())

# 5. Delete the photo
response = requests.delete(f"{base_url}/photo/{photo_id}/")
print(response.json())

# 6. List all photos
response = requests.get(f"{base_url}/photos/")
print("All photos:", response.json())

# 7. List all places
response = requests.get(f"{base_url}/places/")
print("All places:", response.json())

# Delete the place (cleanup)
response = requests.delete(f"{base_url}/place/{place_id}/")
print(response.json())
