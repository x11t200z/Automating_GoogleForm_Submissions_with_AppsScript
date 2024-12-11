import csv
import random

def generate_responses(output_file, num_responses):
    # Các lựa chọn với trọng số thực tế hơn
    column_1_choices = ["Có", "Không"]
    column_2_choices = ["Nam", "Nữ"]
    column_3_choices = ["18-25", "26-35", "36-45", "Từ 45 trở lên"]
    column_4_choices = ["Sản xuất", "Bán hàng và Tiếp thị", "Nhân sự", "Nghiên cứu và Phát triển", "Tài chính"]
    column_5_choices = ["Dưới 1 năm", "1-5 năm", "5-10 năm", "Trên 10 năm"]
    column_6_choices = ["Hiếm khi", "Hàng ngày", "Hàng tuần", "Hàng tháng"]

    # Trọng số (weights) cho các lựa chọn
    column_1_weights = [0.8, 0.2]  # "Không" chiếm khoảng 5%
    column_2_weights = [0.6, 0.4]  # Nam chiếm 60%
    column_3_weights = [0.3, 0.4, 0.2, 0.1]  # Phân phối độ tuổi
    column_4_weights = [0.2, 0.3, 0.1, 0.25, 0.15]  # Ngành nghề
    column_5_weights = [0.3, 0.4, 0.2, 0.1]  # Thâm niên làm việc
    column_6_weights = [0.1, 0.4, 0.3, 0.2]  # Tần suất sử dụng

    # Mở tệp để ghi
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Tiêu đề cột
        header = ["Cột 1", "Cột 2", "Cột 3", "Cột 4", "Cột 5", "Cột 6"] + [f"Cột {i}" for i in range(7, 33)]
        writer.writerow(header)

        # Sinh dữ liệu ngẫu nhiên
        for _ in range(num_responses):
            column_1 = random.choices(column_1_choices, weights=column_1_weights, k=1)[0]
            
            # Nếu cột 1 là "Không", các cột còn lại sẽ để trống
            if column_1 == "Không":
                row = [column_1] + [""] * (len(header) - 1)
            else:
                # Sinh dữ liệu ngẫu nhiên cho các cột còn lại
                column_2 = random.choices(column_2_choices, weights=column_2_weights, k=1)[0]
                column_3 = random.choices(column_3_choices, weights=column_3_weights, k=1)[0]
                column_4 = random.choices(column_4_choices, weights=column_4_weights, k=1)[0]
                column_5 = random.choices(column_5_choices, weights=column_5_weights, k=1)[0]
                column_6 = random.choices(column_6_choices, weights=column_6_weights, k=1)[0]

                # Các giá trị từ cột 7 đến 32 (ngẫu nhiên trong khoảng 1 đến 5)
                other_columns = [random.randint(1, 5) for _ in range(7, 33)]

                # Tạo dòng dữ liệu
                row = [column_1, column_2, column_3, column_4, column_5, column_6] + other_columns

            writer.writerow(row)

# Tạo dữ liệu
output_file = "responses_realistic.csv"
num_responses = 225  # Số lượng phiếu trả lời
generate_responses(output_file, num_responses)
print(f"Đã tạo tệp {output_file} với {num_responses} phiếu trả lời.")
