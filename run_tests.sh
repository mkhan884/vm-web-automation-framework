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

# make sure the output directory exists even if report generation fails
mkdir -p allure-report

# Step 3: Generate allure report
allure generate allure-results --clean -o allure-report

# Step 4: Open the report (optional)
# this will fail in headless CI; the script may be running locally
allure open allure-report || true
