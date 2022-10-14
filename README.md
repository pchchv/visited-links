<div align="center">

# Web application for recording visited links

</div>

## Running the application

```
docker-compose up --build
```

### Running the application without Docker

```
uvicorn main:app
```

## HTTP Methods

```
"GET" / — Checking the server connection

    example: 
        "GET" :8000/
```

```
"POST" /visited_links — Add new links. Need JSON body

    example: 
        "POST" :8080/visited_links
```

```json
{
    "links": [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "facebook.com",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
    ]
}
```

```
"GET" /visited_domains — Get unique domains visited in a given period

    example: 
        "GET" :8000/visited_domains?from=1545221231&to=1545217638
```
