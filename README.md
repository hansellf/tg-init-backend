
# Telegram Init Data Validator Backend

This FastAPI service validates Telegram WebApp `initData` and responds with dynamic TON payment data.

## Deploy on Render

- Set `BOT_TOKEN` as environment variable
- URL: `/init-data?initData=...&ton_amount=1.5&wallet=...&description=...`
