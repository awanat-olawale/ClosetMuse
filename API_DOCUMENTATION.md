# ClosetMuse API Documentation (One-Page)

ClosetMuse is a digital wardrobe API with four apps: **users**, **wardrobe**, **planner**, and **declutter**.  
Some endpoints require the user to be **logged in**.

---

## 1. Users App

- **POST /api/users/register/**  
  Body: `{ "username": "", "email": "", "password": "" }`  
  Description: Register a new user

- **POST /api/users/login/**  
  Body: `{ "email": "", "password": "" }`  
  Description: Login and receive authentication info

- **GET /api/users/profile/**  
  Description: Get authenticated user profile (requires login)

- **PUT /api/users/profile/**  
  Body: `{ "username": "", "email": "" }`  
  Description: Update user profile (requires login)

---

## 2. Wardrobe App

- **GET /api/wardrobe/items/**  
  Description: List all clothing items (requires login)

- **POST /api/wardrobe/items/**  
  Body: `{ "name": "", "category": "", "color": "", "image": "" }`  
  Description: Add a new clothing item (requires login)

- **GET /api/wardrobe/items/<id>/**  
  Description: Get a single item (requires login)

- **PUT /api/wardrobe/items/<id>/**  
  Body: `{ "name": "", "category": "", "color": "" }`  
  Description: Update a clothing item (requires login)

- **DELETE /api/wardrobe/items/<id>/**  
  Description: Delete a clothing item (requires login)

- **GET /api/wardrobe/outfits/?date=YYYY-MM-DD**  
  Description: List outfits (optional date filter, requires login)

- **POST /api/wardrobe/outfits/**  
  Body: `{ "item_ids": [], "date": "" }`  
  Description: Create a new outfit (requires login)

---

## 3. Planner App

- **GET /api/planner/schedule/?start_date=&end_date=**  
  Description: List planned outfits (optional date range, requires login)

- **POST /api/planner/schedule/**  
  Body: `{ "outfit_id": 1, "date": "" }`  
  Description: Schedule an outfit (requires login)

- **PUT /api/planner/schedule/<id>/**  
  Body: `{ "date": "" }`  
  Description: Update scheduled outfit (requires login)

- **DELETE /api/planner/schedule/<id>/**  
  Description: Delete scheduled outfit (requires login)

---

## 4. Declutter App

- **GET /api/declutter/items/**  
  Description: List declutter items (requires login)

- **POST /api/declutter/items/**  
  Body: `{ "item_id": 1, "status": "donate/sell/archive" }`  
  Description: Add item to declutter list (requires login)

- **PUT /api/declutter/items/<id>/**  
  Body: `{ "status": "" }`  
  Description: Update declutter item status (requires login)

- **DELETE /api/declutter/items/<id>/**  
  Description: Remove declutter item (requires login)
