from selenium import webdriver

def test_smoke_the_internet():
    # 1. Khởi tạo phiên làm việc (Setup)
    driver = webdriver.Chrome()
    
    try:
        # 2. Thực thi hành động (Act)
        driver.get("https://the-internet.herokuapp.com/")
        
        # 3. Kiểm chứng kết quả (Assert)
        actual_title = driver.title
        assert actual_title == "The Internet", f"Lỗi: Tiêu đề thực tế là '{actual_title}'"
        # So sánh xem tiêu đề của trang web trên có phải là The Internet hay không, nếu không phải thì sẽ báo lỗi
        #và ghi lại đúng tên tiêu đề, phải sửa lại code python để lỗi pass
    finally:
        # 4. Dọn dẹp (Teardown)
        driver.quit()