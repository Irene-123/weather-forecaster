from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    
    yield driver
    
    driver.quit()


# ═══════════════════════════════════════════════════════════
# TEST 1: Successful Login
# ═══════════════════════════════════════════════════════════

def test_successful_login(driver):
    
    driver.get("https://practicetestautomation.com/practice-test-login/")

    print("Finding username by ID...")
    username = driver.find_element(By.ID, "username")
    username.send_keys("student")

    print("Finding password by XPATH...")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("Password123")

    print("Finding submit button by CSS_SELECTOR...")
    submit = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit.click()
    
    assert "logged-in-successfully" in driver.current_url
    print("✓ Login successful!")
    
    print("Finding success message by CLASS_NAME...")
    success_msg = driver.find_element(By.CLASS_NAME, "post-title")
    assert "Logged In Successfully" in success_msg.text
    print(f"✓ Message: {success_msg.text}")
    print("Finding logout button by LINK_TEXT...")
    logout = driver.find_element(By.LINK_TEXT, "Log out")
    logout.click()
    print("✓ Logged out successfully")


# ═══════════════════════════════════════════════════════════
# TEST 2: Invalid Username
# ═══════════════════════════════════════════════════════════

def test_invalid_username(driver):
    """Test login with invalid username - More Locator Examples"""
    print("\n" + "="*60)
    print("Test 2: Invalid Username - More Locator Examples")
    print("="*60)
    
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Find username by XPATH with attribute
    print("Finding username by XPATH (with @name attribute)...")
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("wronguser")
    
    password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password.send_keys("Password123")
    
    # Find submit by ID (XPATH with @value was wrong!)
    print("Finding submit by ID...")
    submit = driver.find_element(By.ID, "submit")
    submit.click()
    # Check for error message by ID
    print("Finding error message by ID...")
    error = driver.find_element(By.ID, "error")
    assert "Your username is invalid!" in error.text
    print("✓ Error message displayed correctly")
    print(f"✓ Error: {error.text}")



# ═══════════════════════════════════════════════════════════
# TEST 3: Invalid Password
# ═══════════════════════════════════════════════════════════

def test_invalid_password(driver):
    """Test login with invalid password - Advanced Locators"""
    print("\n" + "="*60)
    print("Test 3: Invalid Password - Advanced Locators")
    print("="*60)
    
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Find username by XPATH (text contains)
    print("Finding username by XPATH (contains text)...")
    username = driver.find_element(By.XPATH, "//input[contains(@id, 'user')]")
    username.send_keys("student")
    
    # Find password by CSS_SELECTOR with ID
    print("Finding password by CSS_SELECTOR (#id)...")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("wrongpassword")
    
    # Find submit by ID
    print("Finding submit by ID...")
    submit = driver.find_element(By.ID, "submit")
    submit.click()
    
    # Check for error message by XPATH
    print("Finding error by XPATH...")
    error = driver.find_element(By.XPATH, "//div[@id='error']")
    assert "Your password is invalid!" in error.text
    print("✓ Error message displayed correctly")
    print(f"✓ Error: {error.text}")



def test_locator_summary(driver):
    """Summary of all locators used"""
    print("\n" + "="*60)
    print("LOCATOR SUMMARY - What We Used:")
    print("="*60)
    print("✓ By.ID              → find_element(By.ID, 'username')")
    print("✓ By.XPATH           → find_element(By.XPATH, '//input[@id=\"password\"]')")
    print("✓ By.CSS_SELECTOR    → find_element(By.CSS_SELECTOR, '#submit')")
    print("✓ By.CLASS_NAME      → find_element(By.CLASS_NAME, 'post-title')")
    print("✓ By.LINK_TEXT       → find_element(By.LINK_TEXT, 'Log out')")
    print("="*60)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    assert "Test Login" in driver.title


if __name__ == "__main__":
    import sys
    pytest.main([__file__, "-v", "-s"])