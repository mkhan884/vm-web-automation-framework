# Step 1: Run pytest with allure results - rerun twice with a delay of 1s
pytest \
  --alluredir=allure-results \
  --reruns 2 \
  --reruns-delay 1 \
  -v

# Step 2: Copy history if exists
if [ -d "allure-report/history" ]; then
  cp -r allure-report/history allure-results/
fi

# Step 3: Generate allure report
allure generate allure-results --clean -o allure-report

# Step 4: Open the report
allure open allure-report
