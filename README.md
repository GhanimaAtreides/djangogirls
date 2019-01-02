# Ghanima's blog

## Admin

Local admin: http://localhost:8000/admin

## Development

### Start

in the same folder where this file is:

```sh
docker-compose up -d
```

### Stop

```sh
docker-compose down
```

### Logs

```sh
docker-compose logs -f web
```

### Deploy

1. Commit
2. `git push heroku master`