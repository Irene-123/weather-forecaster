"""
test_login.py - Login Tests
Uses 'driver' fixture from conftest.py automatically
"""

from selenium.webdriver.common.by import By

# ═══════════════════════════════════════════════════════════
# TEST 1: Successful Login
# ═══════════════════════════════════════════════════════════

def test_successful_login(driver):
    """Test login with valid credentials"""
    # Open page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Login
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    
    # Verify
    assert "logged-in-successfully" in driver.current_url
    
    success_msg = driver.find_element(By.CLASS_NAME, "post-title")
    assert "Logged In Successfully" in success_msg.text
    
    print("✓ Login successful!")


# ═══════════════════════════════════════════════════════════
# TEST 2: Invalid Username
# ═══════════════════════════════════════════════════════════

def test_invalid_username(driver):
    """Test login with invalid username"""
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    
    error = driver.find_element(By.ID, "error")
    assert "Your username is invalid!" in error.text
    
    print("✓ Invalid username detected!")


# ═══════════════════════════════════════════════════════════
# TEST 3: Invalid Password
# ═══════════════════════════════════════════════════════════

def test_invalid_password(driver):
    """Test login with invalid password"""
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "submit").click()
    
    error = driver.find_element(By.ID, "error")
    assert "Your password is invalid!" in error.text
    
    print("✓ Invalid password detected!")


# ═══════════════════════════════════════════════════════════
# TEST 4: Multiple Locators Example
# ═══════════════════════════════════════════════════════════

def test_different_locators(driver):
    """Test using different locator types"""
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # By ID
    driver.find_element(By.ID, "username").send_keys("student")
    
    # By XPATH
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password123")
    
    # By CSS_SELECTOR
    driver.find_element(By.CSS_SELECTOR, "#submit").click()
    
    # By CLASS_NAME
    success_msg = driver.find_element(By.CLASS_NAME, "post-title")
    assert success_msg.is_displayed()
    
    # By LINK_TEXT
    logout = driver.find_element(By.LINK_TEXT, "Log out")
    assert logout.is_displayed()