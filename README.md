# Rate limit test

For testing rate limit

## Prerequisites

setting configuration

1. edit setting.json
   - url
   - http header
   - http post data

```
{
    "url": "https://www.google.com",

    "header": {
        "User-Agent": "thread-test",
        "Content-Type": "application/x-www-form-urlencoded"
    },

    "data": {
        "user_email": "test@hanmail.net",
        "arg1": "abcd",
        "arg2": "1234"
    }
}
```

## Usage

```
python ratelimit.py <thread count>
```

e.g)

```
python ratelimit.py 10
```
