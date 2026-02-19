# Step 1: Run pytest with allure results - rerun twice with a delay of 1s
pytest \
  --alluredir=allure-results \
  --reruns 2 \
  --reruns-delay 1 \
  -v
