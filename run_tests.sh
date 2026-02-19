#!/usr/bin/env bash
# Step 1: Run pytest with allure results - rerun once with a delay of 1s
# Enable undetected-chromedriver by exporting USE_UNDETECTED=true if desired
export USE_UNDETECTED=${USE_UNDETECTED:-true}

pytest \
  --alluredir=allure-results \
  --reruns 1 \
  --reruns-delay 1 \
  -v

# Optional: quick CI diagnostic (uncomment in CI to run)
# curl -I -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" https://www.virginmobile.ae
# CI smoke test using the updated driver (uncomment to run)
# CI=true USE_UNDETECTED=true python -c "from utils.driver import get_driver; d=get_driver(); d.get('https://www.virginmobile.ae'); print(d.title); d.quit()"
