# 📁 Diplom_3

### 1. Password Recovery Tests
- [x] Navigate to Recover Password  
- [x] Enter email and click Recover  
- [x] Toggle password visibility highlights the field

### 2. Personal Account Tests
- [x] Click Personal Account  
- [x] Open Order History  
- [x] Sign out of the account

### 3. Main Functionality Tests
- [x] Click Constructor  
- [x] Click Order Feed  
- [x] Click an ingredient to open its detail popup  
- [x] Close the popup by clicking the ✕ icon  
- [x] Adding an ingredient increments its counter  
- [x] Authenticated user can place an order

### 4. Order Feed Tests
- [x] Click an order to open its detail popup  
- [x] Orders from Order History appear in Order Feed  
- [x] New orders increment Total Completed  
- [x] New orders increment Completed Today  
- [x] Placed orders show under In Progress

### 5. Allure Report
- [x] Report generated in `allure_report/`

### 6. Install dependencies  
pip install -r requirements.txt

### 7. Run tests  
pytest

### 8. Generate Allure report  
allure generate allure_results --clean -o allure_report

### 9. Open the report  
allure open allure_report
