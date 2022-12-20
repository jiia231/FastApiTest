# Task

### Description
The main idea is to create application, 
where users can create new posts to 
sell their products.

### Stack: 
* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL

### Requirements:
1) Registration, login, logout endpoints. Use JWT token
2) Logic, described above
3) Use linters and formatters. Add pre-commit hook
4) Write unittests for endpoints
5) Prepare ReadMe file
6) *\*Optional*: make your project available to run with docker-compose up command.

### Endpoints

`POST /posts - create new post`
```json

{
"title": "Iphone 13",
"description": "...",
"price": 1000
}
```

`GET /posts - all posts`
Don't forget about pagination.
```json
[
{
"title": "Iphone 13",
"description": "...",
"price": 1000,
"is_active": True,
"created_at": "",
"updated_at": "",
"author": {
   "id": 1,
   "email": ""
   }
},
{
"title": "Iphone 12",
"description": "...",
"price": 800,
"is_active": True,
"created_at": "",
"updated_at": "",
"author": {
   "id": 2,
   "email": ""
   }
},
]
```

`GET /posts/{id} - get post by id`  
`UPDATE /posts/{id} - update post by id`  
`DELETE /posts/{id} - delete post by id`

Users can also leave comments under post

`POST /posts/{id}/comments`
```json
{
"comment": "Don't buy iphone 13, Samsung is better"
}
```

`GET /posts/{id}/comments`
```json
[
{
"comment": "Don't buy  iphone 13, Samsung is better",
"author": 1,
"created_at": ""
},
{
"comment": "It's too expensive",
"author": 2,
"created_at": ""
}
]
```
